# Depth-Aware 3D Spatial Grounding of Vision–Language Instructions for Precise AR Manipulation

> Draft v0.1.0 — prospective structure only; NOT SUBMITTED. No empirical results are reported.

## Abstract

**To be completed after the study.** This section must summarize the background, predefined methods, observed results with uncertainty and limitations; do not use anticipated results as if they were measured.

## 1. Introduction

Mapowanie instrukcji języka naturalnego na obiekty i współrzędne 3D na podstawie obrazów, głębi i chmur punktów z jawną kontrolą niepewności.

Research question: Czy integracja VLM z geometrią 3D ogranicza błędy wskazania obiektu referencyjnego i pozycjonowania wskazówek AR względem podejścia wyłącznie obrazowego?

## 2. Related work

A structured comparison of primary literature, available benchmarks and the specific research gap is required. All citations must be verified against original publications; `references.bib` has intentionally not been populated with invented entries.

## 3. Research questions and hypotheses

- H1 (proposed): Wykorzystanie głębi i jawnych transformacji układów współrzędnych ogranicza błąd lokalizacji wskazań 3D dla komend precyzyjnych względem modelu tylko 2D.
- H2 (proposed): Polityka wstrzymania wskazówki przy niejednoznaczności zmniejsza liczbę błędnych, pewnych rekomendacji kosztem częściowej abstencji.

These hypotheses must be operationalized and preregistered, if applicable, prior to confirmatory data collection.

## 4. Materials and methods

Proposed design: Benchmark scen z kontrolowaną geometrią i zestawem niejednoznacznych instrukcji; bazowe VLM 2D, VLM + głębia oraz model z mechanizmem abstencji.

Sample and setting: Zestaw obiektów i scen montażowych z niezależną referencją geometryczną; ocena użytkowników możliwa jako odrębny etap.

Manipulated factors or comparators: Reprezentacja przestrzenna, poziom niejednoznaczności instrukcji oraz rodzaj zakłóceń sensora.

Primary endpoint candidate: Odsetek poprawnie rozstrzygniętych referencji oraz błąd położenia wskazówki w centymetrach (wybrać metrykę główną przed testem).

Secondary outcomes: Błąd kątowy, skuteczność abstencji, czas inferencji, opóźnienie kotwiczenia, stabilność śledzenia.

For acquisition settings, ethics, missing data, exclusions and sample-size justification, see [protocol](protocol/README.md).

## 5. Analysis plan

Grupowanie wyników według sceny i przedmiotu, ocena na niewidzianych scenach; bootstrap klastrowy oraz analizowanie kalibracji niepewności.

See [analyses](analyses/README.md) for the proposed estimand, validation partitions and reporting requirements.

## 6. Results

**No results are available.** Populate this section only from traceable recorded observations and analysis scripts. Refer to [results](results/README.md).

## 7. Discussion

To be completed after results. Discuss alternative explanations, generalizability, uncertainty, false alarms, real-world constraints and comparison with verified prior work.

## 8. Limitations

Niedokładna kalibracja kamera–głębia–świat, dryf kotwic AR, zasłanianie obiektów, niejednoznaczność języka i błąd niezależnej referencji.

## 9. Ethics, data and code availability

**Pending.** Provide the actual ethics decision or documented exemption, consent approach, lawful data-access terms, exact code revision and sanitized data-release strategy.

## 10. Conclusions

To be written only after the observations support a bounded conclusion.

## References

Bibliographic entries will be curated in [references.bib](references.bib).
