# P04 — Grounding przestrzenny 3D modeli VLM w zadaniach manipulacyjnych AR

**Proponowany tytuł angielski:** *Depth-Aware 3D Spatial Grounding of Vision–Language Instructions for Precise AR Manipulation*

**Status:** planowana publikacja; hipotezy i procedury nie są jeszcze prerejestrowane. Nie przeprowadzono tutaj eksperymentów, nie ma wyników empirycznych ani zatwierdzenia komisji etycznej.

## Cel i wkład

Mapowanie instrukcji języka naturalnego na obiekty i współrzędne 3D na podstawie obrazów, głębi i chmur punktów z jawną kontrolą niepewności.

## Pytanie badawcze

Czy integracja VLM z geometrią 3D ogranicza błędy wskazania obiektu referencyjnego i pozycjonowania wskazówek AR względem podejścia wyłącznie obrazowego?

## Wariant minimalny (19.11.2026)

Benchmark: ten sam VLM na obrazie 2D i z jawną geometrią 3D. Wynik: poprawność wskazań obiektów na niewidzianych scenach. Korzystać ze skalibrowanej referencji bez zakładania surowej mapy głębi Quest 3.

Jest to propozycja pilotażu, a nie zatwierdzona zmiana protokołu, prerejestracja czy wynik badania. [Plan minimalny](../mvp_plan.md).

## Projekt metodologiczny

Benchmark scen z kontrolowaną geometrią i zestawem niejednoznacznych instrukcji; bazowe VLM 2D, VLM + głębia oraz model z mechanizmem abstencji.

Główna grupa badana: Zestaw obiektów i scen montażowych z niezależną referencją geometryczną; ocena użytkowników możliwa jako odrębny etap.

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
