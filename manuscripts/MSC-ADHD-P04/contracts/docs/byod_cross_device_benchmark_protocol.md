# ARC-ADHD BYOD cross-device benchmark protocol

Status: pre-freeze engineering protocol, version 0.1.

This protocol defines how candidate private Android execution environments are tested before the Phase 0 BYOD compatibility policy is frozen.

It does **not** define final pass/fail timing thresholds. Numerical timing thresholds must be selected from engineering evidence and scientific requirements before participant outcome data are inspected.

## 1. Purpose

The benchmark answers four questions:

1. Can the core ARC-ADHD runtime execute reliably across the intended Android range?
2. Which device/runtime characteristics materially affect task/recovery telemetry?
3. Which technical checks can be enforced locally before a participant session?
4. What compatibility/fallback policy minimizes invalid measurement without unnecessary device exclusion?

The benchmark is an engineering-validation exercise, not a ranking of phone quality.

## 2. Boundary of what the app can measure

An app-only benchmark can validly characterize:

- application frame-time distribution;
- missed/stalled application frames;
- monotonic-clock ordering;
- software scheduling deviation relative to the app's own monotonic clock;
- task/state-machine determinism;
- telemetry write/persistence behavior;
- queue restart/retry/deduplication behavior;
- application background/resume behavior;
- runtime exceptions/fatal errors;
- coarse thermal/power warnings exposed by the platform;
- supported optional capabilities.

An app-only benchmark does **not** directly establish:

- physical display onset latency;
- touch-to-photon latency;
- absolute touchscreen hardware latency;
- acoustic output latency;
- haptic perceptual onset latency.

Those quantities require an external reference measurement if the scientific analysis later depends on them.

Do not infer physical timing accuracy from software timestamps alone.

## 3. Device sampling

The engineering pool should represent the intended BYOD population rather than only recent flagship phones.

Before freeze, document coverage across:

- Android major/API versions under consideration;
- low, middle and high runtime-performance classes;
- common refresh-rate classes;
- small/medium/large logical display classes;
- devices with and without haptics;
- devices with different memory/storage constraints;
- multiple vendors where available.

The study does not need equal numbers per commercial model.

Exact manufacturer/model may be retained in the private engineering benchmark log when necessary to reproduce technical faults. It is not automatically part of participant research telemetry.

## 4. Build freeze for a benchmark round

Every benchmark round must freeze:

- repository commit;
- Unity version;
- Android build/application version;
- task configuration;
- benchmark script/configuration version;
- telemetry schema;
- state-machine version;
- BYOD qualification-policy candidate version.

Results from materially different builds must not be pooled without explicit version handling.

## 5. Run identifiers

Every run receives:

- random benchmark run ID;
- engineering device label;
- capability-profile ID;
- application version;
- Android major version;
- benchmark protocol/config version;
- run index on the device;
- execution-condition code.

The engineering device label must not be derived from IMEI, serial number, Android ID, advertising ID or MAC address.

## 6. Benchmark conditions

At minimum test each candidate execution environment under:

### Condition A: ordinary foreground run

- app in foreground;
- no intentional network dependency;
- normal device state;
- complete deterministic benchmark sequence.

### Condition B: offline run

- network unavailable;
- full task/state-machine/telemetry path remains functional;
- upload remains queued rather than affecting intervention logic.

### Condition C: restart persistence

- write a committed telemetry batch;
- terminate/restart the app;
- verify the pending queue is recoverable;
- verify no duplicate scientific events are created after retry/acknowledgement.

### Condition D: background/resume

- background the app at predefined safe states;
- resume;
- verify allowed resume paths;
- verify an open recovery interval is invalidated when the configured validity rule requires it.

### Condition E: full-duration synthetic session

- execute at least the maximum planned Phase 0 session duration;
- include repeated task/challenge/state transitions;
- monitor frame-time, errors, queue integrity and thermal/power warnings.

Additional stress conditions may be added, but they must not replace the ordinary-use conditions.

## 7. Warm-up and repetition

The benchmark configuration should define:

- warm-up duration/trials;
- number of repeated runs per execution condition;
- full-duration synthetic-session length;
- whether runs are repeated after app restart;
- whether runs are repeated after device restart.

These values remain `UNSET` until the benchmark package is frozen.

Do not choose repetition counts after inspecting which devices fail.

## 8. Frame-time metrics

Record at least:

- sample count;
- median frame time;
- p95 frame time;
- p99 frame time;
- maximum frame time;
- count/rate of frames beyond a candidate stall boundary;
- longest consecutive degraded-frame sequence.

The candidate stall boundary is a versioned engineering parameter.

Do not define a device as scientifically invalid solely because its nominal refresh rate is lower.

The relevant question is whether the frozen task and measurement logic remain stable and interpretable.

## 9. Software scheduling metrics

For deterministic scheduled events record:

- requested monotonic schedule time;
- actual callback/dispatch monotonic time;
- signed deviation;
- absolute deviation;
- p50/p95/p99 absolute deviation;
- number of severe scheduling stalls.

This measures **software scheduling behavior**, not physical stimulus onset.

If absolute physical onset is needed for a later endpoint, perform a separate external validation.

## 10. Monotonic timing invariants

Hard invariants:

- scientific event timestamps never move backward within one clock domain;
- monotonic sequence numbers are strictly increasing where required;
- no duplicate event ID represents a second scientific event;
- wall-clock changes do not alter scientific interval computation.

Any violation is an implementation/integrity failure rather than ordinary device variability.

## 11. State-machine replay

The benchmark should execute deterministic reference paths covering:

- normal observed-recovery path;
- right-censored path;
- technical invalidation;
- child pause;
- safe stop;
- protocol abort;
- BYOD qualified-with-fallback path;
- technical interruption/resume.

For a frozen configuration and input sequence, recorded decisions must match the reference replay.

Any unexplained mismatch is a benchmark hard failure.

## 12. Signal Gate runtime check

The benchmark uses the same runtime path as the candidate Signal Gate task.

Record:

- rendered trial count;
- expected versus delivered state transitions;
- missed/duplicated trial IDs;
- input event count;
- task exceptions;
- timing summary.

Do not use a simplified benchmark loop that bypasses the scientific task/controller code.

## 13. Storage integrity

Hard checks:

- app-local store is writable;
- committed event survives ordinary app restart;
- queue survives offline operation;
- acknowledgement removes only acknowledged records;
- retry does not create duplicate event IDs;
- checksum/record-integrity checks pass when enabled.

Any durability failure means `benchmark_passed=false` regardless of frame-time performance.

## 14. Backgrounding and private-phone interruptions

Test:

- background during baseline task;
- background during a safe non-recovery state;
- background during recovery measurement;
- resume after allowed interruption;
- invalidation when recovery interpretability is lost.

Record:

- state at interruption;
- duration according to the app monotonic/elapsed clock;
- resume target;
- event validity decision;
- actual versus expected state-machine decision.

## 15. Thermal and power context

Where Android exposes reliable information, record coarse:

- thermal warning/state;
- power-saving state;
- battery level bucket;
- change over the full-duration run.

Do not disable user/system safety protections to obtain better benchmark results.

Final qualification rules should prefer warnings/fallbacks when scientifically valid rather than excluding devices solely for noncritical differences.

## 16. Audio and haptics

For core qualification:

- ordinary audio capability is optional;
- haptics are optional.

Benchmark:

- capability detection;
- command invocation success;
- fallback activation.

The core benchmark does not claim to validate auditory or haptic physical onset timing.

The bilateral-audio companion study requires a separate stereo/acoustic qualification.

## 17. Privacy

Engineering benchmark output should use the minimum device metadata required to diagnose compatibility.

Participant-facing qualification telemetry should remain coarser than private engineering logs.

Do not collect:

- IMEI;
- device serial;
- Android ID;
- advertising ID;
- MAC address;
- personal account identifiers;
- Wi-Fi SSID/BSSID;
- contacts;
- calls/messages;
- installed-app list;
- precise GPS;
- personal media metadata.

## 18. Hard-failure criteria independent of numerical thresholds

A run is technically invalid if any of the following occurs:

- fatal application error;
- monotonic timestamp ordering violation;
- deterministic state-machine/replay mismatch;
- missing or duplicated scientific event identity caused by runtime logic;
- durable-storage failure;
- telemetry queue cannot recover after required restart;
- retry creates duplicate scientific events;
- mandatory pause/stop path fails;
- offline run changes study-critical controller behavior;
- mandatory UI/touch check fails.

These invariants can be enforced before numerical performance thresholds are frozen.

## 19. Numerical threshold selection

Timing/performance thresholds are frozen only after a cross-device engineering dataset exists.

Selection process:

1. define which metric is scientifically relevant;
2. identify the failure mode the threshold is intended to prevent;
3. inspect the engineering-only cross-device distribution;
4. run sensitivity/replay checks;
5. choose the least restrictive threshold that still protects task/recovery interpretability;
6. document excluded device classes and expected exclusion burden;
7. freeze the threshold/version;
8. do not retune it using participant clinical or recovery outcomes.

Thresholds must not be chosen simply to preserve a desired percentage of devices.

## 20. Required candidate threshold fields

The future compatibility policy should explicitly freeze, where needed:

- minimum supported Android/API version;
- maximum acceptable p95/p99 application frame time or equivalent runtime criterion;
- stall definition and maximum allowed stall burden;
- software scheduling-deviation criterion if scientifically required;
- minimum free local storage;
- maximum allowed benchmark errors;
- full-duration run requirement;
- background/resume validity rules.

Fields not required for scientific validity should not become exclusion criteria.

## 21. Cross-device analysis

Before participant recruitment summarize:

- number of tested execution profiles;
- Android-version coverage;
- display/refresh classes;
- performance-class distribution;
- hard-failure rates by reason;
- optional fallback rates;
- frame-time distributions;
- scheduling-deviation distributions;
- storage/restart reliability;
- interruption/resume reliability;
- thermal/power warnings;
- proportion that would qualify under each candidate policy.

The final policy should report the expected technical exclusion burden.

## 22. Freeze rule

The BYOD compatibility policy may be marked frozen only after:

- benchmark protocol version is frozen;
- cross-device engineering data have been reviewed;
- mandatory hard invariants pass on supported profiles;
- numerical thresholds, if used, have documented rationale;
- expected device exclusion/fallback burden is known;
- the policy is encoded in machine-readable configuration;
- the repository commit is archived.

Participant outcome data must not be used to rescue or tighten the compatibility threshold after study start.

## 23. Machine-readable report

Each benchmark run should conform to:

`schemas/byod_benchmark_run.schema.json`.

Candidate threshold configuration is maintained in:

`config/byod_benchmark_thresholds.example.json`.

Both remain engineering contracts until the compatibility policy is frozen.
