# P02 — plan analiz (przed zebraniem danych)

**Status:** planowana publikacja; hipotezy i procedury nie są jeszcze prerejestrowane. Nie przeprowadzono tutaj eksperymentów, nie ma wyników empirycznych ani zatwierdzenia komisji etycznej.

## Pytanie i efekt

Czy personalizacja i uczenie ciągłe poprawiają rozpoznawanie deklarowanej frustracji oraz skuteczność wspierających mikrointerwencji AR?

Kandydat na punkt końcowy główny: Jakość predykcji względem niezależnych samoopisowych etykiet frustracji na przyszłych sesjach (metryka pierwotna do wskazania).

Pozostałe miary: Fałszywe alerty na godzinę, błąd wykonania, czas ukończenia, kalibracja modelu, zapominanie katastroficzne i akceptowalność wsparcia.

## Podejście statystyczne

Walidacja chronologiczna w obrębie osoby i test na nowych osobach; porównania sparowane i analiza zmian między sesjami. Separować jakość detekcji od efektu interwencji.

Kontrasty, poziom istotności, korekta wielokrotnych porównań, reguły braków danych i miary niepewności wymagają wcześniejszego ustalenia. Zweryfikować założenia modelu oraz skuteczną liczebność niezależnych jednostek. Nie traktować wielu klatek tej samej sesji jako niezależnych uczestników.

## Kontrole i odporność

Frustracja nie jest tożsama z koncentracją, błędem manualnym ani rozpoznaniem klinicznym; ryzyko stronniczych etykiet, dryfu, przecieku danych czasowych i nadmiernej ingerencji w zadanie.

Oddzielić tuning/trening od oceny końcowej. Raportować zarówno efekty, jak i ich przedziały ufności, jednostki pomiaru, denominatory oraz wyniki analiz wrażliwości. Wszystkie analizy dokonane po zobaczeniu wyników oznaczyć jako eksploracyjne.

## Dostarczane pliki

Skrypt lub notebook odtwarzający analizę (do dodania po implementacji), manifest wejść i wersji, tabele wyników oraz dziennik decyzji metodologicznych. Nie deklarować uzyskanych wyników bez śladu audytowego.
