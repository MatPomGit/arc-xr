# P01 — Multimodalna ocena obciążenia poznawczego i adaptacja interfejsu AR

**Proponowany tytuł angielski:** *Multimodal Cognitive-Load Estimation for Adaptive Information Density in Augmented Reality*

**Status:** planowana publikacja; hipotezy i procedury nie są jeszcze prerejestrowane. Nie przeprowadzono tutaj eksperymentów, nie ma wyników empirycznych ani zatwierdzenia komisji etycznej.

## Cel i wkład

Okulometria (średnica źrenicy, fiksacje, sakkady), opcjonalnie sygnały mimiczne i lekkie modele Edge AI do sterowania zagęszczeniem HUD oraz poziomem szczegółowości obiektów 3D.

## Pytanie badawcze

Czy multimodalna estymacja obciążenia poznawczego poprawia adaptację interfejsu AR względem interfejsu statycznego i adaptacji opartej na jednej modalności?

## Wariant minimalny (19.11.2026)

Pilotaż: statyczny HUD kontra HUD sterowany prostą regułą zachowania. Wynik: odsetek błędnych prób. To nie test hipotez multimodalnych H1/H2, które wymagają osobnego badania. Standardowy Quest 3 nie śledzi wzroku; Tobii Eye Tracker 5 mierzy przy monitorze, a nie w Quest 3.

Jest to propozycja pilotażu, a nie zatwierdzona zmiana protokołu, prerejestracja czy wynik badania. [Plan minimalny](../mvp_plan.md).

## Projekt metodologiczny

Kontrolowane badanie z powtarzanymi pomiarami: HUD statyczny, adaptacja jednomodalna, adaptacja multimodalna; kolejność warunków zrównoważona. Oddzielna walidacja algorytmu i ocena wpływu interwencji na zachowanie.

Główna grupa badana: Dorośli użytkownicy wykonywający standaryzowane zadania wymagające selekcji informacji w AR; kryteria i liczebność do uzasadnienia analizą mocy.

## Struktura

- [Szkic manuskryptu](manuscript.md)
- [Przegląd literatury i granice nowości](related_work.md)
- [Hipotezy i zmienne](hypotheses/README.md)
- [Protokół badania](protocol/README.md)
- [Eksperymenty i pomiary](experiments/README.md)
- [Plan analiz](analyses/README.md)
- [Rejestr wyników](results/README.md)
- [Plan figur](figures/README.md)
- [Bibliografia BibTeX](references.bib)

Zanim rozpocznie się zbieranie danych, należy uzupełnić i zatwierdzić protokół, uzasadnienie liczebności próby oraz dokumentację etyczną.

## Manuskrypt w LaTeX

[Równoległe źródło artykułu (main.tex)](main.tex) jest samodzielnym szkicem naukowym. Dotychczasowe protokoły i rozbudowany tekst Markdown zachowują swoją rolę dokumentacji badania.
