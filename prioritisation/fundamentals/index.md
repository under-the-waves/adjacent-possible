---
layout: default
title: Fundamentals Screen
permalink: /prioritisation/fundamentals/
---

<style>
body .main-content {
    max-width: none !important;
    padding: 1rem !important;
}

.triage-container {
    max-width: 760px;
    margin: 0 auto;
    padding: 20px;
    font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
    color: #333;
}

.triage-header h1 {
    font-weight: normal;
    color: #000;
    margin-bottom: 8px;
}
.triage-header p.lede {
    color: #555;
    margin-bottom: 24px;
}

.btn-primary {
    background: #155799;
    color: #fff;
    border: none;
    border-radius: 6px;
    padding: 12px 22px;
    font-size: 1em;
    cursor: pointer;
    font-weight: 600;
}
.btn-primary:hover { background: #0f4373; }
.btn-primary:disabled { background: #bdbdbd; cursor: not-allowed; }

.btn-secondary {
    background: #fff;
    color: #155799;
    border: 1px solid #155799;
    border-radius: 6px;
    padding: 10px 18px;
    font-size: 0.9em;
    cursor: pointer;
    font-weight: 600;
    text-decoration: none;
    display: inline-block;
}
.btn-secondary:hover { background: #f0f6fc; }

.btn-link {
    background: none;
    border: none;
    color: #155799;
    cursor: pointer;
    text-decoration: underline;
    padding: 4px 8px;
    font-size: 0.9em;
}

.prior-banner {
    background: #f5f5f5;
    border-left: 4px solid #888;
    border-radius: 4px;
    padding: 12px 16px;
    margin-bottom: 24px;
    font-size: 0.9em;
}
.prior-banner .actions { margin-top: 8px; }

.start-row { margin-top: 24px; }
.start-row .meta {
    color: #888;
    font-size: 0.85em;
    margin-top: 10px;
}

/* Survey */
.progress-bar-container { margin-bottom: 24px; }
.progress-bar-outer {
    height: 8px;
    background: #e0e0e0;
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 6px;
}
.progress-bar-fill {
    height: 100%;
    background: #155799;
    border-radius: 4px;
    transition: width 0.3s ease;
}
.progress-info {
    display: flex;
    justify-content: space-between;
    font-size: 0.8em;
    color: #666;
}

.question-card {
    background: #fff;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.q-section {
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-size: 0.75em;
    color: #888;
    font-weight: 600;
    margin-bottom: 8px;
}
.q-text {
    font-size: 1.05em;
    color: #222;
    margin-bottom: 18px;
    line-height: 1.4;
}
.q-options { display: flex; flex-direction: column; gap: 6px; }
.radio-option {
    display: flex;
    align-items: center;
    padding: 11px 14px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.12s;
    font-size: 0.95em;
    background: #fff;
}
.radio-option:hover { border-color: #155799; background: #f7fbff; }
.radio-option input[type="radio"] {
    margin-right: 10px;
    accent-color: #155799;
}
.radio-option.selected { border-color: #155799; background: #e3f2fd; }

.nav-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 8px;
}

.hidden { display: none; }

@media (max-width: 600px) {
    .triage-container { padding: 12px; }
    .question-card { padding: 18px; }
}
</style>

<div class="triage-container">

  <!-- Landing view -->
  <div id="viewLanding">
    <div class="triage-header">
      <h1>Fundamentals screen</h1>
      <p class="lede">Personalises the fundamentals layer of your results. About five minutes, fourteen short questions covering sleep, wellbeing, foundational finances, social connection, and physical activity.</p>
    </div>

    <div id="priorBanner" class="prior-banner hidden">
      <div id="priorBannerText"></div>
      <div class="actions">
        <a href="{{ site.baseurl }}/prioritisation/triage/#results" class="btn-secondary">View your results</a>
        <button class="btn-link" onclick="startSurvey()">Retake</button>
      </div>
    </div>

    <p>The screen uses validated short forms (the WHO-5 Wellbeing Index for wellbeing, the UCLA-3 short scale for loneliness) plus single behavioural items for sleep, debt, contact frequency, activity, and diet. The cutoffs and underlying evidence are documented in the <a href="{{ site.baseurl }}/methodology/fundamentals-cutoffs/">fundamentals cutoffs reference</a>.</p>

    <p>This screen is meaningful on its own, but works best after the <a href="{{ site.baseurl }}/prioritisation/triage/">triage screen</a> – which is shorter and covers acute issues that warrant attention before optimisation. Most users will want to take both.</p>

    <p>Your responses stay on this device unless you sign in, in which case they sync across devices via your account. They are not shared.</p>

    <div class="start-row">
      <button class="btn-primary" onclick="startSurvey()">Start the screen</button>
      <div class="meta">14 questions, about five minutes.</div>
    </div>
  </div>

  <!-- Survey view -->
  <div id="viewSurvey" class="hidden">
    <div class="progress-bar-container">
      <div class="progress-bar-outer"><div class="progress-bar-fill" id="progressFill"></div></div>
      <div class="progress-info">
        <span id="progressText">Question 1 of 14</span>
        <button class="btn-link" onclick="exitSurvey()" style="padding:0;">Exit</button>
      </div>
    </div>
    <div id="questionMount"></div>
    <div class="nav-row">
      <button class="btn-secondary" id="backBtn" onclick="goBack()">Back</button>
      <button class="btn-primary" id="nextBtn" onclick="goNext()" disabled>Next</button>
    </div>
  </div>

</div>

<script>
// ────────────────────────────────────────────────────────────────────────────
// Scales
// ────────────────────────────────────────────────────────────────────────────

var SCALE_WHO5 = [
    { label: 'At no time', value: 0 },
    { label: 'Some of the time', value: 1 },
    { label: 'Less than half of the time', value: 2 },
    { label: 'More than half of the time', value: 3 },
    { label: 'Most of the time', value: 4 },
    { label: 'All of the time', value: 5 }
];

var SCALE_UCLA3 = [
    { label: 'Hardly ever', value: 1 },
    { label: 'Some of the time', value: 2 },
    { label: 'Often', value: 3 }
];

var SCALE_YN = [
    { label: 'Yes', value: 'yes' },
    { label: 'No', value: 'no' }
];

var SCALE_SLEEP = [
    { label: 'Under 5 hours', value: 'under5' },
    { label: '5 to 6 hours', value: '5-6' },
    { label: '6 to 7 hours', value: '6-7' },
    { label: '7 to 8 hours', value: '7-8' },
    { label: '8 hours or more', value: '8plus' }
];

var SCALE_CONTACT = [
    { label: 'Daily', value: 'daily' },
    { label: 'Weekly', value: 'weekly' },
    { label: 'Monthly', value: 'monthly' },
    { label: 'Less than monthly', value: 'less' }
];

var SCALE_ACTIVITY = [
    { label: 'None', value: '0' },
    { label: 'Under 60 minutes', value: 'under60' },
    { label: '60 to 150 minutes', value: '60-150' },
    { label: '150 to 300 minutes', value: '150-300' },
    { label: 'Over 300 minutes', value: 'over300' }
];

var SCALE_VEG = [
    { label: '0 to 1 servings', value: '0-1' },
    { label: '2 servings', value: '2' },
    { label: '3 to 4 servings', value: '3-4' },
    { label: '5 or more servings', value: '5plus' }
];

// ────────────────────────────────────────────────────────────────────────────
// Questions
// ────────────────────────────────────────────────────────────────────────────

var WHO5_LEAD = 'Over the last two weeks, ';
var QUESTIONS = [
    { id: 'who5_1', section: 'Wellbeing',  text: WHO5_LEAD + 'I have felt cheerful and in good spirits.',                       options: SCALE_WHO5 },
    { id: 'who5_2', section: 'Wellbeing',  text: WHO5_LEAD + 'I have felt calm and relaxed.',                                   options: SCALE_WHO5 },
    { id: 'who5_3', section: 'Wellbeing',  text: WHO5_LEAD + 'I have felt active and vigorous.',                                options: SCALE_WHO5 },
    { id: 'who5_4', section: 'Wellbeing',  text: WHO5_LEAD + 'I woke up feeling fresh and rested.',                             options: SCALE_WHO5 },
    { id: 'who5_5', section: 'Wellbeing',  text: WHO5_LEAD + 'My daily life has been filled with things that interest me.',    options: SCALE_WHO5 },
    { id: 'sleep_hours',        section: 'Sleep',     text: 'On a typical work night, roughly how many hours of sleep do you get?', options: SCALE_SLEEP },
    { id: 'emergency',          section: 'Finances',  text: 'If you had an unexpected $400 expense, could you cover it from cash or savings without borrowing?', options: SCALE_YN },
    { id: 'high_interest_debt', section: 'Finances',  text: 'Are you currently carrying balances on credit cards, payday loans, or overdrafts that charge interest?', options: SCALE_YN },
    { id: 'ucla_1', section: 'Social connection', text: 'How often do you feel that you lack companionship?', options: SCALE_UCLA3 },
    { id: 'ucla_2', section: 'Social connection', text: 'How often do you feel left out?',                    options: SCALE_UCLA3 },
    { id: 'ucla_3', section: 'Social connection', text: 'How often do you feel isolated from others?',        options: SCALE_UCLA3 },
    { id: 'contact_freq', section: 'Social connection', text: 'How often do you have meaningful contact with close friends or family (in person, by phone, or video)?', options: SCALE_CONTACT },
    { id: 'activity_min', section: 'Activity', text: 'In a typical week, roughly how many minutes of activity that raises your heart rate noticeably do you do? (Brisk walking, cycling, sport, gym, manual work all count.)', options: SCALE_ACTIVITY },
    { id: 'veg_servings', section: 'Nutrition', text: 'On a typical day, how many servings of vegetables or fruit do you eat? (One serving is roughly a fist-sized portion.)', options: SCALE_VEG }
];

// ────────────────────────────────────────────────────────────────────────────
// Storage and state
// ────────────────────────────────────────────────────────────────────────────

var STORAGE_RESPONSES = 'ap-fundamentals-responses';
var STORAGE_FLAGS     = 'ap-fundamentals-flags';
var STORAGE_DONE_AT   = 'ap-fundamentals-completed-at';

var answers = {};
var index = 0;

function saveAnswers() { window.APStorage.save(STORAGE_RESPONSES, answers); }
function loadAnswers() { return window.APStorage.load(STORAGE_RESPONSES) || {}; }
function saveFlags(f)  { window.APStorage.save(STORAGE_FLAGS, f); }
function saveDoneAt()  { window.APStorage.save(STORAGE_DONE_AT, new Date().toISOString()); }
function loadDoneAt()  { return window.APStorage.load(STORAGE_DONE_AT); }

// ────────────────────────────────────────────────────────────────────────────
// Flag computation
// ────────────────────────────────────────────────────────────────────────────

function computeFlags(a) {
    var flags = {};

    // Sleep
    if (a.sleep_hours === 'under5' || a.sleep_hours === '5-6') flags.sleep = true;

    // Wellbeing (WHO-5 sum ≤ 13 raw)
    var who5Sum = ['who5_1','who5_2','who5_3','who5_4','who5_5']
        .reduce(function(s, k) { return s + (typeof a[k] === 'number' ? a[k] : 0); }, 0);
    if (who5Sum <= 13) flags.wellbeing = true;

    // Foundational finances
    if (a.emergency === 'no' || a.high_interest_debt === 'yes') flags.finances = true;

    // Social
    var uclaSum = ['ucla_1','ucla_2','ucla_3']
        .reduce(function(s, k) { return s + (typeof a[k] === 'number' ? a[k] : 0); }, 0);
    if (uclaSum >= 6 || a.contact_freq === 'monthly' || a.contact_freq === 'less') flags.social = true;

    // Activity and nutrition
    if (a.activity_min === '0' || a.activity_min === 'under60' ||
        a.veg_servings === '0-1' || a.veg_servings === '2') flags.activity = true;

    return flags;
}

// ────────────────────────────────────────────────────────────────────────────
// View switching
// ────────────────────────────────────────────────────────────────────────────

function showView(name) {
    ['Landing', 'Survey'].forEach(function(v) {
        document.getElementById('view' + v).classList.toggle('hidden', v !== name);
    });
    window.scrollTo(0, 0);
}

// ────────────────────────────────────────────────────────────────────────────
// Landing
// ────────────────────────────────────────────────────────────────────────────

function renderLanding() {
    var doneAt = loadDoneAt();
    var banner = document.getElementById('priorBanner');
    if (doneAt) {
        var dateStr;
        try {
            dateStr = new Intl.DateTimeFormat('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }).format(new Date(doneAt));
        } catch (e) { dateStr = doneAt.split('T')[0]; }
        document.getElementById('priorBannerText').textContent = 'You took this screen on ' + dateStr + '.';
        banner.classList.remove('hidden');
    } else {
        banner.classList.add('hidden');
    }
    showView('Landing');
}

// ────────────────────────────────────────────────────────────────────────────
// Survey
// ────────────────────────────────────────────────────────────────────────────

function startSurvey() {
    answers = {};
    index = 0;
    renderQuestion();
    showView('Survey');
}

function renderQuestion() {
    if (index >= QUESTIONS.length) {
        finishSurvey();
        return;
    }
    var q = QUESTIONS[index];
    var total = QUESTIONS.length;
    document.getElementById('progressText').textContent = 'Question ' + (index + 1) + ' of ' + total;
    document.getElementById('progressFill').style.width = (index / total * 100) + '%';

    var html = '<div class="question-card">';
    html += '<div class="q-section">' + escapeHtml(q.section) + '</div>';
    html += '<div class="q-text">' + escapeHtml(q.text) + '</div>';
    html += '<div class="q-options">';
    var current = answers[q.id];
    q.options.forEach(function(opt, i) {
        var checked = (current !== undefined && current === opt.value) ? 'checked' : '';
        var sel     = (current !== undefined && current === opt.value) ? ' selected' : '';
        var optId   = 'opt_' + q.id + '_' + i;
        html += '<label class="radio-option' + sel + '" for="' + optId + '">';
        html += '<input type="radio" name="opt_' + q.id + '" id="' + optId + '" value="' + i + '" ' + checked + ' onchange="onAnswer(\'' + q.id + '\', ' + i + ')">';
        html += '<span>' + escapeHtml(opt.label) + '</span>';
        html += '</label>';
    });
    html += '</div></div>';
    document.getElementById('questionMount').innerHTML = html;

    document.getElementById('backBtn').disabled = (index === 0);
    document.getElementById('nextBtn').disabled = (current === undefined);
    document.getElementById('nextBtn').textContent = (index === QUESTIONS.length - 1) ? 'Finish' : 'Next';
}

function onAnswer(qid, optIndex) {
    var q = QUESTIONS.find(function(x) { return x.id === qid; });
    if (!q) return;
    answers[qid] = q.options[optIndex].value;
    saveAnswers();
    var labels = document.querySelectorAll('label.radio-option');
    labels.forEach(function(l) { l.classList.remove('selected'); });
    var picked = document.getElementById('opt_' + qid + '_' + optIndex);
    if (picked && picked.parentNode) picked.parentNode.classList.add('selected');
    document.getElementById('nextBtn').disabled = false;
}

function goNext() { index += 1; renderQuestion(); }
function goBack() { if (index > 0) { index -= 1; renderQuestion(); } }

function exitSurvey() {
    saveAnswers();
    renderLanding();
}

function finishSurvey() {
    var flags = computeFlags(answers);
    saveFlags(flags);
    saveDoneAt();
    window.location.href = '{{ site.baseurl }}/prioritisation/triage/#results';
}

// ────────────────────────────────────────────────────────────────────────────
// Utilities
// ────────────────────────────────────────────────────────────────────────────

function escapeHtml(s) {
    if (s === undefined || s === null) return '';
    return String(s)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}

window.addEventListener('ap-storage-sync', function() {
    if (!document.getElementById('viewLanding').classList.contains('hidden')) {
        renderLanding();
    }
});

document.addEventListener('DOMContentLoaded', function() {
    answers = loadAnswers();
    renderLanding();
});
</script>
