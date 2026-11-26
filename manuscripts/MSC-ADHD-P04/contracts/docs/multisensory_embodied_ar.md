# Multisensory, embodied and AR design

## 1. Rationale

ARC-ADHD should use the smartphone as a multisensory interaction device rather than as a small visual display. Visual, auditory, haptic, proprioceptive/interoceptive and movement-related information should be coordinated around the same therapeutic action.

The design objective is **cross-modal congruence**, not maximal stimulation. Additional channels should make a task easier to perceive, support inhibition or regulation, or move attention from the screen toward the body and the surrounding environment. Sensory channels must not be added merely to increase stimulation.

The intervention therefore distinguishes:

- visual information;
- auditory information;
- haptic/vibrotactile information;
- body-focused/interoceptive information;
- physical movement;
- augmented-reality interaction with the environment;
- optional bilateral auditory stimulation.

## 2. Multisensory control model

Let the latent functional state remain:

x_t = [A_t, I_t, W_t, F_t, R_t]

where A, I, W, F and R denote attention, inhibition, working-memory control, flexibility, and regulation/recovery.

Introduce a modality/context vector:

m_t = [V_t, Au_t, H_t, B_t, M_t, AR_t]

where:

- V = visual cue state;
- Au = auditory cue state;
- H = haptic/vibrotactile cue state;
- B = body-awareness/interoceptive component;
- M = movement demand;
- AR = degree of coupling to the real environment.

Observed behavior is then modeled conceptually as:

y_t = f(x_t, d_t, m_t, c_t) + epsilon_t

where d_t is cognitive difficulty and c_t contains contextual factors such as fatigue, device state and task history.

This prevents a methodological error in which improvement caused by an extra sensory cue is incorrectly interpreted as improvement of the underlying executive function.

## 3. Visual modality

Visual information remains the principal channel for spatial and object-level interaction, but it should be deliberately limited.

Recommended rules:

- one dominant task target at a time;
- low visual clutter outside explicit distractor conditions;
- strong figure-ground separation;
- limited animation unrelated to the current goal;
- color never used as the sole information channel;
- adjustable motion intensity;
- predictable visual transitions.

Visual distractors are experimental manipulations, not decorative content.

## 4. Auditory modality

Sound should be used for temporal structure, selective attention and off-screen information.

Possible functions:

- auditory target detection;
- inhibition cue;
- temporal/rhythmic sequencing;
- spatialized indication of an off-screen target;
- calm spoken guidance during regulation;
- sonification of breathing or movement rhythm;
- confirmation that a task state has changed without requiring continuous visual fixation.

A key design principle is that some tasks should be solvable by listening while looking away from the display.

### 4.1 Auditory attention tasks

Examples:

- detect a target tone among distractor sounds;
- respond to a target only when visual and auditory rules agree;
- inhibit a response when a specific sound occurs;
- remember and reproduce short sound sequences;
- switch between "follow the image" and "follow the sound" rules.

These tasks allow cross-modal selective attention and task switching to be measured explicitly.

## 5. Haptic and vibrotactile modality

Phone vibration should become an information channel, not merely feedback after success.

Potential uses:

- a short pulse marking "pause before action";
- distinct pulse patterns for go, stop and rule-switch cues;
- paced vibration during breathing;
- rhythmic tapping tasks;
- haptic warning when attention has to return from the screen to the environment;
- tactile confirmation during AR movement tasks.

Haptic cues should be short and low intensity. Continuous or startling vibration should be avoided.

The child or caregiver must be able to reduce or disable haptics. Sensory hypersensitivity must be treated as a design constraint, not as non-compliance.

## 6. Body awareness and interoception

A specific ARC-ADHD component should train noticing bodily signals that accompany activation and recovery.

The evidence base supports studying interoception in ADHD, but it does not justify assuming that interoceptive training is already an established ADHD treatment. Accordingly, this module should initially be treated as a mechanistic and exploratory component.

### 6.1 Body check-in

A check-in should avoid abstract questions such as "How do you feel?" as the only prompt.

The child can instead be guided through concrete observations:

- Is breathing fast, slow or hard to notice?
- Are the shoulders loose or tense?
- Are the hands relaxed or tightly held?
- Does the body feel still or as if it wants to move?
- Is the jaw relaxed or tense?
- Do the feet feel firmly in contact with the floor?
- Does the body feel warmer, colder or unchanged?

The goal is noticing, not judging.

### 6.2 Body map

An age-appropriate body silhouette can be used to indicate where the child notices activation.

The body map should be used as a subjective report and must not be interpreted as a diagnostic biomarker.

### 6.3 Regulation through movement

Short regulation actions can include:

- slow reach and return;
- bilateral hand movements;
- shoulder tension and release;
- standing and grounding through the feet;
- controlled weight shifting;
- slow walking to an AR target;
- matching movement to an auditory or haptic rhythm.

No breath holding, hyperventilation or high-intensity exercise should be required.

## 7. Multisensory regulation sequences

A regulation sequence can deliberately shift the dominant sensory channel.

Example:

1. visual challenge produces a frustration event;
2. screen content becomes visually quieter;
3. phone emits a short haptic "pause" cue;
4. child looks away from the screen;
5. spoken instruction asks the child to notice feet and breathing;
6. a slow vibration or sound rhythm guides two or three cycles;
7. the child physically moves to the next AR anchor;
8. the task resumes.

This creates a transition from exteroceptive task demand to body awareness and then back to goal-directed action.

## 8. Augmented-reality mode

AR should be a core alternative mode rather than a cosmetic camera overlay.

The main design goals are:

- maintain contact with the real environment;
- reduce prolonged stationary screen use;
- incorporate locomotion and orientation;
- support transfer from digital task to real-world action;
- permit executive-control tasks to be embedded in ordinary physical space.

### 8.1 Candidate AR tasks

#### Spatial target search

Virtual targets are anchored to safe surfaces in a prepared room. The child must remember a rule and physically move to the correct target.

Targets:
- working memory;
- selective attention;
- navigation;
- response inhibition.

#### Stop-and-go exploration

The child walks between AR anchors. Audio or haptic stop signals require movement inhibition before the next step.

Targets:
- motor inhibition;
- sustained attention;
- response control.

#### Rule-switch trail

Objects initially follow one sorting rule and later switch to another.

Targets:
- cognitive flexibility;
- working memory;
- recovery from rule errors.

#### Regulation stations

After an error or challenge, a regulation object appears away from the current screen-centered position. The child has to orient to the room, move to the station and perform a short body-based strategy.

Targets:
- disengagement from perseveration;
- body awareness;
- recovery;
- return to goal.

#### Real-world grounding task

The game asks the child to identify safe properties of the current environment, for example three visible shapes or two sounds, without collecting or storing identifiable environmental imagery.

Target:
- external attentional redeployment and grounding.

## 9. AR safety

The first research build should use **indoor, caregiver-prepared play zones**.

Mandatory constraints:

- no use near roads, stairs, balconies, kitchens or water;
- no running;
- caregiver confirms a clear area before the first AR block;
- movement targets remain within a small bounded zone;
- the game pauses if tracking quality is lost;
- no reward is lost for stopping;
- screen fixation while walking is minimized;
- camera frames should be processed locally unless a separately approved research purpose requires storage;
- no face recognition or environmental surveillance is required.

Outdoor geolocation gameplay should not be part of the initial clinical research build.

## 10. Movement as a therapeutic variable

Movement should be logged and experimentally separated from cognitive difficulty.

Potential smartphone-derived variables:

- movement duration;
- number of transitions between anchors;
- angular orientation changes;
- coarse displacement proxy;
- task completion while moving versus stationary.

Accelerometer and gyroscope data should be processed into predefined features where possible rather than uploading continuous raw sensor streams.

The project should test whether movement improves engagement, executive-task performance or regulation. It should not assume that more movement is always better.

## 11. Optional bilateral auditory stimulation

Alternating left-right auditory stimulation through stereo Bluetooth headphones can be implemented as an **experimental module**.

This component must not be described as an established ADHD treatment and must not be equated with EMDR.

At present, evidence specifically supporting bilateral auditory stimulation for core ADHD symptoms or emotion regulation in children is insufficient. Its inclusion is therefore justified only as a falsifiable mechanistic sub-study.

### 11.1 Candidate implementation

- alternating low-complexity tones or soft non-verbal sounds;
- slow, configurable left-right alternation;
- fixed short duration;
- conservative volume limit;
- immediate stop control;
- headphone channel check before use;
- no aversive, startling or emotionally loaded sound.

Bluetooth latency means the system should not make millisecond-level neurophysiological claims from nominal software timing alone.

### 11.2 Experimental comparison

A blinded within-person comparison can use:

A. alternating left-right stimulation;
B. matched simultaneous or centrally presented stereo stimulation;
C. quiet regulation period.

Proximal outcomes:

- subjective activation before/after;
- recovery latency;
- post-challenge error rate;
- ability to resume the task;
- acceptability and adverse sensory responses.

A clinical symptom claim should require a separate adequately powered trial.

## 12. Sensory personalization

Personalization should control tolerability, not manipulate the child into longer play.

Configurable dimensions:

- sound level;
- spoken instruction on/off;
- haptic intensity;
- haptic on/off;
- animation intensity;
- AR on/off when the protocol permits;
- reduced-stimulation mode;
- headphone mode.

The study should record configuration because modality availability changes the delivered intervention.

## 13. Multisensory overload rule

More modalities are not necessarily better.

The controller should include a sensory-load state S_t based on:

- number of simultaneously active channels;
- recent errors;
- rapid exits or pauses;
- child-reported overload;
- repeated missed instructions.

If overload criteria are reached, the controller should reduce simultaneous channels before lowering the cognitive construct being trained.

This distinction is critical because sensory overload and cognitive difficulty are not equivalent.

## 14. Research design for modality effects

A large between-group trial is inefficient for testing every sensory component. ARC-ADHD should embed smaller mechanistic experiments.

### 14.1 Micro-randomized cue trial

At eligible task moments, randomize among:

- visual-only cue;
- audiovisual cue;
- audiovisual plus haptic cue.

Primary proximal outcome:

- probability of correct inhibition or strategy initiation.

Secondary outcomes:

- response latency;
- missed cues;
- overload/pause events.

### 14.2 AR versus stationary blocks

Use matched cognitive content in:

- stationary screen mode;
- AR movement mode.

Compare:

- executive performance;
- adherence;
- recovery;
- movement;
- perceived effort;
- enjoyment;
- adverse effects.

### 14.3 Bilateral-audio substudy

Keep this separate from the principal intervention efficacy analysis unless prior feasibility results justify making it a core component.

## 15. New hypotheses

**H6.** Congruent multisensory cues will improve proximal task-state detection and inhibitory responding relative to visual-only cues, but the effect will vary with sensory tolerance.

**H7.** Repeated body-awareness practice will be associated with improved identification of activation and shorter recovery after challenge, without assuming that subjective body awareness itself is a clinical endpoint.

**H8.** AR movement blocks will show higher physical engagement and at least non-inferior executive-task performance compared with matched stationary blocks.

**H9.** If bilateral auditory stimulation has a specific regulatory effect, alternating stimulation should produce a measurable proximal advantage over matched non-alternating stimulation. Failure to observe this difference should be treated as evidence against retaining the component.

## 16. Design principle

ARC-ADHD should deliberately move the child through three attentional spaces:

**screen -> body -> real environment -> goal**

The phone is therefore a temporary mediator of regulation, not the environment in which the child is expected to remain continuously immersed.
