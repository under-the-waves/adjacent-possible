#!/usr/bin/env python3
"""
Phase B: Extract life area data from index.md pages into YAML files
and rewrite the markdown to use Jekyll includes.

Processes each life area's index.md to:
1. Parse values (name, weight, key, description)
2. Parse benchmarks (level, value key, text)
3. Parse reasoning (from <script> block)
4. Write YAML to _data/life_areas/{slug}.yml
5. Rewrite markdown to use includes
"""

import os
import re
import sys
import yaml

# Project root
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Taxonomy ──────────────────────────────────────────────────────────
# Maps each slug to its domain, pillar, and whether it's the domain representative.

TAXONOMY = {
    # Expand Your Awareness
    "self-awareness":        {"domain": "Values",       "pillar": "Expand Your Awareness", "domain_representative": True},
    "value-system":          {"domain": "Values",       "pillar": "Expand Your Awareness", "domain_representative": False},
    "life-purpose":          {"domain": "Purpose",      "pillar": "Expand Your Awareness", "domain_representative": True},
    "ethics":                {"domain": "Purpose",      "pillar": "Expand Your Awareness", "domain_representative": False},
    "media-diet":            {"domain": "Knowledge",    "pillar": "Expand Your Awareness", "domain_representative": True},
    "information-management":{"domain": "Knowledge",    "pillar": "Expand Your Awareness", "domain_representative": False},
    "worldview":             {"domain": "Knowledge",    "pillar": "Expand Your Awareness", "domain_representative": False},
    "rationality":           {"domain": "Knowledge",    "pillar": "Expand Your Awareness", "domain_representative": False},
    "cognitive-skills":      {"domain": "Learning",     "pillar": "Expand Your Awareness", "domain_representative": True},
    "life-skills":           {"domain": "Learning",     "pillar": "Expand Your Awareness", "domain_representative": False},
    "learning-methods":      {"domain": "Learning",     "pillar": "Expand Your Awareness", "domain_representative": False},

    # Look After Yourself
    "fitness":               {"domain": "Health",       "pillar": "Look After Yourself", "domain_representative": True},
    "nutrition":             {"domain": "Health",       "pillar": "Look After Yourself", "domain_representative": False},
    "sleep":                 {"domain": "Health",       "pillar": "Look After Yourself", "domain_representative": False},
    "health-management":     {"domain": "Health",       "pillar": "Look After Yourself", "domain_representative": False},
    "mindfulness":           {"domain": "Wellbeing",    "pillar": "Look After Yourself", "domain_representative": True},
    "mental-health":         {"domain": "Wellbeing",    "pillar": "Look After Yourself", "domain_representative": False},
    "behaviours":            {"domain": "Wellbeing",    "pillar": "Look After Yourself", "domain_representative": False},
    "physical-safety":       {"domain": "Security",     "pillar": "Look After Yourself", "domain_representative": True},
    "emergency-preparedness":{"domain": "Security",     "pillar": "Look After Yourself", "domain_representative": False},
    "digital-safety":        {"domain": "Security",     "pillar": "Look After Yourself", "domain_representative": False},
    "legal-matters":         {"domain": "Security",     "pillar": "Look After Yourself", "domain_representative": False},

    # Connect with Others
    "body-image":            {"domain": "Expression",   "pillar": "Connect with Others", "domain_representative": True},
    "style":                 {"domain": "Expression",   "pillar": "Connect with Others", "domain_representative": False},
    "personality":           {"domain": "Expression",   "pillar": "Connect with Others", "domain_representative": False},
    "communication":         {"domain": "Expression",   "pillar": "Connect with Others", "domain_representative": False},
    "family-of-origin":      {"domain": "Family",       "pillar": "Connect with Others", "domain_representative": True},
    "extended-family":       {"domain": "Family",       "pillar": "Connect with Others", "domain_representative": False},
    "children":              {"domain": "Family",       "pillar": "Connect with Others", "domain_representative": False},
    "friendship":            {"domain": "Friends and Relationships", "pillar": "Connect with Others", "domain_representative": True},
    "relationship-status":   {"domain": "Friends and Relationships", "pillar": "Connect with Others", "domain_representative": False},
    "relationship-quality": {"domain": "Friends and Relationships", "pillar": "Connect with Others", "domain_representative": False},
    "sex":                   {"domain": "Friends and Relationships", "pillar": "Connect with Others", "domain_representative": False},

    # Organise Your Life
    "housing":               {"domain": "Environment",  "pillar": "Organise Your Life", "domain_representative": True},
    "possessions":           {"domain": "Environment",  "pillar": "Organise Your Life", "domain_representative": False},
    "transportation":        {"domain": "Environment",  "pillar": "Organise Your Life", "domain_representative": False},
    "housework":             {"domain": "Environment",  "pillar": "Organise Your Life", "domain_representative": False},
    "financial-planning-tracking": {"domain": "Finances", "pillar": "Organise Your Life", "domain_representative": True},
    "saving":                {"domain": "Finances",     "pillar": "Organise Your Life", "domain_representative": False},
    "investing":             {"domain": "Finances",     "pillar": "Organise Your Life", "domain_representative": False},
    "organisation":          {"domain": "Productivity", "pillar": "Organise Your Life", "domain_representative": True},
    "systems":               {"domain": "Productivity", "pillar": "Organise Your Life", "domain_representative": False},
    "time-management":       {"domain": "Productivity", "pillar": "Organise Your Life", "domain_representative": False},
    "goals":                 {"domain": "Productivity", "pillar": "Organise Your Life", "domain_representative": False},
    "habits":                {"domain": "Productivity", "pillar": "Organise Your Life", "domain_representative": False},

    # Create & Contribute
    "current-work":          {"domain": "Career",       "pillar": "Create & Contribute", "domain_representative": True},
    "career-planning":       {"domain": "Career",       "pillar": "Create & Contribute", "domain_representative": False},
    "networks":              {"domain": "Career",       "pillar": "Create & Contribute", "domain_representative": False},
    "participatory-leisure": {"domain": "Leisure",      "pillar": "Create & Contribute", "domain_representative": True},
    "consumptive-leisure":   {"domain": "Leisure",      "pillar": "Create & Contribute", "domain_representative": False},
    "global-impact":         {"domain": "Impact",       "pillar": "Create & Contribute", "domain_representative": True},
    "community-contribution":{"domain": "Impact",       "pillar": "Create & Contribute", "domain_representative": False},
}

# Already converted -- skip these
ALREADY_CONVERTED = {"fitness", "friendship", "saving"}


def slug_to_name(slug):
    """Derive a display name from a slug."""
    # Special cases
    special = {
        "sex": "Sex",
        "digital-safety": "Digital Safety",
        "financial-planning-tracking": "Financial Planning and Tracking",
    }
    if slug in special:
        return special[slug]
    return slug.replace("-", " ").title()


def parse_values_from_markdown(content):
    """
    Parse value sections: ### ValueName (XX%) followed by bullets or paragraphs.
    Returns list of {name, weight, description_lines}.
    """
    values = []
    # Find the values section -- look for ### Name (XX%) patterns
    pattern = r'###\s+(.+?)\s*\((\d+)%\)\s*\n(.*?)(?=\n###\s|\n##\s|\n<script|\n\[←|\Z)'
    matches = re.finditer(pattern, content, re.DOTALL)

    for m in matches:
        name = m.group(1).strip()
        weight = int(m.group(2))
        body = m.group(3).strip()

        # Parse bullets
        desc_lines = []
        for line in body.split('\n'):
            line = line.strip()
            if line.startswith('- '):
                desc_lines.append(line[2:].strip())
            elif line and not line.startswith('#') and not line.startswith('['):
                # Paragraph text -- treat as a single bullet
                desc_lines.append(line)

        values.append({
            'name': name,
            'weight': weight,
            'description': desc_lines,
        })

    return values


def derive_value_keys(content, values):
    """
    Derive value keys from showReasoning('levelN-KEY') onclick calls.
    Falls back to deriving from value name if no onclick found.
    """
    # Find all unique keys from showReasoning calls
    key_pattern = r"showReasoning\('level\d+-([^']+)'\)"
    found_keys = list(dict.fromkeys(re.findall(key_pattern, content)))

    if found_keys and len(found_keys) >= len(values):
        # Assign keys to values in order
        for i, v in enumerate(values):
            if i < len(found_keys):
                v['key'] = found_keys[i]
    else:
        # Fallback: derive from name
        for v in values:
            key = v['name'].lower()
            # Clean up: take first word or use simple slug
            key = re.sub(r'[^a-z0-9]+', '-', key).strip('-')
            # Use first meaningful word
            parts = key.split('-')
            v['key'] = parts[0] if parts else 'value'

    return values


def parse_benchmarks_from_markdown(content, values):
    """
    Parse benchmark sections under ### Level N: headings.
    Pattern: **ValueName**: benchmark text <span ...>i</span>
    """
    # Find level sections
    level_pattern = r'###\s+Level\s+(\d+)[:\s].*?\n(.*?)(?=\n###\s+Level\s+\d+|\n##\s|\n<script|\n\[←|\Z)'
    level_matches = re.finditer(level_pattern, content, re.DOTALL)

    benchmarks = {}  # {key: {level_1: text, level_2: text, ...}}

    for lm in level_matches:
        level_num = int(lm.group(1))
        level_body = lm.group(2)

        # Find **ValueName**: text <span...>
        bench_pattern = r'\*\*([^*]+)\*\*:\s*(.*?)(?=\n\n|\n\*\*|\Z)'
        bench_matches = re.finditer(bench_pattern, level_body, re.DOTALL)

        for bm in bench_matches:
            bench_name = bm.group(1).strip()
            bench_text = bm.group(2).strip()

            # Remove the <span> info icon
            bench_text = re.sub(r'\s*<span[^>]*>.*?</span>', '', bench_text).strip()

            # Find matching value by name
            matched_key = None
            for v in values:
                if v['name'] == bench_name:
                    matched_key = v['key']
                    break

            if matched_key is None:
                # Try partial match
                for v in values:
                    if bench_name.lower() in v['name'].lower() or v['name'].lower() in bench_name.lower():
                        matched_key = v['key']
                        break

            if matched_key:
                if matched_key not in benchmarks:
                    benchmarks[matched_key] = {}
                benchmarks[matched_key][f'level_{level_num}'] = bench_text

    return benchmarks


def parse_reasoning_from_script(content, values):
    """
    Parse reasoning entries from the <script> block.
    Only extract level-specific entries (levelN-key pattern).
    General research entries stay in the markdown.
    """
    # Extract the script block
    script_match = re.search(r'<script>\s*(?://.*?\n)*\s*const\s+researchData\s*=\s*\{(.*?)\};\s*</script>', content, re.DOTALL)
    if not script_match:
        return {}

    script_body = script_match.group(1)

    reasoning = {}  # {key: {level_1: text, ...}}

    # Parse entries -- match 'levelN-key': { title: '...', content: '...' }
    # Handle multi-line content with nested quotes
    entry_pattern = r"'(level(\d+)-([^']+))'\s*:\s*\{\s*title\s*:\s*'((?:[^'\\]|\\.)*)'\s*,\s*content\s*:\s*'((?:[^'\\]|\\.)*)'\s*\}"
    for em in re.finditer(entry_pattern, script_body, re.DOTALL):
        full_key = em.group(1)
        level_num = int(em.group(2))
        value_key = em.group(3)
        title = em.group(4).replace("\\'", "'")
        reasoning_text = em.group(5).replace("\\'", "'")

        if value_key not in reasoning:
            reasoning[value_key] = {}
        reasoning[value_key][f'level_{level_num}'] = reasoning_text

    return reasoning


def get_non_level_research_entries(content):
    """
    Extract non-level-specific research entries from the script block.
    These stay in the rewritten markdown.
    """
    script_match = re.search(r'<script>\s*(?://.*?\n)*\s*const\s+researchData\s*=\s*\{(.*?)\};\s*</script>', content, re.DOTALL)
    if not script_match:
        return []

    script_body = script_match.group(1)
    entries = []

    # Find all entries
    entry_pattern = r"(?://[^\n]*\n\s*)?'([^']+)'\s*:\s*\{\s*title\s*:\s*'((?:[^'\\]|\\.)*)'\s*,\s*content\s*:\s*'((?:[^'\\]|\\.)*)'\s*\}"
    for em in re.finditer(entry_pattern, script_body, re.DOTALL):
        key = em.group(1)
        # Skip level-specific entries
        if re.match(r'level\d+-', key):
            continue
        entries.append(em.group(0).strip())

    return entries


def build_yaml_data(slug, values, benchmarks, reasoning):
    """Build the YAML data structure."""
    tax = TAXONOMY[slug]
    data = {
        'slug': slug,
        'name': slug_to_name(slug),
        'domain': tax['domain'],
        'pillar': tax['pillar'],
        'domain_representative': tax['domain_representative'],
        'values': [],
    }

    for v in values:
        value_entry = {
            'key': v['key'],
            'name': v['name'],
            'weight': v['weight'],
            'description': v['description'],
        }

        # Add benchmarks if they exist
        vkey = v['key']
        if vkey in benchmarks or vkey in reasoning:
            value_entry['benchmarks'] = {}
            for level_num in range(1, 6):
                level_key = f'level_{level_num}'
                bench_text = benchmarks.get(vkey, {}).get(level_key)
                reason_text = reasoning.get(vkey, {}).get(level_key)

                if bench_text or reason_text:
                    level_data = {}
                    if bench_text:
                        level_data['text'] = bench_text
                    if reason_text:
                        level_data['reasoning'] = reason_text
                    value_entry['benchmarks'][level_key] = level_data

        data['values'].append(value_entry)

    return data


def write_yaml(slug, data):
    """Write YAML file for a life area."""
    path = os.path.join(ROOT, '_data', 'life_areas', f'{slug}.yml')

    # Custom representer to handle multiline strings
    class MyDumper(yaml.Dumper):
        pass

    def str_representer(dumper, data):
        if '\n' in data or len(data) > 120:
            return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
        if "'" in data and '"' not in data:
            return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')
        return dumper.represent_scalar('tag:yaml.org,2002:str', data)

    MyDumper.add_representer(str, str_representer)

    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, Dumper=MyDumper, default_flow_style=False,
                  allow_unicode=True, sort_keys=False, width=200)

    print(f"  Wrote {path}")


def rewrite_markdown(slug, content, has_benchmarks, non_level_entries):
    """
    Rewrite the index.md to use includes.
    """
    lines = content.split('\n')

    # Check for existing frontmatter
    has_frontmatter = lines[0].strip() == '---'

    # Find sections to replace
    # 1. Values section: from first ### Name (XX%) to next ## heading
    # 2. Benchmarks section: from ### Level 1: to next ## heading or <script>
    # 3. Script block: replace reasoning entries with include

    # Strategy: rebuild the file by finding and replacing sections

    new_content = content

    # Step 1: Replace values section with include
    # Find the range of ### Value (XX%) entries
    values_pattern = r'(###\s+.+?\s*\(\d+%\)\s*\n(?:.*?\n)*?)(?=\n##\s|\n<script|\n\[←|\Z)'
    values_match = re.search(values_pattern, new_content, re.DOTALL)
    if values_match:
        # Find the start of the first value heading
        first_value = re.search(r'###\s+.+?\s*\(\d+%\)', new_content)
        if first_value:
            # Find the end of all value sections (before next ## or other section)
            # Look from the first value heading onwards
            after_values = new_content[first_value.start():]
            # Find where values end -- next ## heading that's NOT a value
            end_match = re.search(r'\n(?=##\s(?!#))', after_values)
            if end_match:
                values_end = first_value.start() + end_match.start()
            else:
                # Values go to end
                end_match = re.search(r'\n(?=\[←|\Z)', after_values)
                values_end = first_value.start() + (end_match.start() if end_match else len(after_values))

            values_section = new_content[first_value.start():values_end]
            new_content = new_content[:first_value.start()] + '{% include life-area-values.html %}\n' + new_content[values_end:]

    # Step 2: Replace benchmarks section with include (if present)
    if has_benchmarks:
        # Find ### Level 1: section through ### Level 5:
        bench_start = re.search(r'###\s+Level\s+1[:\s]', new_content)
        if bench_start:
            # Find end of benchmark sections
            after_bench = new_content[bench_start.start():]
            # End at ## Levels or <script> or [←
            end_match = re.search(r'\n(?=##\s(?!#)|<script|\[←)', after_bench)
            if end_match:
                bench_end = bench_start.start() + end_match.start()
            else:
                bench_end = len(new_content)

            new_content = new_content[:bench_start.start()] + '{% include life-area-benchmarks.html %}\n' + new_content[bench_end:]

    # Step 3: Rewrite script block
    if has_benchmarks:
        script_match = re.search(
            r'<script>\s*(?://.*?\n)*\s*const\s+researchData\s*=\s*\{.*?\};\s*\n\s*</script>\s*\n?\s*(?:\{%\s*include\s+popup-boilerplate\.html\s*%\})?',
            new_content, re.DOTALL
        )
        if script_match:
            # Build new script block
            new_script = '<script>\n// Research data for info buttons\nconst researchData = {\n'

            if non_level_entries:
                for entry in non_level_entries:
                    new_script += f'    {entry},\n'

            new_script += '    {% include benchmark-reasoning.html %}\n'
            new_script += '};\n\n</script>\n\n{% include popup-boilerplate.html %}'

            new_content = new_content[:script_match.start()] + new_script + new_content[script_match.end():]
    elif re.search(r'<script>', new_content):
        # Page has a script block but no benchmarks -- keep as-is
        # (some pages have research popups in the prose)
        pass

    # Step 4: Handle frontmatter
    if has_frontmatter:
        # Add life_area_slug to existing frontmatter
        fm_end = new_content.index('---', 3)
        fm_content = new_content[3:fm_end].strip()
        if 'life_area_slug' not in fm_content:
            new_content = f'---\n{fm_content}\nlife_area_slug: {slug}\n---' + new_content[fm_end + 3:]
    else:
        # Add new frontmatter
        new_content = f'---\nlife_area_slug: {slug}\n---\n{new_content}'

    return new_content


def has_page_benchmarks(content):
    """Check if the page has benchmark sections (### Level N:)."""
    return bool(re.search(r'###\s+Level\s+\d+[:\s]', content))


def has_page_script(content):
    """Check if the page has a researchData script block."""
    return bool(re.search(r'const\s+researchData\s*=', content))


def process_page(slug):
    """Process a single life area page."""
    index_path = os.path.join(ROOT, slug, 'index.md')

    if not os.path.exists(index_path):
        print(f"  SKIP: {index_path} not found")
        return False

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already converted
    if '{% include life-area-values.html %}' in content:
        print(f"  SKIP: already converted")
        return False

    # Parse values
    values = parse_values_from_markdown(content)
    if not values:
        print(f"  ERROR: no values found")
        return False

    # Derive keys from showReasoning calls
    values = derive_value_keys(content, values)

    print(f"  Found {len(values)} values: {[v['key'] for v in values]}")

    # Parse benchmarks
    page_has_benchmarks = has_page_benchmarks(content)
    benchmarks = {}
    reasoning = {}
    non_level_entries = []

    if page_has_benchmarks:
        benchmarks = parse_benchmarks_from_markdown(content, values)
        reasoning = parse_reasoning_from_script(content, values)
        non_level_entries = get_non_level_research_entries(content)
        bench_count = sum(len(v) for v in benchmarks.values())
        reason_count = sum(len(v) for v in reasoning.values())
        print(f"  Found {bench_count} benchmarks, {reason_count} reasoning entries, {len(non_level_entries)} non-level entries")
    elif has_page_script(content):
        # Has script but no level-based benchmarks -- treat as having non-level entries only
        non_level_entries = get_non_level_research_entries(content)
        print(f"  Values only (no benchmarks), {len(non_level_entries)} non-level research entries")
    else:
        print(f"  Values only (no benchmarks, no script)")

    # Build YAML
    yaml_data = build_yaml_data(slug, values, benchmarks, reasoning)

    # Write YAML
    write_yaml(slug, yaml_data)

    # Rewrite markdown
    new_content = rewrite_markdown(slug, content, page_has_benchmarks, non_level_entries)

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  Rewrote {index_path}")
    return True


def main():
    print("Phase B: Extracting life area data to YAML\n")

    # Ensure _data/life_areas exists
    data_dir = os.path.join(ROOT, '_data', 'life_areas')
    os.makedirs(data_dir, exist_ok=True)

    success = 0
    errors = 0
    skipped = 0

    for slug in sorted(TAXONOMY.keys()):
        if slug in ALREADY_CONVERTED:
            print(f"[{slug}] Already converted, skipping")
            skipped += 1
            continue

        print(f"[{slug}]")
        try:
            if process_page(slug):
                success += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback
            traceback.print_exc()
            errors += 1

    print(f"\nDone: {success} converted, {skipped} skipped, {errors} errors")


if __name__ == '__main__':
    main()
