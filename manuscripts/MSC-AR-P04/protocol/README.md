# P04 — protokół badania (wersja robocza)

**Stan:** NIEZATWIERDZONY. Nie jest to prerejestracja ani zgoda etyczna.

## Cel

Czy integracja VLM z geometrią 3D ogranicza błędy wskazania obiektu referencyjnego i pozycjonowania wskazówek AR względem podejścia wyłącznie obrazowego?

## Uczestnicy / jednostki obserwacji

Zestaw obiektów i scen montażowych z niezależną referencją geometryczną; ocena użytkowników możliwa jako odrębny etap.

Dokładne kryteria włączenia, wyłączenia, liczebność i analizę mocy należy określić przed rekrutacją.

## Schemat i warunki

Benchmark scen z kontrolowaną geometrią i zestawem niejednoznacznych instrukcji; bazowe VLM 2D, VLM + głębia oraz model z mechanizmem abstencji.

Manipulacja / porównania: Reprezentacja przestrzenna, poziom niejednoznaczności instrukcji oraz rodzaj zakłóceń sensora.

## Pomiar

- **Kandydat na punkt końcowy główny:** Odsetek poprawnie rozstrzygniętych referencji oraz błąd położenia wskazówki w centymetrach (wybrać metrykę główną przed testem).
- **Punkty końcowe dodatkowe:** Błąd kątowy, skuteczność abstencji, czas inferencji, opóźnienie kotwiczenia, stabilność śledzenia.
- **Kontrola zakłóceń:** Niedokładna kalibracja kamera–głębia–świat, dryf kotwic AR, zasłanianie obiektów, niejednoznaczność języka i błąd niezależnej referencji.

## Przebieg i jakość danych

Zarejestrować czas próby, identyfikator sesji, parametry urządzenia, synchronizację sygnałów, jakość kalibracji i reguły odrzuceń. Zaplanować pilotaż oraz losowanie/zrównoważenie kolejności. Zabezpieczyć niezależny test końcowy i unikać strojenia analizy na jego podstawie.

## Etyka i bezpieczeństwo

Ocena etyczna i świadoma zgoda wymagają rozstrzygnięcia przed badaniem z ludźmi. Minimalizować zbieranie danych biometrycznych; rozdzielić identyfikatory od zapisów pomiarowych. Zapewnić możliwość przerwania sesji AR w razie dyskomfortu i kontrolę nad działaniami asystenta.

## Rejestr decyzji (do wypełnienia)

| Decyzja | Stan |
| --- | --- |
| Ostateczny punkt końcowy | DO USTALENIA |
| Liczebność i analiza mocy | DO USTALENIA |
| Kryteria wykluczeń i braków danych | DO USTALENIA |
| Etyka, zgoda i retencja | DO USTALENIA |
| Zamrożony plan analiz | DO USTALENIA |
| Ewentualny identyfikator prerejestracji | BRAK |
