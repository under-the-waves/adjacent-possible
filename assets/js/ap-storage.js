// AP Storage – localStorage-first persistence with optional Clerk sync
(function() {
    'use strict';

    var CLERK_META_KEY = 'ap';
    var DEBOUNCE_MS = 2000;
    var debounceTimer = null;
    var clerkReady = false;

    // localStorage key -> unsafeMetadata field name
    var KEY_MAP = {
        'ap-dashboard-levels': 'levels',
        'ap-survey-tier': 'tier',
        'ap-survey-responses': 'responses',
        'ap-survey-weights': 'weights',
        'ap-slider-weights': 'sliderWeights',
        'ap-level1-progress': 'level1Progress',
        'ap-level1-assess': 'level1Assess'
    };

    function load(key) {
        try {
            var raw = localStorage.getItem(key);
            if (raw === null) return null;
            return JSON.parse(raw);
        } catch (e) {
            return null;
        }
    }

    function save(key, value) {
        localStorage.setItem(key, JSON.stringify(value));
        localStorage.setItem('ap-last-modified', new Date().toISOString());
        scheduleSyncToClerk();
    }

    function isSignedIn() {
        return clerkReady && window.Clerk && window.Clerk.user;
    }

    // Build the full ap object from localStorage
    function buildPayload() {
        var payload = { version: 1, lastModified: localStorage.getItem('ap-last-modified') || new Date().toISOString() };
        Object.keys(KEY_MAP).forEach(function(lsKey) {
            var field = KEY_MAP[lsKey];
            var val = load(lsKey);
            if (val !== null) payload[field] = val;
        });
        return payload;
    }

    // Write remote ap object into localStorage
    function applyPayload(payload) {
        Object.keys(KEY_MAP).forEach(function(lsKey) {
            var field = KEY_MAP[lsKey];
            if (payload[field] !== undefined) {
                localStorage.setItem(lsKey, JSON.stringify(payload[field]));
            }
        });
        if (payload.lastModified) {
            localStorage.setItem('ap-last-modified', payload.lastModified);
        }
    }

    function syncToClerk() {
        if (!isSignedIn()) return Promise.resolve();
        var payload = buildPayload();
        var meta = Object.assign({}, window.Clerk.user.unsafeMetadata);
        meta[CLERK_META_KEY] = payload;
        return window.Clerk.user.update({ unsafeMetadata: meta }).catch(function(err) {
            console.warn('APStorage: Clerk sync failed', err);
        });
    }

    function scheduleSyncToClerk() {
        if (!isSignedIn()) return;
        if (debounceTimer) clearTimeout(debounceTimer);
        debounceTimer = setTimeout(function() {
            debounceTimer = null;
            syncToClerk();
        }, DEBOUNCE_MS);
    }

    function syncFromClerk() {
        if (!isSignedIn()) return;
        var remote = window.Clerk.user.unsafeMetadata[CLERK_META_KEY];
        if (!remote || !remote.lastModified) return;

        var localTs = localStorage.getItem('ap-last-modified');
        // If remote is newer (or no local timestamp), pull remote data
        if (!localTs || new Date(remote.lastModified) > new Date(localTs)) {
            applyPayload(remote);
            // Dispatch event so open pages can react
            window.dispatchEvent(new CustomEvent('ap-storage-sync'));
        }
    }

    // Called when Clerk finishes loading
    function onClerkReady() {
        clerkReady = true;
        if (window.Clerk && window.Clerk.user) {
            syncFromClerk();
        }
        // Listen for sign-in events
        if (window.Clerk) {
            window.Clerk.addListener(function(evt) {
                if (window.Clerk.user) {
                    syncFromClerk();
                }
            });
        }
    }

    // Flush pending writes before page unload
    window.addEventListener('beforeunload', function() {
        if (debounceTimer && isSignedIn()) {
            clearTimeout(debounceTimer);
            debounceTimer = null;
            // Use sendBeacon-style sync (best-effort)
            var payload = buildPayload();
            var meta = Object.assign({}, window.Clerk.user.unsafeMetadata);
            meta[CLERK_META_KEY] = payload;
            try {
                window.Clerk.user.update({ unsafeMetadata: meta });
            } catch (e) { /* best effort */ }
        }
    });

    window.APStorage = {
        load: load,
        save: save,
        isSignedIn: isSignedIn,
        syncFromClerk: syncFromClerk,
        syncToClerk: syncToClerk,
        _onClerkReady: onClerkReady
    };
})();
