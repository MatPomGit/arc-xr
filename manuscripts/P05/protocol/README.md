# P05 — protokół badania (wersja robocza)

**Stan:** NIEZATWIERDZONY. Nie jest to prerejestracja ani zgoda etyczna.

## Cel

Czy rozumowanie oparte na temporalnym grafie procedury zmniejsza liczbę pominiętych błędów i fałszywych alarmów względem analizy samego strumienia wideo?

## Uczestnicy / jednostki obserwacji

Standaryzowane zadania montażowe o odwracalnych błędach; uczestnicy o zarejestrowanym doświadczeniu.

Dokładne kryteria włączenia, wyłączenia, liczebność i analizę mocy należy określić przed rekrutacją.

## Schemat i warunki

Zbiór referencyjnych przebiegów prawidłowych i nieprawidłowych procedur z anotacją kroków i czasu; offline benchmark detekcji, następnie kontrolowane badanie interwencji.

Manipulacja / porównania: Model procedury (brak grafu/graf temporalny) oraz sposób komunikatu (tekst/wizualna wskazówka AR).

## Pomiar

- **Kandydat na punkt końcowy główny:** Czułość wykrywania pominiętych kroków przy zadanym limicie fałszywych alarmów na procedurę.
- **Punkty końcowe dodatkowe:** Opóźnienie detekcji, F1 błędów, czas korekty, błędy po korekcie, dostępność śladu decyzyjnego.
- **Kontrola zakłóceń:** Niejednoznaczne granice kroków, brak widoczności dłoni, częściowa obserwowalność stanu, opóźnienia inferencji i błędne ostrzeżenia generowane przez VLM.

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
