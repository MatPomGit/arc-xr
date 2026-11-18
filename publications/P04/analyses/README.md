# P04 — plan analiz (przed zebraniem danych)

**Status:** planowana publikacja; hipotezy i procedury nie są jeszcze prerejestrowane. Nie przeprowadzono tutaj eksperymentów, nie ma wyników empirycznych ani zatwierdzenia komisji etycznej.

## Pytanie i efekt

Czy integracja VLM z geometrią 3D ogranicza błędy wskazania obiektu referencyjnego i pozycjonowania wskazówek AR względem podejścia wyłącznie obrazowego?

Kandydat na punkt końcowy główny: Odsetek poprawnie rozstrzygniętych referencji oraz błąd położenia wskazówki w centymetrach (wybrać metrykę główną przed testem).

Pozostałe miary: Błąd kątowy, skuteczność abstencji, czas inferencji, opóźnienie kotwiczenia, stabilność śledzenia.

## Podejście statystyczne

Grupowanie wyników według sceny i przedmiotu, ocena na niewidzianych scenach; bootstrap klastrowy oraz analizowanie kalibracji niepewności.

Kontrasty, poziom istotności, korekta wielokrotnych porównań, reguły braków danych i miary niepewności wymagają wcześniejszego ustalenia. Zweryfikować założenia modelu oraz skuteczną liczebność niezależnych jednostek. Nie traktować wielu klatek tej samej sesji jako niezależnych uczestników.

## Kontrole i odporność

Niedokładna kalibracja kamera–głębia–świat, dryf kotwic AR, zasłanianie obiektów, niejednoznaczność języka i błąd niezależnej referencji.

Oddzielić tuning/trening od oceny końcowej. Raportować zarówno efekty, jak i ich przedziały ufności, jednostki pomiaru, denominatory oraz wyniki analiz wrażliwości. Wszystkie analizy dokonane po zobaczeniu wyników oznaczyć jako eksploracyjne.

## Dostarczane pliki

Skrypt lub notebook odtwarzający analizę (do dodania po implementacji), manifest wejść i wersji, tabele wyników oraz dziennik decyzji metodologicznych. Nie deklarować uzyskanych wyników bez śladu audytowego.
