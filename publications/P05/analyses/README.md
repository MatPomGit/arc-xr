# P05 — plan analiz (przed zebraniem danych)

**Status:** planowana publikacja; hipotezy i procedury nie są jeszcze prerejestrowane. Nie przeprowadzono tutaj eksperymentów, nie ma wyników empirycznych ani zatwierdzenia komisji etycznej.

## Pytanie i efekt

Czy rozumowanie oparte na temporalnym grafie procedury zmniejsza liczbę pominiętych błędów i fałszywych alarmów względem analizy samego strumienia wideo?

Kandydat na punkt końcowy główny: Czułość wykrywania pominiętych kroków przy zadanym limicie fałszywych alarmów na procedurę.

Pozostałe miary: Opóźnienie detekcji, F1 błędów, czas korekty, błędy po korekcie, dostępność śladu decyzyjnego.

## Podejście statystyczne

Podział danych według uczestnika, sesji i procedury; analiza metryk zdarzeniowych, a nie tylko klas klatkowych; przedziały ufności klastrowane po sesji.

Kontrasty, poziom istotności, korekta wielokrotnych porównań, reguły braków danych i miary niepewności wymagają wcześniejszego ustalenia. Zweryfikować założenia modelu oraz skuteczną liczebność niezależnych jednostek. Nie traktować wielu klatek tej samej sesji jako niezależnych uczestników.

## Kontrole i odporność

Niejednoznaczne granice kroków, brak widoczności dłoni, częściowa obserwowalność stanu, opóźnienia inferencji i błędne ostrzeżenia generowane przez VLM.

Oddzielić tuning/trening od oceny końcowej. Raportować zarówno efekty, jak i ich przedziały ufności, jednostki pomiaru, denominatory oraz wyniki analiz wrażliwości. Wszystkie analizy dokonane po zobaczeniu wyników oznaczyć jako eksploracyjne.

## Dostarczane pliki

Skrypt lub notebook odtwarzający analizę (do dodania po implementacji), manifest wejść i wersji, tabele wyników oraz dziennik decyzji metodologicznych. Nie deklarować uzyskanych wyników bez śladu audytowego.
