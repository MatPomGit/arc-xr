# ARC-ADHD safety, pause, overload and caregiver interaction rules

Status: Phase 0 candidate rules, version 0.1. The behavioral rules are implementation requirements; any numerical limits remain subject to study freeze.

## 1. Purpose

This document defines how the core application responds to:

- explicit child pause;
- explicit child stop;
- sensory overload;
- caregiver safety intervention;
- researcher/operator intervention;
- technical states that make continued measurement unsafe or uninterpretable.

The central principle is that safety and child agency have priority over task progression, adaptation and challenge delivery.

## 2. Priority order

When multiple conditions are true, the application shall apply this order:

1. fatal integrity condition;
2. safety stop;
3. explicit child stop;
4. caregiver/researcher safety stop;
5. explicit child pause;
6. sensory-overload simplification;
7. technical interruption;
8. scientific state transition;
9. ordinary game progression.

A lower-priority action cannot cancel a higher-priority one.

## 3. Child stop

### Requirement

A stop control must be available throughout the participant-facing session.

The application shall treat an explicit stop as authoritative.

### On child stop

The application shall:

- stop challenge presentation;
- stop optional haptic/audio patterns;
- stop task progression;
- preserve already durably written telemetry;
- record the stop source as child;
- close an open recovery event according to the protocol;
- transition to SAFE_STOP;
- not ask the child to complete one more trial;
- not require an explanation before stopping.

### Reward behavior

Stopping shall not:

- remove previously earned progress;
- display failure language;
- reduce a streak;
- trigger social comparison;
- lock future participation.

## 4. Child pause

### Requirement

Pause is distinct from stop.

A pause shall:

- suspend new challenge events;
- suspend ordinary progression where scientifically safe;
- preserve current task context;
- stop nonessential sensory presentation;
- expose resume and stop choices;
- record pause onset and end;
- set the recent-pause guard used by challenge eligibility.

### Resume

On resume:

- the application restores the explicit stored resume target;
- it does not infer the target only from the visible UI;
- a new challenge remains suppressed until the configured post-pause eligibility conditions are met;
- if the pause invalidated recovery measurement, the event becomes RECOVERY_DATA_INVALID rather than censored.

## 5. Sensory overload

### Sources

The core application may recognize overload from:

- explicit child report;
- caregiver/researcher safety input when protocol permits;
- a predefined protocol safety condition.

The core shall not classify overload from facial behavior, inferred emotion or an opaque model.

### First response

When overload does not require immediate stop, the application shall simplify sensory presentation before reducing cognitive demand.

Candidate simplification order:

1. remove decorative audio;
2. reduce decorative animation;
3. disable optional haptic cues;
4. replace optional spoken/functional audio with visual fallback when possible;
5. enter a quiet pause state when simplification is insufficient.

This order can be versioned by study configuration.

### Cognitive difficulty

Low performance during high sensory load must not immediately trigger cognitive difficulty reduction.

The controller should first:

1. simplify sensory load;
2. collect a new configured observation window;
3. reassess performance;
4. reduce cognitive demand only if the applicable controller rule still supports it.

## 6. Safety stop

A safety stop may be triggered by:

- explicit child stop;
- caregiver safety stop;
- researcher safety stop;
- protocol-defined distress condition;
- application integrity failure affecting safe continuation;
- device failure affecting safe interaction.

Safety stop always suppresses further challenge events.

## 7. Caregiver role

The caregiver is a safety/logistics support person, not an uncontrolled co-therapist inside the task.

### Allowed caregiver actions

Where the protocol permits:

- help position/hold the research device before the task;
- read logistical instructions when the child needs help;
- activate safety stop;
- alert the researcher/operator to a problem;
- assist with accessibility needs defined in the protocol.

### Not allowed during active task unless explicitly protocolized

- tell the child which response is correct;
- coach the child to improve task score;
- choose a regulation strategy for the child;
- reveal upcoming challenge events;
- change cognitive difficulty;
- change hidden study configuration;
- interpret telemetry or recovery score to the child.

Any protocol-approved caregiver assistance that can affect task performance should be logged.

## 8. Researcher/operator role

The researcher/operator may:

- verify study configuration before session;
- resolve device setup problems;
- invoke safety stop;
- classify documented protocol deviations;
- inspect protected technical diagnostics.

The researcher/operator should not manually tune difficulty during a locked session unless the protocol explicitly contains such an override.

Any manual scientific-state override must be logged with a reason code.

## 9. Error burst and repeated failure

Repeated task errors alone are not automatically a safety event.

The application may use a configured error-burst rule to:

- suppress challenge scheduling;
- simplify sensory presentation;
- hold or reduce cognitive difficulty;
- offer a neutral pause.

The child must not receive punitive language.

A safety stop requires the separate safety rule, not simply a poor score.

## 10. Challenge after pause or overload

After a child pause or overload event, a new challenge must not be scheduled immediately.

The candidate Phase 0 rule requires:

- return to BASELINE_TASK;
- safety and overload clear;
- telemetry healthy;
- a new valid reference window;
- recent-pause guard cleared according to configuration;
- all ordinary eligibility conditions satisfied.

## 11. Recovery-event handling

### Pause during recovery

If pause preserves valid measurement according to the study rule, recovery monitoring can resume only through explicit state-machine logic.

If the pause makes the recovery interval uninterpretable, close as RECOVERY_DATA_INVALID.

Do not convert such events into right-censored outcomes merely because a valid recovery was not observed.

### Stop during recovery

A child/safety stop closes participant-facing activity.

The research event must record the specific stop/censor/invalidity semantics defined in the protocol. The application shall not fabricate a recovery time.

## 12. Accessibility

Safety controls must be:

- large enough for reliable touch;
- visually distinct but not alarming;
- available without sound;
- available when haptics are disabled;
- understandable with low reading burden.

A motor-accessible alternative to gestures should be available for core stop/pause behavior.

## 13. Notifications and feedback

The application shall not use:

- guilt-based wording;
- countdown threats;
- "you will lose progress" warnings;
- caregiver-facing alarm language for ordinary task errors;
- hidden escalating stimulation to regain attention.

Safety prompts should be neutral and actionable.

## 14. Session-level safety telemetry

Record at minimum:

- pause count;
- pause source;
- stop source;
- overload flag/source;
- sensory simplification actions;
- safety override activation;
- caregiver/researcher manual intervention;
- early termination reason;
- protocol deviation if applicable.

## 15. Phase 0 review variables

Phase 0 should specifically inspect:

- how often children use pause;
- whether stop remains understandable;
- whether reduced-stimulation mode is sufficient;
- whether caregiver intervention contaminates task behavior;
- whether challenge eligibility correctly suppresses post-pause events;
- whether any safety rule unexpectedly prevents normal session completion.

## 16. Machine-readable configuration

The candidate configuration is stored in:

`config/interaction_safety.phase0.example.json`.

It contains behavioral switches and ordering rules. Numerical thresholds should not be added as frozen values until justified by the Phase 0 design process.
