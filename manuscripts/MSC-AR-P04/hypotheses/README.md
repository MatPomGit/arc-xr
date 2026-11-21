# P04 — hipotezy i operacjonalizacja

**Status:** planowana publikacja; hipotezy i procedury nie są jeszcze prerejestrowane. Nie przeprowadzono tutaj eksperymentów, nie ma wyników empirycznych ani zatwierdzenia komisji etycznej.

## H1 (robocza)

Wykorzystanie głębi i jawnych transformacji układów współrzędnych ogranicza błąd lokalizacji wskazań 3D dla komend precyzyjnych względem modelu tylko 2D.

## H2 (robocza)

Polityka wstrzymania wskazówki przy niejednoznaczności zmniejsza liczbę błędnych, pewnych rekomendacji kosztem częściowej abstencji.

## Pytanie główne i pomiar

Czy integracja VLM z geometrią 3D ogranicza błędy wskazania obiektu referencyjnego i pozycjonowania wskazówek AR względem podejścia wyłącznie obrazowego?

Planowany główny punkt końcowy: Odsetek poprawnie rozstrzygniętych referencji oraz błąd położenia wskazówki w centymetrach (wybrać metrykę główną przed testem).

Dodatkowe punkty końcowe: Błąd kątowy, skuteczność abstencji, czas inferencji, opóźnienie kotwiczenia, stabilność śledzenia.

## Warunki zamrożenia hipotez

Przed zbieraniem danych należy wskazać jednostkę analizy (osoba, sesja, scena lub próba), kierunek kontrastu, efekt minimalnie istotny, regułę odrzucenia hipotezy zerowej i sposób kontroli wielokrotnego testowania. W protokole należy odróżnić hipotezy potwierdzające od analiz eksploracyjnych. Nie utożsamiać korelacji pomiaru fizjologicznego z przyczynowym wpływem interwencji.
