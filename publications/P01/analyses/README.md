# P01 — plan analiz (przed zebraniem danych)

**Status:** planowana publikacja; hipotezy i procedury nie są jeszcze prerejestrowane. Nie przeprowadzono tutaj eksperymentów, nie ma wyników empirycznych ani zatwierdzenia komisji etycznej.

## Pytanie i efekt

Czy multimodalna estymacja obciążenia poznawczego poprawia adaptację interfejsu AR względem interfejsu statycznego i adaptacji opartej na jednej modalności?

Kandydat na punkt końcowy główny: Odsetek błędów zadaniowych oraz/lub czas poprawnego wykonania (ostateczny jeden wynik główny do zamrożenia).

Pozostałe miary: NASA-TLX, dokładność estymacji obciążenia na zewnętrznych etykietach, opóźnienie adaptacji, FPS, zużycie energii, wskaźniki okoruchowe.

## Podejście statystyczne

Hierarchiczny model dla efektu warunku z uczestnikiem jako efektem losowym; osobno walidacja międzyosobnicza modelu i analiza interwencji. Raportować przedziały ufności i rozkłady błędów.

Kontrasty, poziom istotności, korekta wielokrotnych porównań, reguły braków danych i miary niepewności wymagają wcześniejszego ustalenia. Zweryfikować założenia modelu oraz skuteczną liczebność niezależnych jednostek. Nie traktować wielu klatek tej samej sesji jako niezależnych uczestników.

## Kontrole i odporność

Oświetlenie i luminancja (pupilometria), kalibracja eye trackera, akomodacja, okulary, zmęczenie, efekt uczenia; mikroekspresje nie stanowią zweryfikowanej samodzielnej miary obciążenia.

Oddzielić tuning/trening od oceny końcowej. Raportować zarówno efekty, jak i ich przedziały ufności, jednostki pomiaru, denominatory oraz wyniki analiz wrażliwości. Wszystkie analizy dokonane po zobaczeniu wyników oznaczyć jako eksploracyjne.

## Dostarczane pliki

Skrypt lub notebook odtwarzający analizę (do dodania po implementacji), manifest wejść i wersji, tabele wyników oraz dziennik decyzji metodologicznych. Nie deklarować uzyskanych wyników bez śladu audytowego.
