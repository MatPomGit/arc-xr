# P01 — protokół badania (wersja robocza)

**Stan:** NIEZATWIERDZONY. Nie jest to prerejestracja ani zgoda etyczna.

## Cel

Czy multimodalna estymacja obciążenia poznawczego poprawia adaptację interfejsu AR względem interfejsu statycznego i adaptacji opartej na jednej modalności?

## Uczestnicy / jednostki obserwacji

Dorośli użytkownicy wykonywający standaryzowane zadania wymagające selekcji informacji w AR; kryteria i liczebność do uzasadnienia analizą mocy.

Dokładne kryteria włączenia, wyłączenia, liczebność i analizę mocy należy określić przed rekrutacją.

## Schemat i warunki

Kontrolowane badanie z powtarzanymi pomiarami: HUD statyczny, adaptacja jednomodalna, adaptacja multimodalna; kolejność warunków zrównoważona. Oddzielna walidacja algorytmu i ocena wpływu interwencji na zachowanie.

Manipulacja / porównania: Typ interfejsu, trudność zadania i gęstość informacji; rzeczywiste manipulacje należy skalibrować przed badaniem.

## Pomiar

- **Kandydat na punkt końcowy główny:** Odsetek błędów zadaniowych oraz/lub czas poprawnego wykonania (ostateczny jeden wynik główny do zamrożenia).
- **Punkty końcowe dodatkowe:** NASA-TLX, dokładność estymacji obciążenia na zewnętrznych etykietach, opóźnienie adaptacji, FPS, zużycie energii, wskaźniki okoruchowe.
- **Kontrola zakłóceń:** Oświetlenie i luminancja (pupilometria), kalibracja eye trackera, akomodacja, okulary, zmęczenie, efekt uczenia; mikroekspresje nie stanowią zweryfikowanej samodzielnej miary obciążenia.

## Przebieg i jakość danych

Zarejestrować czas próby, identyfikator sesji, parametry urządzenia, synchronizację sygnałów, jakość kalibracji i reguły odrzuceń. Zaplanować pilotaż oraz losowanie/zrównoważenie kolejności. Zabezpieczyć niezależny test końcowy i unikać strojenia analizy na jego podstawie.

## Etyka i bezpieczeństwo

Ocena etyczna i świadoma zgoda wymagają rozstrzygnięcia przed badaniem z ludźmi. Minimalizować zbieranie danych biometrycznych; rozdzielić identyfikatory od zapisów pomiarowych. Zapewnić możliwość przerwania sesji AR w razie dyskomfortu i kontrolę nad działaniami asystenta.

## Proponowane decyzje metodologiczne M2 (niezatwierdzone)

Na podstawie przeglądu M1 proponuje się poniższe definicje. Nie stanowią zamrożonego protokołu, prerejestracji ani uprawnienia do rozpoczęcia pomiarów.

- **Kandydat na pojedynczy wynik główny:** odsetek błędnych prób zadaniowych w każdym warunku. Kryterium błędu, mianownik i los prób nieukończonych wymagają wcześniejszego ustalenia. Czas poprawnego wykonania pozostaje wynikiem dodatkowym.
- **Kandydat na estymand:** średnia różnica prawdopodobieństwa błędu między adaptacją multimodalną a statycznym HUD w docelowej populacji dorosłych osób. Definicja rozkładu trudności i sposobu standaryzacji wymaga decyzji.
- **Jednostka niezależna:** uczestnik. Próby i sesje są pomiarami zagnieżdżonymi. Drugorzędne porównania obejmują adaptację jedno- i multimodalną oraz jednomodalną i statyczną; wymagają uprzedniej kontroli wielokrotnych testów.
- **Walidacja predykcji:** podział po tożsamości osoby (np. LOSO), bez przecieku klatek i sesji. Dobór hiperparametrów i kalibrację prowadzić w obrębie danych treningowych.
- **Kontrola pomiarowa:** rejestrować luminancję sceny i HUD, jakość kalibracji eye trackera, brakujące próbki, okulary, zmęczenie i kolejność warunków. Średnica źrenicy nie stanowi swoistej etykiety obciążenia.
- **Regulator i bezpieczeństwo:** z góry określić maksymalną liczbę przełączeń HUD, opóźnienie adaptacji i reguły abstencji; oddzielnie oszacować koszt obliczeniowy modeli.
- **Otwarte bramki:** analiza mocy, liczebność, decyzja etyczna lub udokumentowane zwolnienie, świadoma zgoda oraz retencja danych.

## Rejestr decyzji (do wypełnienia)

| Decyzja | Stan |
| --- | --- |
| Ostateczny punkt końcowy | DO USTALENIA |
| Liczebność i analiza mocy | DO USTALENIA |
| Kryteria wykluczeń i braków danych | DO USTALENIA |
| Etyka, zgoda i retencja | DO USTALENIA |
| Zamrożony plan analiz | DO USTALENIA |
| Ewentualny identyfikator prerejestracji | BRAK |
