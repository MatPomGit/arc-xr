# Temporal Knowledge Graphs and Egocentric Vision–Language Models for AR Procedure Verification

> Draft v0.1.0 — prospective structure only; NOT SUBMITTED. No empirical results are reported.

## Abstract

**To be completed after the study.** This section must summarize the background, predefined methods, observed results with uncertainty and limitations; do not use anticipated results as if they were measured.

## 1. Introduction

Połączenie temporalnego grafu wiedzy o sekwencji czynności z egocentrycznym VLM do wykrywania pominięć i błędnych kroków procedur.

Research question: Czy rozumowanie oparte na temporalnym grafie procedury zmniejsza liczbę pominiętych błędów i fałszywych alarmów względem analizy samego strumienia wideo?

## 2. Related work

A structured comparison of primary literature, available benchmarks and the specific research gap is required. All citations must be verified against original publications; `references.bib` has intentionally not been populated with invented entries.

## 3. Research questions and hypotheses

- H1 (proposed): Model VLM z temporalnym grafem stanu procedury skuteczniej identyfikuje pominięte kroki niż VLM bez jawnego modelu sekwencji.
- H2 (proposed): Wizualne wskazówki AR wyzwalane po potwierdzeniu błędu poprawiają odsetek poprawnych korekt względem informacji wyłącznie tekstowej.

These hypotheses must be operationalized and preregistered, if applicable, prior to confirmatory data collection.

## 4. Materials and methods

Proposed design: Zbiór referencyjnych przebiegów prawidłowych i nieprawidłowych procedur z anotacją kroków i czasu; offline benchmark detekcji, następnie kontrolowane badanie interwencji.

Sample and setting: Standaryzowane zadania montażowe o odwracalnych błędach; uczestnicy o zarejestrowanym doświadczeniu.

Manipulated factors or comparators: Model procedury (brak grafu/graf temporalny) oraz sposób komunikatu (tekst/wizualna wskazówka AR).

Primary endpoint candidate: Czułość wykrywania pominiętych kroków przy zadanym limicie fałszywych alarmów na procedurę.

Secondary outcomes: Opóźnienie detekcji, F1 błędów, czas korekty, błędy po korekcie, dostępność śladu decyzyjnego.

For acquisition settings, ethics, missing data, exclusions and sample-size justification, see [protocol](protocol/README.md).

## 5. Analysis plan

Podział danych według uczestnika, sesji i procedury; analiza metryk zdarzeniowych, a nie tylko klas klatkowych; przedziały ufności klastrowane po sesji.

See [analyses](analyses/README.md) for the proposed estimand, validation partitions and reporting requirements.

## 6. Results

**No results are available.** Populate this section only from traceable recorded observations and analysis scripts. Refer to [results](results/README.md).

## 7. Discussion

To be completed after results. Discuss alternative explanations, generalizability, uncertainty, false alarms, real-world constraints and comparison with verified prior work.

## 8. Limitations

Niejednoznaczne granice kroków, brak widoczności dłoni, częściowa obserwowalność stanu, opóźnienia inferencji i błędne ostrzeżenia generowane przez VLM.

## 9. Ethics, data and code availability

**Pending.** Provide the actual ethics decision or documented exemption, consent approach, lawful data-access terms, exact code revision and sanitized data-release strategy.

## 10. Conclusions

To be written only after the observations support a bounded conclusion.

## References

Bibliographic entries will be curated in [references.bib](references.bib).
