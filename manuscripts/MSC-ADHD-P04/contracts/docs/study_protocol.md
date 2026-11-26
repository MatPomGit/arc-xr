# Study protocol

## 1. Research program

The project should be evaluated in stages. A definitive efficacy claim should not be based on the first playable prototype.

## Phase 0: co-design and construct validation

Participants:

- children with ADHD in the target age range;
- caregivers;
- child psychologists, psychiatrists or therapists;
- HCI/game-design researchers.

Goals:

- verify that mechanics correspond to intended constructs;
- identify confusing or aversive elements;
- establish child-appropriate language;
- establish practical session length;
- test whether challenge events create tolerable rather than excessive frustration;
- test sensory tolerability of sound, haptics and AR;
- establish safe indoor AR play-zone requirements;
- evaluate comprehension of body-awareness prompts.

Outputs:

- frozen construct-to-mechanic map;
- usability requirements;
- sensory-accessibility requirements;
- AR safety thresholds;
- initial telemetry schema.

## Phase 1: feasibility study

Suggested sample: n = 20-30.

Duration: 4-8 weeks.

Primary feasibility outcomes:

- recruitment;
- retention;
- proportion of prescribed sessions completed;
- median session duration;
- frequency of pauses and premature exits;
- sensory-overload events;
- AR-related interruptions or safety stops;
- adverse events;
- child and caregiver acceptability.

No clinical efficacy claim should be based on this phase.

## Phase 2: pilot randomized controlled trial

Recommended design:

- parallel-group randomized trial;
- ARC-ADHD versus active-control game;
- treatment as usual maintained in both groups;
- assessors blinded where feasible;
- baseline, post-intervention and follow-up assessment;
- preregistered primary outcome and analysis.

A simple active control should match:

- device use;
- session frequency;
- visual quality;
- researcher contact;
- general game reward density;
- approximate audio exposure;
- approximate movement opportunity where feasible;

but should not contain the hypothesized regulation-and-recovery mechanisms.

A wait-list alone is insufficient to separate intervention effects from expectancy, attention and game engagement.

## 2. Embedded mechanistic experiments

The principal clinical comparison should remain simple. Sensory components can be evaluated through embedded within-person experiments.

### 2.1 Micro-randomized sensory-cue trial

At eligible task events, randomly assign:

A. visual-only cue;
B. audiovisual cue;
C. audiovisual plus haptic cue.

Primary proximal endpoint:

- correct inhibition or correct strategy initiation.

Secondary endpoints:

- response latency;
- missed cues;
- post-cue recovery;
- reported sensory overload;
- pause/exit probability.

This design helps estimate whether a modality contributes beyond the underlying task.

### 2.2 Matched AR versus stationary blocks

Within the intervention arm, use matched cognitive tasks in:

- stationary phone mode;
- indoor AR movement mode.

Prespecified comparisons:

- executive performance;
- adherence;
- movement amount;
- recovery latency;
- perceived effort;
- enjoyment;
- adverse effects.

AR superiority should not be assumed. Non-inferior cognitive performance combined with more physical engagement would already be informative.

### 2.3 Sensorimotor rhythm substudy

Within-person conditions:

A. haptic rhythm;
B. auditory rhythm;
C. synchronized audio+haptic rhythm.

Tasks can require controlled device rotation or tilt detected by the gyroscope and accelerometer.

Primary proximal outcomes:

- mean absolute synchronization error;
- synchronization variability;
- movement smoothness;
- stop-signal motor inhibition;
- subjective effort.

A second manipulation can compare motor-only, cognitive-only and simultaneous motor+cognitive conditions to estimate dual-task cost.

### 2.4 Real-world search substudy

Use the rear camera only for local feature extraction.

Candidate tasks:

- target color search;
- simple shape search;
- color+shape conjunction search.

Guidance conditions:

A. visual screen guidance;
B. auditory guidance;
C. auditory plus haptic guidance.

Primary proximal outcomes:

- target acquisition time;
- false candidate count;
- rule errors;
- proportion of search requiring visible screen guidance.

The hypothesis is not that camera use itself is therapeutic. The experiment tests whether non-visual guidance can maintain task performance while moving attention from the display into the real environment.

### 2.5 Facial-feedback validation substudy

During eligible stationary tasks, collect only locally derived facial features together with:

- objective task difficulty;
- errors and reaction-time variability;
- sensorimotor performance;
- child-reported difficulty;
- optional observer ratings where separately approved.

Primary question:

Does facial behavior add predictive information about excessive task demand after objective performance measures are already known?

Ablation conditions for a later adaptive-controller study:

A. performance-only adaptation;
B. performance + sensorimotor adaptation;
C. performance + sensorimotor + facial-behavior adaptation.

Primary proximal outcomes:

- time spent in prespecified overload state;
- self-reported excessive difficulty;
- error bursts;
- task completion;
- unnecessary difficulty reductions.

The facial module should be considered unsupported as an adaptive component if it does not provide reproducible incremental value.

### 2.6 Bilateral-auditory feasibility substudy

This should be optional and separate from the main efficacy claim.

Within-person conditions:

A. alternating left-right auditory stimulation;
B. matched simultaneous/central stereo stimulation;
C. quiet regulation period.

Proximal outcomes:

- subjective activation;
- recovery latency;
- post-challenge error rate;
- return-to-task success;
- tolerability.

A null difference between alternating and matched non-alternating stimulation should argue against retaining bilateral stimulation as a specific therapeutic mechanism.

## 3. Initial dose

Provisional dose:

- 8 weeks;
- 4 sessions per week;
- 15-20 min per session.

Within a session, AR should initially be limited to short blocks rather than continuous use.

This dose should be revised after feasibility data.

## 4. Inclusion criteria

Example criteria for the first controlled trial:

- age 8-12 years;
- independently established ADHD diagnosis;
- stable treatment plan for a prespecified period before baseline when receiving medication;
- caregiver able to complete study assessments;
- ability to understand study instructions;
- ability to use the research device safely with available accommodations.

## 5. Exclusion criteria

Exclusion should be minimal and justified. Candidate exclusions:

- acute clinical risk requiring immediate treatment beyond study scope;
- sensory or motor limitation that makes the current interface unusable and cannot be accommodated;
- condition making the planned movement tasks unsafe;
- medication change immediately before baseline when it would make interpretation impossible.

Common co-occurring neurodevelopmental, sensory or emotional difficulties should be measured and reported rather than automatically excluded.

## 6. Outcome hierarchy

### Primary outcome

A preregistered, external caregiver-rated emotion-regulation or emotion-dysregulation measure with an age-appropriate validated version.

The exact Polish instrument should be selected before recruitment based on validation status, licensing and sensitivity to change.

### Key secondary outcomes

- ADHD symptom severity from caregiver report;
- teacher report where feasible;
- functional impairment;
- independent inhibition task;
- independent working-memory task;
- cognitive flexibility task;
- child quality of life;
- intervention acceptability;
- adherence.

### Mechanistic secondary outcomes

- body-state identification consistency;
- in-game recovery latency;
- cross-modal inhibition performance;
- AR versus stationary task performance;
- movement exposure;
- sensory-overload rate.

### Exploratory outcomes

- ecological momentary ratings of frustration and recovery;
- post-error performance;
- strategy selection;
- within-session learning slopes;
- relationship between telemetry and independent outcomes;
- response to bilateral versus non-bilateral auditory regulation.

## 7. Assessment schedule

| Measure | Baseline | Mid | Post | Follow-up |
|---|---:|---:|---:|---:|
| clinical ratings | yes | optional | yes | yes |
| executive tasks | yes | no | yes | yes |
| functional impairment | yes | no | yes | yes |
| body-awareness/interoception measure | yes | optional | yes | optional |
| sensory tolerability | yes | continuous | yes | optional |
| acceptability | no | optional | yes | optional |
| adverse events | continuous | continuous | yes | yes |
| game telemetry | no | continuous | no | no |

A follow-up of at least 1-3 months is desirable in the pilot. A later confirmatory study should use a longer follow-up.

## 8. Randomization and masking

Recommended:

- computer-generated allocation;
- concealment until enrollment is complete;
- stratification by medication status and possibly baseline dysregulation;
- blinded outcome assessor for independent tasks when practical;
- intervention labels that do not reveal which game is hypothesized to be superior;
- automated randomization of eligible sensory cue events.

Participants cannot be fully blinded to game content, so expectancy should be measured.

For the bilateral-audio substudy, condition labels should not indicate which pattern is hypothesized to be active.

## 9. Analysis principles

Primary analysis:

- intention-to-treat;
- linear mixed-effects model or equivalent repeated-measures framework;
- group x time interaction;
- baseline adjustment;
- effect estimate with 95% confidence interval;
- prespecified handling of missing data.

Pilot results should emphasize effect estimates and uncertainty rather than binary significance testing.

Potential covariates must be prespecified, for example:

- age;
- sex;
- baseline severity;
- stable medication status;
- relevant co-occurring conditions;
- baseline sensory sensitivity when mechanistically relevant.

## 10. Mechanism analysis

A separate analysis should examine whether change in the in-game recovery measure predicts change in the external primary outcome.

This association must not be interpreted as mediation unless temporal ordering, model assumptions and study power support a formal mediation analysis.

For micro-randomized cue data, use a repeated-measures model that accounts for events nested within sessions and participants.

For AR comparisons, separate the effects of:

- cognitive task;
- modality;
- physical movement;
- session order.

Movement amount must not be treated as equivalent to therapeutic benefit.

## 11. Sample size

The feasibility phase should not be justified by efficacy power.

For the pilot RCT, sample size should be determined from:

- primary endpoint variance;
- minimally relevant between-group effect;
- repeated-measures correlation;
- expected attrition.

The embedded mechanistic experiments can use repeated within-person observations to estimate proximal effects more efficiently, but participant-level clustering must be modeled.

If parameters are not known, the pilot should estimate them and explicitly defer confirmatory power calculations to the next trial.

## 12. Preregistration

Before the first randomized participant:

- register the protocol;
- freeze the primary outcome;
- freeze primary time point;
- publish the statistical analysis plan;
- define exclusion criteria;
- define telemetry variables before outcome unblinding;
- define eligible events for sensory micro-randomization;
- define AR versus stationary comparison rules;
- define bilateral-audio sham/control condition;
- document all deviations.

## 13. Reporting

Use CONSORT guidance applicable to randomized trials and relevant digital/eHealth extensions where appropriate.

The manuscript should report:

- intervention version;
- device/platform constraints;
- sensory configuration;
- headphone use where applicable;
- proportion of stationary and AR sessions;
- completion dose;
- adverse events;
- sensory-overload events;
- missingness;
- attrition by arm;
- deviations from intended use;
- near-transfer and far-transfer outcomes separately;
- component-level null findings as well as positive findings.
