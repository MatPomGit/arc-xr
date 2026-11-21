# Multimodal Cognitive-Load Estimation for Adaptive Information Density in Augmented Reality

> Draft v0.2.0. Prospective research design only. NOT SUBMITTED. No empirical results are reported.

## Abstract

**To be completed after the study.** This section must summarize the background, predefined methods, observed results with uncertainty and limitations; do not use anticipated results as if they were measured.

## 1. Introduction

Eye-tracking measures, including pupil diameter, fixations and saccades, may inform resource-constrained models that adjust the density of information in an augmented reality (AR) head-up display (HUD) and the level of three-dimensional detail. Facial signals remain optional and exploratory; no single physiological measure is treated as a diagnostic indicator of cognitive workload.

Research question: Does AR adaptation guided by multimodal cognitive-workload estimation reduce task errors compared with a static interface, and how does it compare with adaptation based on one modality?

## 2. Related work

Research has already examined the physiological adaptation of AR. Sun and Liao (2025) used a cumulative skin conductance metric to trigger rest breaks and reported reduced subsequent physiological load without demonstrating improved task performance ([DOI](https://doi.org/10.1017/dsj.2025.10040)). P01 therefore does not claim to be the first physiologically adaptive AR system.

Gonnermann-Müller et al. (2024) studied visual guidance and eye-tracking in industrial AR ([ICIS](https://aisel.aisnet.org/icis2024/humtechinter/humtechinter/18/)). Chiossi et al. (2024) analysed ERP and eye-tracking correlates of visual search in mixed reality ([DOI](https://doi.org/10.1109/TVCG.2024.3456172)). These studies motivate control of visual attention and task complexity; they do not establish the causal efficacy of the proposed three-way HUD-density comparison.

The review by Suzuki, Wild and Scanlon (2024; [DOI](https://doi.org/10.1111/jcal.12882)) documents heterogeneity in physiological cognitive-load assessment in AR. Pupillary responses are sensitive to luminance and other non-cognitive influences (Mathôt, 2018; [DOI](https://doi.org/10.5334/joc.18)). NASA-TLX is a complementary subjective instrument, not a continuous moment-to-moment ground truth (Hart and Staveland, 1988; [DOI](https://doi.org/10.1016/S0166-4115(08)62386-9)).

The proposed contribution is a controlled comparison of static, unimodally adapted and multimodally adapted AR HUD information density. Generalization of the load estimator must be assessed independently from the causal effect of adaptation on a prespecified behavioural endpoint. The [literature matrix](related_work.md) documents existing evidence, its limitations and the proposed research gap. Bibliographic identifiers appear in [references.bib](references.bib). No P01 results are reported.

## 3. Research questions and hypotheses

- H1 (proposed): Multimodally adapted HUD information density reduces the proportion of task trials with errors compared with a static HUD under comparable conditions. Subjective workload is a secondary outcome and cannot substitute for the proposed primary endpoint.
- H2 (proposed): Given a prespecified and comparable computational budget, the multimodal cognitive-workload estimator generalises better to participants excluded from model training than a single-modality estimator.

These hypotheses must be operationalized and preregistered, if applicable, prior to confirmatory data collection.

## 4. Materials and methods

Proposed design: A counterbalanced, within-participant comparison of a static HUD, single-modality adaptive HUD and multimodally adaptive HUD. Generalisation of the predictive model and the causal effect of the interface intervention will be evaluated separately.

Sample and setting: Adult participants performing standardised information-selection tasks in AR. Eligibility criteria and sample size require prospective justification through a power or precision analysis.

Manipulated factors and comparators: Interface condition, task difficulty and information density. The exact manipulations, calibration and balancing procedures remain to be defined.

Primary endpoint candidate: The proportion of task trials with errors. Error coding, the denominator, handling of incomplete trials and the estimand require approval before recruitment. Time to correct completion remains a proposed secondary endpoint.

Secondary outcomes: NASA-TLX ratings, workload-estimation performance against independent reference labels, adaptation latency, frame rate, energy consumption and oculomotor measures.

For acquisition settings, ethics, missing data, exclusions and sample-size justification, see [protocol](protocol/README.md).

## 5. Analysis plan

A hierarchical model with participant-level clustering is proposed for the effect of interface condition. Prediction will be evaluated using participant-disjoint partitions. Effect sizes, uncertainty intervals and error distributions will be reported; confirmatory specifications remain subject to approval.

See [analyses](analyses/README.md) for the proposed estimand, validation partitions and reporting requirements.

## 6. Results

**No results are available.** Populate this section only from traceable recorded observations and analysis scripts. Refer to [results](results/README.md).

## 7. Discussion

To be completed after results. Discuss alternative explanations, generalizability, uncertainty, false alarms, real-world constraints and comparison with verified prior work.

## 8. Limitations

Pupil diameter is sensitive to illumination, accommodation, eyewear, fatigue and eye-tracker calibration. Within-participant learning effects may affect task performance. Facial microexpressions are not validated standalone indicators of cognitive workload.

## 9. Ethics, data and code availability

**Pending.** Provide the actual ethics decision or documented exemption, consent approach, lawful data-access terms, exact code revision and sanitized data-release strategy.

## 10. Conclusions

To be written only after the observations support a bounded conclusion.

## References

Six reference records have been added to [references.bib](references.bib) for the selective literature review. These citations do not represent a completed systematic search or empirical results from P01.
