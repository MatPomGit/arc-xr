# Multimodal Cognitive-Load Estimation for Adaptive Information Density in Augmented Reality

> Draft v0.1.0 — prospective structure only; NOT SUBMITTED. No empirical results are reported.

## Abstract

**To be completed after the study.** This section must summarize the background, predefined methods, observed results with uncertainty and limitations; do not use anticipated results as if they were measured.

## 1. Introduction

Okulometria (średnica źrenicy, fiksacje, sakkady), opcjonalnie sygnały mimiczne i lekkie modele Edge AI do sterowania zagęszczeniem HUD oraz poziomem szczegółowości obiektów 3D.

Research question: Czy multimodalna estymacja obciążenia poznawczego poprawia adaptację interfejsu AR względem interfejsu statycznego i adaptacji opartej na jednej modalności?

## 2. Related work

A structured comparison of primary literature, available benchmarks and the specific research gap is required. All citations must be verified against original publications; `references.bib` has intentionally not been populated with invented entries.

## 3. Research questions and hypotheses

- H1 (proposed): Adaptacyjny interfejs wykorzystujący multimodalną estymację obciążenia ogranicza błędy zadaniowe lub subiektywne przeciążenie względem interfejsu statycznego w porównywalnych warunkach.
- H2 (proposed): Model multimodalny charakteryzuje się lepszą zdolnością generalizacji międzyosobniczej niż porównywalny model jednokanałowy przy z góry ustalonym budżecie obliczeniowym.

These hypotheses must be operationalized and preregistered, if applicable, prior to confirmatory data collection.

## 4. Materials and methods

Proposed design: Kontrolowane badanie z powtarzanymi pomiarami: HUD statyczny, adaptacja jednomodalna, adaptacja multimodalna; kolejność warunków zrównoważona. Oddzielna walidacja algorytmu i ocena wpływu interwencji na zachowanie.

Sample and setting: Dorośli użytkownicy wykonywający standaryzowane zadania wymagające selekcji informacji w AR; kryteria i liczebność do uzasadnienia analizą mocy.

Manipulated factors or comparators: Typ interfejsu, trudność zadania i gęstość informacji; rzeczywiste manipulacje należy skalibrować przed badaniem.

Primary endpoint candidate: Odsetek błędów zadaniowych oraz/lub czas poprawnego wykonania (ostateczny jeden wynik główny do zamrożenia).

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

Bibliographic entries will be curated in [references.bib](references.bib).
