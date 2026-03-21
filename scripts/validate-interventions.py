#!/usr/bin/env python3
"""
Validates the integrity of the intervention database.

Checks:
1. Domain key existence: every domain.value key in interventions exists in values.yml
2. No anchor fields: no intervention file contains anchor_type, anchor_max, anchor_unit, anchor_description
3. File naming: all files in _data/interventions/ use kebab-case (no underscores)
4. Required fields: each value entry has pbs, pbs_reasoning, isr, isr_reasoning, uar, uar_reasoning
5. Score ranges: PBS 0-10, ISR 0-100, UAR 0-100
6. intervention_key match: each .md page has a key that corresponds to an actual YAML file
"""

import os
import re
import sys
from pathlib import Path

# Resolve paths relative to the script location
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
DATA_DIR = PROJECT_ROOT / "_data"
INTERVENTIONS_DIR = DATA_DIR / "interventions"
VALUES_FILE = DATA_DIR / "values.yml"
PAGES_DIR = PROJECT_ROOT / "resources" / "intervention-database"

ANCHOR_FIELDS = {"anchor_type", "anchor_max", "anchor_unit", "anchor_description"}
REQUIRED_VALUE_FIELDS = {"pbs", "pbs_reasoning", "isr", "isr_reasoning", "uar", "uar_reasoning"}


def parse_values_keys(filepath):
    """Parse values.yml to extract all valid domain.value keys (e.g. fitness.health)."""
    keys = set()
    current_domain = None
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            # Skip comments and blank lines
            stripped = line.rstrip()
            if not stripped or stripped.lstrip().startswith("#"):
                continue
            # Top-level domain: no leading whitespace, ends with ':'
            if not line[0].isspace() and ":" in stripped:
                current_domain = stripped.split(":")[0].strip()
            # Second-level value: exactly 2 spaces indent, ends with ':'
            elif re.match(r"^  \S", line) and ":" in stripped and current_domain:
                value_name = stripped.strip().split(":")[0].strip()
                keys.add(f"{current_domain}.{value_name}")
    return keys


def parse_intervention_yaml(filepath):
    """Parse an intervention YAML file and return value entries as a list of dicts.

    Returns a list of (domain_key, {field: value}) tuples for each values entry,
    plus a flag indicating whether any anchor fields were found.
    """
    value_entries = []
    has_anchor_fields = []
    in_values_block = False
    current_domain_key = None
    current_fields = {}

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        stripped = line.rstrip()

        # Check for anchor fields anywhere in the file
        for af in ANCHOR_FIELDS:
            if re.match(rf"^\s+{af}\s*:", line):
                has_anchor_fields.append(af)

        # Detect start of values block
        if re.match(r"^values\s*:", stripped):
            in_values_block = True
            continue

        if not in_values_block:
            continue

        # End of values block: a new top-level key
        if stripped and not stripped.startswith(" ") and not stripped.startswith("#"):
            in_values_block = False
            if current_domain_key and current_fields:
                value_entries.append((current_domain_key, dict(current_fields)))
            continue

        # Domain key line (e.g. " fitness.health:" with leading spaces)
        domain_match = re.match(r"^\s+([\w\-]+\.[\w\-]+)\s*:", stripped)
        if domain_match:
            if current_domain_key and current_fields:
                value_entries.append((current_domain_key, dict(current_fields)))
            current_domain_key = domain_match.group(1)
            current_fields = {}
            continue

        # Field line (e.g. "   pbs: 7")
        field_match = re.match(r"^\s+(pbs|pbs_reasoning|isr|isr_reasoning|uar|uar_reasoning)\s*:\s*(.*)", stripped)
        if field_match and current_domain_key:
            field_name = field_match.group(1)
            field_value = field_match.group(2).strip().strip('"')
            current_fields[field_name] = field_value

    # Flush last entry
    if current_domain_key and current_fields:
        value_entries.append((current_domain_key, dict(current_fields)))

    return value_entries, has_anchor_fields


def parse_md_frontmatter(filepath):
    """Extract intervention_key from a markdown file's YAML frontmatter."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None
    frontmatter = match.group(1)
    key_match = re.search(r"^intervention_key\s*:\s*(.+)$", frontmatter, re.MULTILINE)
    if key_match:
        return key_match.group(1).strip().strip('"').strip("'")
    return None


def main():
    issues = []

    # Load valid domain.value keys from values.yml
    if not VALUES_FILE.exists():
        print(f"ERROR: {VALUES_FILE} not found")
        sys.exit(1)
    valid_keys = parse_values_keys(VALUES_FILE)

    # Get all intervention YAML files
    if not INTERVENTIONS_DIR.exists():
        print(f"ERROR: {INTERVENTIONS_DIR} not found")
        sys.exit(1)
    yml_files = sorted(INTERVENTIONS_DIR.glob("*.yml"))
    yml_basenames = {f.stem for f in yml_files}

    for yml_file in yml_files:
        filename = yml_file.name
        stem = yml_file.stem

        # Check 3: File naming (kebab-case, no underscores)
        if "_" in stem:
            issues.append(f"[NAMING] {filename}: contains underscores (should be kebab-case)")
        if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", stem):
            issues.append(f"[NAMING] {filename}: does not match kebab-case pattern")

        # Parse the intervention file
        value_entries, anchor_fields = parse_intervention_yaml(yml_file)

        # Check 2: No anchor fields
        for af in anchor_fields:
            issues.append(f"[ANCHOR] {filename}: contains forbidden field '{af}'")

        for domain_key, fields in value_entries:
            # Check 1: Domain key existence
            if domain_key not in valid_keys:
                issues.append(f"[DOMAIN] {filename}: domain key '{domain_key}' not found in values.yml")

            # Check 4: Required fields
            missing = REQUIRED_VALUE_FIELDS - set(fields.keys())
            if missing:
                issues.append(f"[FIELDS] {filename} [{domain_key}]: missing required fields: {', '.join(sorted(missing))}")

            # Check 5: Score ranges
            for score_field, min_val, max_val in [("pbs", 0, 10), ("isr", 0, 100), ("uar", 0, 100)]:
                if score_field in fields:
                    try:
                        val = float(fields[score_field])
                        if val < min_val or val > max_val:
                            issues.append(
                                f"[RANGE] {filename} [{domain_key}]: {score_field}={val} "
                                f"out of range [{min_val}-{max_val}]"
                            )
                    except ValueError:
                        issues.append(
                            f"[RANGE] {filename} [{domain_key}]: {score_field} is not numeric: "
                            f"'{fields[score_field]}'"
                        )

    # Check 6: intervention_key match in .md pages
    if PAGES_DIR.exists():
        md_files = sorted(PAGES_DIR.glob("*.md"))
        for md_file in md_files:
            if md_file.stem == "index":
                continue
            key = parse_md_frontmatter(md_file)
            if key is None:
                issues.append(f"[KEY] {md_file.name}: no intervention_key in frontmatter")
            elif key not in yml_basenames:
                issues.append(f"[KEY] {md_file.name}: intervention_key '{key}' has no matching YAML file")

    # Summary
    print(f"Scanned {len(yml_files)} intervention YAML files")
    if PAGES_DIR.exists():
        page_count = len([f for f in PAGES_DIR.glob("*.md") if f.stem != "index"])
        print(f"Scanned {page_count} intervention page files")
    print(f"Valid domain keys in values.yml: {len(valid_keys)}")
    print()

    if issues:
        print(f"Found {len(issues)} issue(s):\n")
        for issue in issues:
            print(f"  {issue}")
        print()
        sys.exit(1)
    else:
        print("All checks passed. No issues found.")
        sys.exit(0)


if __name__ == "__main__":
    main()
