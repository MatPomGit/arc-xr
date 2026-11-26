# Statistical reporting policy

This policy complements docs/core_statistical_analysis_plan.md. The study-specific SAP remains authoritative for estimands and model choices.

## General rules
- Report effect estimates and uncertainty, not only p-values.
- Distinguish preregistered confirmatory, prespecified secondary and exploratory analyses.
- Preserve the unit of analysis and dependence structure.
- Do not convert right-censored recovery events into ordinary maximum times.
- Report exclusions, missingness and technical invalidity by group/condition where applicable.
- Distinguish scientific missingness from telemetry failure and protocol invalidity.
- State multiplicity handling for every family of confirmatory tests.
- Report prespecified sensitivity analyses without selecting the most favorable result.

## Device heterogeneity
BYOD effects are modeled or stratified when prespecified and empirically justified. Unsupported devices are technical exclusions, not outcome-driven exclusions.

## Optional modules
Facial, bilateral-audio, AR/embodied and EEG analyses have independent hypotheses and evidence gates. They may not be used post hoc to rescue a failed core primary endpoint.

## Exploratory analyses
Exploratory analyses are welcome when clearly labeled and separated from preregistered conclusions. New hypotheses generated after outcome inspection become future confirmatory hypotheses, not retrospectively confirmed ones.
