# Multimodal Cognitive-Load Estimation for Adaptive Information Density in Augmented Reality

> Draft v0.1.0 — prospective structure only; NOT SUBMITTED. No empirical results are reported.

## Abstract

**To be completed after the study.** This section must summarize the background, predefined methods, observed results with uncertainty and limitations; do not use anticipated results as if they were measured.

## 1. Introduction

Okulometria (średnica źrenicy, fiksacje, sakkady), opcjonalnie sygnały mimiczne i lekkie modele Edge AI do sterowania zagęszczeniem HUD oraz poziomem szczegółowości obiektów 3D.

Research question: Czy multimodalna estymacja obciążenia poznawczego poprawia adaptację interfejsu AR względem interfejsu statycznego i adaptacji opartej na jednej modalności?

## 2. Related work

Research has already examined the physiological adaptation of AR. Sun and Liao (2025) used a cumulative skin conductance metric to trigger rest breaks and reported reduced subsequent physiological load without demonstrating improved task performance ([DOI](https://doi.org/10.1017/dsj.2025.10040)). P01 therefore does not claim to be the first physiologically adaptive AR system.

Gonnermann-Müller et al. (2024) studied visual guidance and eye-tracking in industrial AR ([ICIS](https://aisel.aisnet.org/icis2024/humtechinter/humtechinter/18/)). Chiossi et al. (2024) analysed ERP and eye-tracking correlates of visual search in mixed reality ([DOI](https://doi.org/10.1109/TVCG.2024.3456172)). These studies motivate control of visual attention and task complexity; they do not establish the causal efficacy of the proposed three-way HUD-density comparison.

The review by Suzuki, Wild and Scanlon (2024; [DOI](https://doi.org/10.1111/jcal.12882)) documents heterogeneity in physiological cognitive-load assessment in AR. Pupillary responses are sensitive to luminance and other non-cognitive influences (Mathôt, 2018; [DOI](https://doi.org/10.5334/joc.18)). NASA-TLX is a complementary subjective instrument, not a continuous moment-to-moment ground truth (Hart and Staveland, 1988; [DOI](https://doi.org/10.1016/S0166-4115(08)62386-9)).

The proposed contribution is a controlled comparison of static, unimodally adapted and multimodally adapted AR HUD information density. Generalization of the load estimator must be assessed independently from the causal effect of adaptation on a prespecified behavioural endpoint. The [literature matrix](related_work.md) documents existing evidence, its limitations and the proposed research gap. Bibliographic identifiers appear in [references.bib](references.bib). No P01 results are reported.

## 3. Research questions and hypotheses

- H1 (proposed): Adaptacyjny interfejs wykorzystujący multimodalną estymację obciążenia ogranicza błędy zadaniowe lub subiektywne przeciążenie względem interfejsu statycznego w porównywalnych warunkach.
- H2 (proposed): Model multimodalny charakteryzuje się lepszą zdolnością generalizacji międzyosobniczej niż porównywalny model jednokanałowy przy z góry ustalonym budżecie obliczeniowym.

These hypotheses must be operationalized and preregistered, if applicable, prior to confirmatory data collection.

## 4. Materials and methods

Proposed design: Kontrolowane badanie z powtarzanymi pomiarami: HUD statyczny, adaptacja jednomodalna, adaptacja multimodalna; kolejność warunków zrównoważona. Oddzielna walidacja algorytmu i ocena wpływu interwencji na zachowanie.

Sample and setting: Dorośli użytkownicy wykonywający standaryzowane zadania wymagające selekcji informacji w AR; kryteria i liczebność do uzasadnienia analizą mocy.

Manipulated factors or comparators: Typ interfejsu, trudność zadania i gęstość informacji; rzeczywiste manipulacje należy skalibrować przed badaniem.

Primary endpoint candidate: Odsetek błędnych prób zadaniowych; ostateczna definicja błędu, mianownik i estymand wymagają zatwierdzenia przed rekrutacją. Czas poprawnego wykonania pozostaje proponowanym wynikiem dodatkowym.

Secondary outcomes: NASA-TLX, dokładność estymacji obciążenia na zewnętrznych etykietach, opóźnienie adaptacji, FPS, zużycie energii, wskaźniki okoruchowe.

For acquisition settings, ethics, missing data, exclusions and sample-size justification, see [protocol](protocol/README.md).

## 5. Analysis plan

Hierarchiczny model dla efektu warunku z uczestnikiem jako efektem losowym; osobno walidacja międzyosobnicza modelu i analiza interwencji. Raportować przedziały ufności i rozkłady błędów.

See [analyses](analyses/README.md) for the proposed estimand, validation partitions and reporting requirements.

## 6. Results

**No results are available.** Populate this section only from traceable recorded observations and analysis scripts. Refer to [results](results/README.md).

## 7. Discussion

To be completed after results. Discuss alternative explanations, generalizability, uncertainty, false alarms, real-world constraints and comparison with verified prior work.

## 8. Limitations

Oświetlenie i luminancja (pupilometria), kalibracja eye trackera, akomodacja, okulary, zmęczenie, efekt uczenia; mikroekspresje nie stanowią zweryfikowanej samodzielnej miary obciążenia.

## 9. Ethics, data and code availability

**Pending.** Provide the actual ethics decision or documented exemption, consent approach, lawful data-access terms, exact code revision and sanitized data-release strategy.

## 10. Conclusions

To be written only after the observations support a bounded conclusion.

## References

Six reference records have been added to [references.bib](references.bib) for the selective literature review. These citations do not represent a completed systematic search or empirical results from P01.
