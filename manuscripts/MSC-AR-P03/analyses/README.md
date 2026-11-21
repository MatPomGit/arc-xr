# P03 — plan analiz (przed zebraniem danych)

**Status:** planowana publikacja; hipotezy i procedury nie są jeszcze prerejestrowane. Nie przeprowadzono tutaj eksperymentów, nie ma wyników empirycznych ani zatwierdzenia komisji etycznej.

## Pytanie i efekt

Jak kontrolowane błędy okluzji i asynchronii wpływają na komfort, jakość doświadczenia i wydajność użytkowników podczas długich sesji HMD AR?

Kandydat na punkt końcowy główny: Zmiana standaryzowanej skali subiektywnego zmęczenia od wartości początkowej (konkretny instrument do uzasadnienia).

Pozostałe miary: Częstość mrugania, stabilność fiksacji, błędy zadaniowe, opóźnienie end-to-end, ocena QoE.

## Podejście statystyczne

Model mieszany z czynnikami okluzji, asynchronii, czasu i ich interakcji; do oceny prognostycznej walidacja rozdzielająca uczestników.

Kontrasty, poziom istotności, korekta wielokrotnych porównań, reguły braków danych i miary niepewności wymagają wcześniejszego ustalenia. Zweryfikować założenia modelu oraz skuteczną liczebność niezależnych jednostek. Nie traktować wielu klatek tej samej sesji jako niezależnych uczestników.

## Kontrole i odporność

Luminancja, kontrast, długość ekspozycji, pole widzenia, akomodacja–wergencja, różnice HMD i kolejność warunków; metryki okulometryczne są wskaźnikami nieswoistymi.

Oddzielić tuning/trening od oceny końcowej. Raportować zarówno efekty, jak i ich przedziały ufności, jednostki pomiaru, denominatory oraz wyniki analiz wrażliwości. Wszystkie analizy dokonane po zobaczeniu wyników oznaczyć jako eksploracyjne.

## Dostarczane pliki

Skrypt lub notebook odtwarzający analizę (do dodania po implementacji), manifest wejść i wersji, tabele wyników oraz dziennik decyzji metodologicznych. Nie deklarować uzyskanych wyników bez śladu audytowego.
