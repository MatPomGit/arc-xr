# P05 — Autonomiczny asystent AR do weryfikacji procedur manualnych

**Proponowany tytuł angielski:** *Temporal Knowledge Graphs and Egocentric Vision–Language Models for AR Procedure Verification*

**Status:** planowana publikacja; hipotezy i procedury nie są jeszcze prerejestrowane. Nie przeprowadzono tutaj eksperymentów, nie ma wyników empirycznych ani zatwierdzenia komisji etycznej.

## Cel i wkład

Połączenie temporalnego grafu wiedzy o sekwencji czynności z egocentrycznym VLM do wykrywania pominięć i błędnych kroków procedur.

## Pytanie badawcze

Czy rozumowanie oparte na temporalnym grafie procedury zmniejsza liczbę pominiętych błędów i fałszywych alarmów względem analizy samego strumienia wideo?

## Wariant minimalny (19.11.2026)

Benchmark: jedna prosta, bezpieczna procedura montażowa. Porównać analizę bez pamięci i ze stanem kroków. Wynik: czułość wykrywania pominięć przy ustalonym limicie fałszywych alarmów. Grafy i automatyczne interwencje odłożyć.

Jest to propozycja pilotażu, a nie zatwierdzona zmiana protokołu, prerejestracja czy wynik badania. [Plan minimalny](../mvp_plan.md).

## Projekt metodologiczny

Zbiór referencyjnych przebiegów prawidłowych i nieprawidłowych procedur z anotacją kroków i czasu; offline benchmark detekcji, następnie kontrolowane badanie interwencji.

Główna grupa badana: Standaryzowane zadania montażowe o odwracalnych błędach; uczestnicy o zarejestrowanym doświadczeniu.

## Struktura

- [Szkic manuskryptu](manuscript.md)
- [Hipotezy i zmienne](hypotheses/README.md)
- [Protokół badania](protocol/README.md)
- [Eksperymenty i pomiary](experiments/README.md)
- [Plan analiz](analyses/README.md)
- [Rejestr wyników](results/README.md)
- [Plan figur](figures/README.md)
- [Bibliografia BibTeX](references.bib)

Zanim rozpocznie się zbieranie danych, należy uzupełnić i zatwierdzić protokół, uzasadnienie liczebności próby oraz dokumentację etyczną.
