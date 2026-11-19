# Mobile GazeAdaptive: mobilna gra 2D z adaptacją na podstawie spojrzenia

**Wersja:** 1.0.0  
**Data:** 2026-11-19  
**Status:** koncepcja badawcza do weryfikacji w pilotażu  
**Kontekst:** *Neuroadaptive XR and Affective Computing*; potencjalna współpraca dydaktyczno-badawcza Erasmus+ (m.in. University of Moratuwa)

## 1. Streszczenie

Projekt zakłada przygotowanie prostej gry 2D działającej w przeglądarce smartfona. Gra wykorzystuje przednią kamerę RGB do przybliżonego określania, na który **duży obszar ekranu** patrzy uczestnik, i wyświetla wskazówkę wyłącznie wtedy, gdy pojawiają się oznaki trudności z wykonaniem zadania. Najważniejsza innowacja polega na porównaniu adaptacji automatycznej z **adaptacją ostrożną**, która uwzględnia jakość pomiaru spojrzenia i może świadomie zrezygnować z interwencji.

Badanie ma być możliwe do przeprowadzenia na zwykłym telefonie, bez dodatkowego eye-trackera, EEG i gogli VR. Jest to **eksperyment nad adaptacyjnym interfejsem opartym na estymacji uwagi wzrokowej**, nie zaś bezpośredni pomiar aktywności neuronalnej ani pełny eksperyment XR. W przyszłości jego mechanizm można przenieść do środowiska XR.

## 2. Główne pytanie badawcze

**Czy uwzględnianie jakości szacowania kierunku spojrzenia podczas podejmowania decyzji o podpowiedzi poprawia użyteczność adaptacyjnej gry w porównaniu z adaptacją reagującą na każdą wykrytą trudność?**

Pytania pomocnicze:

1. Z jaką trafnością zwykła przednia kamera smartfona pozwala rozpoznawać dwa, a następnie cztery duże obszary uwagi w stabilnych warunkach?
2. Czy ograniczenie podpowiedzi do sytuacji, w których pomiar jest wiarygodny, zmniejsza liczbę interwencji bez pogorszenia wykonania zadania?
3. Jak zmieniają się wyniki w zależności od typu telefonu, oświetlenia i niewielkich przesunięć głowy lub urządzenia?

## 3. Warunki badania

Przyjmujemy, że uczestnik **leży lub półleży wygodnie na kanapie**, a telefon jest umieszczony stabilnie, w przybliżeniu na wprost twarzy. Zalecany jest odpowiednio zabezpieczony uchwyt; ręczne podtrzymywanie urządzenia może powodować ruchy i pogarszać pomiar.

| Parametr | Założenie początkowe |
|---|---|
| Urządzenie | Typowy smartfon z przednią kamerą RGB |
| Sposób dostępu | Strona HTTPS uruchamiana w przeglądarce mobilnej |
| Pozycja | Leżąca lub półleżąca, bez celowego poruszania głową |
| Odległość twarz–ekran | Wstępnie 30–40 cm; do weryfikacji |
| Orientacja | Początkowo pionowa, niezmieniana w czasie próby |
| Stabilizacja | Bezpieczny uchwyt, mocowanie albo stabilne podparcie |
| Oświetlenie | Równomierne oświetlenie twarzy, bez silnego światła za plecami |
| Kalibracja | 9 punktów ekranu |
| Walidacja | Co najmniej 5 innych punktów, niewykorzystywanych do kalibracji |
| Podział ekranu | Najpierw 2 duże regiony; 4 tylko po pozytywnej walidacji |

**Uwaga:** stabilne ułożenie pomaga utrzymać geometrię pomiaru, ale nie gwarantuje dokładności; wpływają na nią również pozycja przedniej kamery, okulary, oświetlenie, rozdzielczość obrazu oraz indywidualna anatomia twarzy.

## 4. Mechanika gry

Uczestnik widzi dwa (później ewentualnie cztery) duże obszary ekranu zawierające proste symbole. Jego zadaniem jest odnalezienie wskazanego symbolu i **zatwierdzenie wyboru dotykiem**, nie spojrzeniem. Rozdzielenie obserwacji wzroku od zatwierdzenia odpowiedzi ogranicza konsekwencje błędnej estymacji spojrzenia.

Przebieg pojedynczej próby:

1. Na ekranie wyświetla się symbol docelowy oraz plansza.
2. Uczestnik przeszukuje wzrokowo obszary.
3. Algorytm rejestruje czas szukania oraz przybliżony region spojrzenia, jeśli jakość sygnału pozwala go określić.
4. Zależnie od warunku eksperymentalnego gra może delikatnie podświetlić region zawierający cel.
5. Uczestnik zatwierdza odpowiedź dotknięciem ekranu.
6. Aplikacja zapisuje wynik, czasy, parametry jakości i informacje o interwencjach.

Wszystkie warunki korzystają z tego samego zestawu plansz (ze zrównoważoną kolejnością) i tej samej formy wskazówki. Zmieniamy **regułę jej wyświetlenia**, nie treść ani intensywność pomocy.

## 5. Trzy warunki eksperymentalne

| Warunek | Reguła |
|---|---|
| **A. Statyczny** | Brak wskazówek niezależnie od zachowania uczestnika. |
| **B. Adaptacyjny** | Gra wyświetla wskazówkę po przekroczeniu ustalonego progu trudności, np. długiego czasu szukania lub powtarzających się powrotów wzroku. |
| **C. Ostrożny** | Ten sam sygnał trudności co w B, lecz wskazówka pojawia się tylko przy wystarczającej jakości i stabilności estymacji spojrzenia. |

Na początek próg trudności i poziom jakości można określić prostymi, jawnie udokumentowanymi regułami. Nie trzeba trenować skomplikowanego modelu ML. W warunkach B i C należy użyć **dokładnie tego samego estymatora oraz tego samego detektora trudności**, aby interpretowalna była zmiana samej polityki interwencji.

Jeśli śledzenie spojrzenia okaże się niewiarygodne, uczestnik może kontynuować grę, ale próba jest oznaczana jako niespełniająca kryteriów pomiarowych. Dopuszczalny jest też tryb zapasowy wykorzystujący sam czas odpowiedzi; wyniki tego trybu trzeba analizować oddzielnie.

## 6. Hipotezy

- **H1:** Wariant ostrożny (C) generuje mniej podpowiedzi niż zwykła adaptacja (B).
- **H2:** Wariant ostrożny (C) pozwala utrzymać porównywalną skuteczność wykonania zadania przy mniejszej liczbie interwencji. Formalne twierdzenie o niegorszości wymaga z góry ustalonego marginesu i odpowiedniej analizy mocy.
- **H3:** Jakość klasyfikacji regionów spojrzenia obniża się przy większych zmianach położenia głowy i telefonu oraz przy niekorzystnym oświetleniu.

Hipotezy dotyczą zachowania i adaptacji interfejsu. **Nie wolno na ich podstawie automatycznie wnioskować o konkretnych emocjach, poziomie stresu lub przeciążeniu neuronalnym.**

## 7. Pomiar i kryteria jakości

Podstawowe wskaźniki:

- trafność klasyfikacji regionu na punktach walidacyjnych (oddzielnie dla dwóch i czterech obszarów);
- błąd przestrzenny estymacji, jeśli model zwraca współrzędne (np. w cm po uwzględnieniu wielkości ekranu);
- odsetek brakujących lub odrzuconych próbek oraz stabilność pomiaru;
- opóźnienie wyznaczania predykcji i rzeczywista częstotliwość przetwarzania;
- czas i poprawność odpowiedzi;
- liczba podpowiedzi oraz liczba prób, w których adaptacja została wstrzymana;
- krótka subiektywna ocena trudności i użyteczności po bloku.

Jako **roboczy próg inżynierski** można przyjąć co najmniej 85% poprawnej klasyfikacji regionu na danych walidacyjnych. Nie jest to potwierdzony standard naukowy ani gwarancja poprawności adaptacji; próg należy skorygować na podstawie pilotażu oraz kosztu pomyłek. Przy dwóch równych regionach punkt odniesienia dla klasyfikacji losowej wynosi 50%, a przy czterech 25%, o ile klasy są zrównoważone.

Ważne, by walidacja obejmowała także punkty blisko granic regionów. Podczas krótkiego badania można wykonać ponowną walidację w środku i na końcu sesji, aby oszacować dryft kalibracji.

## 8. Minimalny plan badawczy

### Etap I. Wykonalność techniczna

Przygotować mobilną stronę umożliwiającą zgodę na kamerę, kalibrację 9-punktową, walidację na osobnych punktach i zapis podstawowych statystyk pomiarowych. Na tym etapie **nie jest potrzebna gra ani moduł adaptacji**.

Pilotaż: orientacyjnie 10–15 ochotników z różnymi smartfonami. Sprawdzić osobno Android i iOS, a także różne oświetlenie i drobne przesunięcia telefonu. Ocenić, czy dwa regiony są rozpoznawane wystarczająco wiarygodnie. Cztery regiony rozważyć dopiero wtedy, gdy pomiary to uzasadnią.

### Etap II. Gra i polityki adaptacji

Wdrożyć prostą grę 2D z wyborem dotykowym oraz trzema warunkami A/B/C. Każdy uczestnik przechodzi wszystkie warunki, a ich kolejność jest równoważona. W każdym warunku powinny wystąpić porównywalne zadania i poziomy trudności. Wstępnie można rozważyć po około 20 prób na warunek, a liczbę skorygować po pilotażu.

### Etap III. Walidacja naukowa

Przeanalizować wyniki z uwzględnieniem różnic indywidualnych i zróżnicowania urządzeń. Podstawowa analiza może wykorzystać modele mieszane dla czasu odpowiedzi, poprawności i liczby podpowiedzi. Liczebność głównego badania określić na podstawie analizy mocy lub precyzji szacowania; 10–15 osób z pilotażu nie wystarcza do potwierdzenia efektów.

## 9. Architektura techniczna

- **Frontend:** TypeScript, HTML/CSS, Canvas lub SVG, responsywny układ pionowy.
- **Kamera:** przeglądarkowe `getUserMedia()` przez HTTPS, po zgodzie użytkownika.
- **Detekcja cech twarzy:** np. MediaPipe Face Landmarker, o ile wydajność i kompatybilność mobilna są wystarczające.
- **Estymacja punktu spojrzenia:** dodatkowy model mapujący cechy oka i twarzy na ekran, wymagający indywidualnej kalibracji; **MediaPipe Face Landmarker sam nie dostarcza skalibrowanego punktu spojrzenia na ekranie**.
- **Adaptacja:** proste reguły zależne od trudności zadania i jakości pomiaru.
- **Dane:** zdarzenia i zagregowane parametry w CSV/JSON; bez domyślnego zapisywania filmu z twarzą.
- **Dystrybucja:** witryna HTTPS; docelowo aplikacja PWA, jeśli testy zgodności przeglądarek to uzasadnią.

Weryfikacja działania musi objąć zarówno Androida, jak i iOS. **Dobre parametry aparatu fotograficznego nie oznaczają automatycznie dokładnej okulografii**: decydują również geometria kamery względem ekranu, przetwarzanie obrazu, jakość modelu, kalibracja i stabilność pozycji.

## 10. Ochrona danych i etyka

Obraz twarzy powinien być przetwarzany lokalnie na urządzeniu, o ile pozwala na to architektura. Do zbioru badawczego trafiają tylko niezbędne wskaźniki, zdarzenia gry oraz jawnie zadeklarowane informacje o urządzeniu i warunkach pomiaru. Uczestnik musi udzielić świadomej zgody na korzystanie z kamery i przetwarzanie danych. Przed badaniami z udziałem ludzi należy sprawdzić wymogi komisji etycznej oraz RODO, szczególnie przy planowanej współpracy międzynarodowej.

W pozycji leżącej telefon powinien znajdować się w **bezpiecznym mocowaniu**, które nie grozi upadkiem urządzenia na twarz uczestnika.

## 11. Zakres projektu i możliwe rozszerzenia

**Wersja minimalna:** jeden ekran gry, dwa duże obszary, kalibracja, trzy proste reguły adaptacji, lokalny eksport danych i pilotaż na różnych telefonach.

**Nie włączamy na początku:** EEG, klasyfikacji konkretnych emocji, awatarów AI, rozbudowanego uczenia maszynowego, VR, szczegółowego pomiaru sakkad ani analizy międzykulturowej. Każdy z tych tematów można rozważyć później.

**Potencjalny kolejny krok:** porównawcze badanie online w Polsce i na Sri Lance, po sprawdzeniu zgodności procedury, aparatury, zgód i zasad przetwarzania danych. Mechanizm ostrożnej adaptacji może w dalszej perspektywie stanowić komponent interfejsów XR.

## 12. Robocze tytuły

- **Projekt:** *Mobile GazeAdaptive: A Smartphone Webcam-Based Adaptive Attention Game*.
- **Artykuł metodologiczny:** *Can Smartphone Cameras Support Reliable Region-Level Gaze Tracking in Mobile Browser Experiments?*
- **Artykuł eksperymentalny:** *When Should an Adaptive Interface Intervene? Quality-Aware Gaze Adaptation in a Mobile Visual Search Game*.

## 13. Najbliższy krok

**Najpierw zbudować wyłącznie test kalibracji i walidacji wzroku na smartfonie.** Decyzja o konstrukcji gry z dwoma lub czterema obszarami oraz o sposobie uruchamiania podpowiedzi powinna wynikać z rzeczywistych wyników tego testu, a nie z deklarowanej rozdzielczości kamer.
