# Sensorimotor fusion and smartphone-sensor training

## 1. Rationale

ARC-ADHD should treat the smartphone not only as a display and response surface, but as a compact multisensor device that can measure how the child moves, orients and synchronizes the device with sensory cues.

The core principle is **closed-loop sensorimotor training**:

**cue -> bodily action -> sensor measurement -> immediate feedback -> adaptation -> reflection**

This extends the intervention beyond visual cognitive training and creates experimentally measurable links between attention, inhibition, rhythm, motor control and body awareness.

## 2. Scientific distinction: interoception, proprioception and sensorimotor control

Moving a phone in response to vibration is not a pure interoception task.

It primarily combines:

- proprioception, awareness of limb and joint position;
- tactile/haptic perception;
- vestibular and visuospatial information;
- sensorimotor synchronization;
- motor planning and correction.

Interoception concerns signals originating from within the body, such as breathing, cardiac sensations, visceral state and perceived arousal.

ARC-ADHD should therefore describe these exercises as an **interoceptive-proprioceptive bridge** when they combine:

1. externally generated haptic rhythm;
2. controlled movement;
3. subjective observation of bodily tension, breathing or activation;
4. comparison of body state before and after movement.

This prevents conceptual overclaiming.

## 3. Smartphone sensor set

### 3.1 Gyroscope

Measures angular velocity around the device axes.

Primary uses:

- controlled wrist rotation;
- rhythmic pronation/supination-like movements;
- orientation-change tasks;
- smoothness measurement;
- stop/start motor inhibition;
- synchronization to haptic or auditory rhythm.

### 3.2 Accelerometer

Measures linear acceleration including the gravity component.

Primary uses:

- movement onset/offset detection;
- movement amplitude proxy;
- shake versus controlled motion discrimination;
- rhythmic up/down or lateral movement;
- movement regularity;
- detecting whether the device is stationary.

### 3.3 Sensor fusion / device orientation

Use fused orientation estimates rather than raw gyroscope integration when possible.

Primary uses:

- target-angle tasks;
- slow trajectory following;
- orientation memory;
- returning the device to a neutral pose;
- tracing spatial patterns by tilt.

### 3.4 Touchscreen

The touchscreen should be combined with IMU rather than treated as a separate interface.

Examples:

- stabilize the phone while tracing with one finger;
- drag an object while maintaining a target orientation;
- alternate thumb taps while following a haptic rhythm;
- perform a fine touch sequence while ignoring irrelevant device movement cues.

These tasks are better candidates for **fine motor control** than phone rotation alone.

### 3.5 Rear camera

The rear camera can support real-world visual search without storing images.

Candidate functions:

- detect a requested color region;
- detect simple geometric shapes;
- verify that a virtual task target corresponds to a real object property;
- recognize fiducial markers in controlled research tasks;
- estimate coarse object position in the image.

The first research build should prefer low-risk local computer-vision operations over open-ended semantic recognition.

### 3.6 Microphone

The microphone is not required for the initial core intervention.

Possible future uses:

- clap/tap rhythm timing;
- environmental sound-level estimation;
- voice-guided interaction.

Continuous audio recording should not be part of standard telemetry.

### 3.7 Magnetometer

Potential use:

- coarse orientation tasks;
- directional search.

Because indoor magnetic fields are noisy, it should not be a primary precision sensor.

### 3.8 Ambient light sensor

Where the platform exposes a reliable sensor, ambient light can support:

- automatic adaptation of visual contrast;
- detection of unsuitable camera-search lighting;
- logging environmental illumination class.

It should not become a therapeutic variable unless separately studied.

### 3.9 Proximity sensor

Where accessible, proximity can support simple near/far interaction states, but availability differs across devices and operating systems.

### 3.10 Barometer

On devices that expose pressure sensors, the barometer can support coarse vertical-change experiments, but it is not required for the core intervention.

### 3.11 Capability principle

Every non-core sensor must have:

- runtime capability detection;
- a defined fallback;
- a versioned device-capability record;
- no requirement that would unnecessarily exclude participants with lower-cost phones.

## 4. Motor-training modules

## 4.1 Haptic rhythm matching

The phone generates a haptic pulse train. The child moves the phone in time with the rhythm.

Example movements:

- slow left-right rotation;
- controlled forward-back tilt;
- small circular wrist motion;
- alternating movement and stillness.

Measured variables:

- phase lag relative to the haptic beat;
- inter-movement interval variability;
- amplitude variability;
- movement smoothness;
- premature movement;
- missed movement;
- overshoot.

The haptic rhythm can gradually change to train adaptation rather than rote repetition.

## 4.2 Auditory-haptic synchronization

Audio and haptic cues can be presented:

- synchronously;
- with a small deliberate phase offset;
- with one modality removed;
- with alternating modality leadership.

Research questions:

- Which modality produces the best synchronization?
- Does congruent audiovisual-haptic timing improve motor regularity?
- Can the child inhibit the dominant cue when the rule changes?

## 4.3 Stop-go motor inhibition

The child moves the phone rhythmically until a stop cue appears.

Stop cue variants:

- sound;
- vibration pattern;
- visual flash;
- multimodal cue.

Outcomes:

- stop latency;
- residual movement after stop cue;
- false starts;
- ability to resume the rhythm.

This combines motor control and inhibitory control in one observable task.

## 4.4 Orientation target

The game asks the child to place the phone at a target orientation.

Difficulty can change through:

- smaller tolerance window;
- memory delay before movement;
- removal of visual guidance;
- distractor sound;
- rule reversal.

Outcomes:

- angular error;
- movement time;
- overshoot;
- correction count;
- path efficiency.

## 4.5 Smooth trajectory task

The child follows an invisible or partially visible orientation trajectory.

This supports:

- slow controlled movement;
- continuous error correction;
- sustained attention;
- sensorimotor prediction.

Candidate metrics:

- RMS orientation error;
- mean angular jerk;
- correction frequency;
- spectral concentration around the target rhythm.

## 4.6 Bilateral hand-switching task

The same task is repeated with the phone held in the left and right hand.

The aim is not to diagnose lateralization. It is to:

- vary motor context;
- prevent overlearning with one hand;
- test transfer of a learned rhythm;
- compare within-person motor consistency.

Hand condition must be logged.

## 5. Fine-motor training

Holding and rotating a smartphone mainly trains wrist/forearm control rather than isolated fine finger dexterity.

To specifically target fine motor control, combine touch and IMU.

Candidate tasks:

### Stable-hand tracing

The child traces a narrow path with one finger while keeping the phone within a target orientation range.

Metrics:

- trace error;
- touch velocity variability;
- orientation drift;
- number of corrective movements.

### Tap sequence with postural constraint

The child performs a finger sequence while holding the phone at a prescribed angle.

Metrics:

- timing accuracy;
- sequence errors;
- unwanted device movement.

### Pinch/drag with rhythmic cue

Pinch or drag gestures must occur at specific points in a haptic rhythm.

Metrics:

- temporal error;
- spatial error;
- pressure proxy where the platform supports it;
- motion artifact.

### Dual-task motor control

Maintain device orientation while responding to occasional auditory targets.

This permits controlled examination of motor-cognitive interference.

## 6. Body-awareness integration

Each sensorimotor task can include a brief body-state loop.

Before:

- How tight are your hands?
- Are your shoulders relaxed?
- Is your breathing easy to notice?
- Does your body want to move quickly or slowly?

During:

- haptic cue guides the action;
- the child notices effort and tension;
- no requirement is made to label an emotion.

After:

- compare tension, breathing and activation;
- select whether the movement helped, changed nothing or made regulation harder.

This is the appropriate point where sensorimotor training can connect to interoceptive awareness.

## 7. Haptic entrainment model

For beat times h_k and detected movement peaks m_k, define temporal synchronization error:

e_k = m_k - h_k

Candidate derived measures:

mean absolute synchronization error:

MAE_sync = mean(|e_k|)

variability:

SD_sync = SD(e_k)

and signed phase bias:

Bias_sync = mean(e_k)

These allow separation of:

- systematic anticipation;
- systematic lag;
- unstable timing.

The adaptation controller can modify tempo only after a stable measurement window.

## 8. Movement smoothness

Raw IMU data should be filtered before analysis.

Candidate features:

- angular velocity RMS;
- peak angular velocity;
- angular jerk;
- number of direction reversals;
- spectral power around the target frequency;
- movement entropy;
- overshoot count.

These are process measures. They are not diagnostic biomarkers unless separately validated.

## 9. Camera-guided real-world search

The rear camera can turn the real environment into a visual-search space.

## 9.1 Color search

Example instruction:

"Find something blue."

The application can locally identify image regions in a target hue range.

The child moves the device until a sufficiently large stable region is detected.

Possible variables:

- search time;
- camera path;
- number of false candidate regions;
- dwell time before confirmation.

Color detection must account for illumination and white-balance variability.

## 9.2 Shape search

Example:

"Find a circle."

Possible first-stage implementation:

- contour extraction;
- polygon approximation;
- circle/ellipse detection;
- geometric confidence threshold.

This is preferable to unrestricted object recognition for the first research prototype because the rule is auditable and privacy risk is lower.

## 9.3 Combined rule

Examples:

- find a red circle;
- find a blue rectangular region;
- find one object matching color A but not shape B.

This supports:

- selective attention;
- working-memory rule maintenance;
- inhibition of distractors;
- rule switching.

## 10. Audio-guided real-world search

Sound can guide attention without requiring continuous fixation on the screen.

Candidate implementations:

### Proximity sonification

As the camera or AR system estimates that the searched target is closer to the center or target location:

- pulse rate increases;
- pitch changes;
- stereo balance shifts.

### Directional stereo cue

When a target is estimated to the left or right of the camera center:

- audio balance shifts toward that side.

The child searches the room by integrating auditory direction with real-world vision.

### Haptic complement

A brief vibration can indicate:

- target acquired;
- target lost;
- stop and verify;
- return to neutral orientation.

The audio should guide attention, not force the child to stare at the display.

## 11. Multisensor search loop

A complete search task can follow:

1. spoken instruction gives the rule;
2. child memorizes the target;
3. screen guidance fades;
4. child scans the real environment with the rear camera;
5. audio guides direction;
6. IMU measures search movement;
7. local vision verifies color/shape;
8. haptic signal confirms acquisition;
9. child lowers the phone;
10. brief body-state check follows.

This is a concrete realization of the ARC principle:

**screen -> body action -> environment -> multisensory feedback -> regulation -> goal completion**

## 12. Sensor-fusion state vector

Extend the modality model with a sensor state:

s_t = [omega_t, a_t, q_t, touch_t, cam_t, audio_t]

where:

- omega = angular velocity;
- a = acceleration;
- q = estimated orientation;
- touch = touch interaction state;
- cam = locally derived visual features;
- audio = output/input event state.

Observed behavior becomes:

y_t = f(x_t, d_t, m_t, s_t, c_t) + epsilon_t

This permits sensor-derived behavior to be modeled without treating raw sensor values as direct measures of ADHD severity.

## 13. Adaptation

Adaptation can occur on separate dimensions:

- cognitive load;
- motor precision;
- rhythm tempo;
- sensory complexity;
- visual-search complexity;
- amount of guidance.

Example:

A child may show accurate cognitive performance but poor motor synchronization. The system should lower motor tempo rather than simplify the cognitive rule.

Conversely, good motor rhythm with poor rule maintenance should not trigger faster movement.

## 14. Safety

### Movement

- no throwing the device;
- no rapid maximal-amplitude wrist movements;
- no tasks requiring movement near the face;
- optional seated version;
- pause on excessive acceleration;
- caregiver configuration for younger participants.

### Camera

- local frame processing;
- no recording by default;
- no face recognition;
- no upload of environmental imagery;
- do not ask the child to search for people.

### Haptics

- short bounded patterns;
- user-adjustable intensity;
- immediate disable option.

### Sensor interpretation

Do not classify a child as having a motor deficit, poor interoception or ADHD severity based solely on game telemetry.

## 15. Experimental decompositions

### Haptic entrainment experiment

Compare:

A. haptic rhythm;
B. auditory rhythm;
C. audio+haptic rhythm.

Outcome:

- synchronization error and variability.

### Visual-search guidance experiment

Compare:

A. visual screen arrow;
B. auditory guidance;
C. auditory+haptic guidance.

Outcome:

- real-world target acquisition time while minimizing screen fixation.

### Motor-cognitive dual-task experiment

Compare:

A. motor rhythm only;
B. cognitive task only;
C. simultaneous motor+cognitive task.

Outcome:

- dual-task cost for motor and cognitive performance.

### Camera-search experiment

Compare:

A. color rule;
B. shape rule;
C. conjunction rule.

Outcome:

- search time, false detections and rule errors.

## 16. Core research hypothesis

The smartphone should be treated as a **sensorimotor mediator** between cognition, body and environment.

The strongest testable claim is not that gyroscope training "treats ADHD", but that multimodal sensorimotor tasks can:

1. quantify and train specific motor-control processes;
2. create repeated opportunities for inhibition and rule maintenance during movement;
3. improve engagement with real-world space;
4. provide a structured bridge from externally cued movement to awareness of bodily state;
5. generate mechanistic variables that can be tested against independent outcomes.
