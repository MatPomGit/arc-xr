# Charakterystyka Aparatury Badawczej oraz Protokoły Eksperymentalne w Obszarze Cognitive AR i Agentów VLM

## 1. Naukowy Opis Aparatury Badawczej i Architektury Połączeń

Posiadany zestaw narzędziowy stanowi heterogeniczne, wysoce modularne środowisko eksperymentalne z zakresu interakcji człowiek–komputer (HCI), przetwarzania przestrzennego (Spatial Computing) oraz psychofizjologii stosowanej. Urządzenia dzielą się na cztery podsystemy funkcjonalne: **wizualizację (HMD)**, **jednostkę obliczeniową**, **sensorykę fizjologiczną** oraz **sensorykę behawioralno-kinematyczną**.

---

### 1.1. Podsystem Wizualizacji i Przetwarzania Przestrzennego

#### Viture Luma Ultra XR (Optical See-Through HMD)
* **Charakterystyka techniczna:** Lekkie okulary rozszerzonej rzeczywistości oparte na układzie optycznym typu *Birdbath* z ekranami Micro-OLED o wysokiej gęstości pikseli (Full HD na oko, wysoka jasność szczytowa i pokrycie barw) oraz wbudowaną elektrochromatyczną regulacją przezierności soczewek. Wyposażone w wbudowany 3-osiowy lub 6-osiowy układ inercyjny (IMU) do śledzenia orientacji głowy.
* **Możliwości pomiarowe i badawcze:** Umożliwiają prezentację wysokokontrastowych bodźców wizualnych (HUD, etykiety, obiekty 3D) bezpośrednio na tle rzeczywistego środowiska pracy bez degradacji rozdzielczości świata fizycznego (brak kamery pośredniczącej). Niska masa własna (~78 g) minimalizuje obciążenie mechaniczne odcinka szyjnego oraz eliminuje nacisk na okolice czołowe czaszki.
* **Interfejsy i łączność:** Przewodowe połączenie USB-C z obsługą standardu *DisplayPort Alt Mode* (przesył obrazu, zasilania oraz danych z sensorów IMU).

#### Meta Quest 3 (Video Pass-Through Mixed Reality HMD)
* **Charakterystyka techniczna:** Autonomiczny system rzeczywistości mieszanej napędzany układem Qualcomm Snapdragon XR2 Gen 2. Wyposażony w optykę typu *Pancake* (rozdzielczość $2064 \times 2208$ px na oko), podwójne kamery RGB o wysokiej rozdzielczości do kolorowego trybu *Video Pass-Through* (VPT), sensor głębi (projektor podczerwieni) oraz 4 kamery śledzące pozycję w przestrzeni (SLAM 6DoF).
* **Możliwości pomiarowe i badawcze:** Zapewnia pełne śledzenie translacji i rotacji w przestrzeni 3D (6DoF), mapowanie geometrii otoczenia (*Scene Understanding / Mesh*) oraz dostęp do strumieni wideo z pierwszej osoby (za pośrednictwem *Passthrough Camera API* lub strumieniowania PCVR). Umożliwia badania nad okluzją wirtualno-rzeczywistą i agentami VLM operującymi w pełnej przestrzeni pomieszczenia.
* **Interfejsy i łączność:** Wi-Fi 6E/7 (bezprzewodowa komunikacja PCVR przez Quest Link / Air Link / ALVR o niskiej latencji), USB-C 3.2 Gen 1 (przewodowy przesył danych i zasilania), Bluetooth LE (obsługa zewnętrznych peryferiów).

#### Samsung Galaxy S25 Ultra (Mobilna Jednostka Obliczeniowa i Hub Sensoryczny)
* **Charakterystyka techniczna:** Flagowa platforma mobilna oparta na układzie Snapdragon 8 Elite z dedykowanym procesorem neuronowym (NPU Hexagon) przystosowanym do akceleracji modeli AI na urządzeniu (Edge-AI), 12/16 GB pamięci RAM LPDDR5X oraz zaawansowanym zestawem kamer (w tym obiektyw ultraszerokokątny i teleobiektyw) i sensorów IMU.
* **Możliwości pomiarowe i badawcze:** Pełni funkcję mobilnego hosta dla okularów Viture Luma Ultra XR (poprzez tryb *Samsung DeX* lub dedykowane aplikacje *Android XR / OpenXR*), a także bramy komunikacyjnej (gateway) agregującej dane z sensorów Bluetooth LE i przesyłającej je przez Wi-Fi do stacji roboczej. Może również służyć jako stacjonarna lub mobilna kamera rejestrująca kontekst sceny dla modeli VLM.
* **Interfejsy i łączność:** USB-C 3.2 z obsługą DisplayPort 1.2+, Wi-Fi 7, Bluetooth 5.4, Ultra-Wideband (UWB).

---

### 1.2. Podsystem Sensoryki Neurofizjologicznej

#### Muse S Athena (Mobilny Elektroencefalograf i Fotopletyzmograf)
* **Charakterystyka techniczna:** Elastyczna, niskoprofilowa opaska neurosensoryczna wyposażona w suche, elastyczne elektrody EEG umieszczone w standardzie międzynarodowego systemu 10-20 w punktach **AF7, AF8** (płat czołowy – lewy i prawy) oraz elektrody referencyjne/skroniowe **TP9, TP10** (za uszami), wspierane przez elektrodę referencyjną Fpz. Ponadto urządzenie integruje wielodługościowy czujnik fotopletyzmograficzny (PPG) na czole oraz 3-osiowy akcelerometr i żyroskop.
* **Możliwości pomiarowe i badawcze:**
  * **EEG (częstotliwość próbkowania 256 Hz):** Rejestracja surowych potencjałów czynnościowych kory mózgowej. Umożliwia ekstrakcję gęstości widmowej mocy (PSD) w pasmach: $\delta$ ($1\text{–}4\text{ Hz}$), $\theta$ ($4\text{–}8\text{ Hz}$), $\alpha$ ($8\text{–}13\text{ Hz}$), $\beta$ ($13\text{–}30\text{ Hz}$) oraz $\gamma$ ($30\text{–}44\text{ Hz}$). Kluczowe wskaźniki badawcze to indeks obciążenia poznawczego (stosunek mocy czołowej $\theta$ do ciemieniowej/skroniowej $\alpha$) oraz czołowa asymetria fal alfa (FAA – *Frontal Alpha Asymmetry*) jako korelat walencji afektywnej.
  * **PPG (64 Hz):** Pomiar tętna (HR) oraz zmienności rytmu zatokowego (HRV, np. metryki RMSSD, SDNN), odzwierciedlających aktywność autonomicznego układu nerwowego (stres, pobudzenie współczulne).
  * **IMU (52 Hz):** Detekcja artefaktów ruchowych głowy i mikroruchów.
* **Interfejsy i łączność:** Bluetooth Low Energy (BLE). Surowe strumienie danych są dostępne w czasie rzeczywistym poprzez otwarte protokoły (np. *BlueMuse*, *BrainFlow SDK*, *Mind Monitor*) z bezpośrednim przekierowaniem do magistrali **Lab Streaming Layer (LSL)**.

---

### 1.3. Podsystem Sensoryki Okulometrycznej i Kinematycznej

#### Tobii Eye Tracker 5 (Okulometr Bezkontaktowy)
* **Charakterystyka techniczna:** Zdalny (remote) system śledzenia ruchu gałek ocznych oraz głowy, wykorzystujący oświetlacze bliskiej podczerwieni (NIR) oraz sensory optyczne do detekcji odbić rogówkowych i środka źrenicy (metoda *PCCR – Pupil Center Corneal Reflection*).
* **Możliwości pomiarowe i badawcze:** Rejestracja punktu fiksacji wzroku w przestrzeni roboczej (ekran lub płaszczyzna kalibracyjna), klasyfikacja zdarzeń okulometrycznych (fiksacje, sakady, mrugnięcia) oraz estymacja pozycji i orientacji głowy (6DoF Head Tracking) w polu widzenia sensora (zasięg pracy $45\text{–}95\text{ cm}$). Umożliwia analizę rozkładu uwagi wzrokowej (*Areas of Interest – AOI*), czasu skupienia (*Dwell Time*) oraz szybkości skanowania wzrokowego.
* **Interfejsy i łączność:** USB 2.0/3.0 (przewodowe połączenie z PC). Dostęp do strumieni danych w czasie rzeczywistym realizowany jest za pomocą *Tobii Stream Engine API* (C/C++/Python/C#) z możliwością publikacji w sieci LSL.

#### Ultraleap 3Di oraz Leap Motion Controller 2 (Sensory Śledzenia Dłoni)
* **Charakterystyka techniczna:** Stereoskopowe kamery głębi działające w bliskiej podczerwieni (850 nm), wykorzystujące zintegrowane diody LED IR do oświetlenia pola widzenia i rekonstrukcji szkieletowego modelu dłoni (27 stopni swobody na dłoń) bez konieczności stosowania znaczników.
  * **Ultraleap 3Di:** Wersja przemysłowa w uszczelnionej obudowie (IP54), zoptymalizowana pod kątem montażu w interfejsach kioskowych i stanowiskowych (pole widzenia $170^\circ \times 170^\circ$, zasięg od $10\text{ cm}$ do $100\text{ cm}$).
  * **Leap Motion Controller 2:** Kompaktowy, ultralekki sensor najnowszej generacji o obniżonym poborze mocy i szerszym polu widzenia ($160^\circ \times 160^\circ$), zaprojektowany zarówno do montażu na goglach HMD (XR), jak i pracy biurkowej.
* **Możliwości pomiarowe i badawcze:** Pomiar trójwymiarowych współrzędnych stawów palców, wektorów prędkości, przyspieszenia oraz kąta zgięcia z częstotliwością do **120 Hz** i submilimetrową precyzją. W badaniach kognitywnych dane te pozwalają obliczać metryki kinematyczne stresu i niepewności decyzyjnej: szarpnięcie ruchu (*jerk* – trzecia pochodna położenia), wskaźnik prostoliniowości trajektorii (*path efficiency*), drżenie posturalne dłoni oraz czas latencji inicjacji ruchu (*hesitation time*).
* **Interfejsy i łączność:** USB-C / USB 3.0. Obsługiwane przez ujednolicone oprogramowanie *Ultraleap Hyperion / Gemini SDK*, oferujące natywne wtyczki dla silników **Unity** i **Unreal Engine**, wsparcie standardu **OpenXR Hand Tracking** oraz bezpośrednie API w językach C# i Python.

---

### 1.4. Macierz Kompatybilności i Topologia Połączeń Międzyurządzeniowych

Ze względu na różnorodność interfejsów fizycznych i protokołów komunikacyjnych, integracja zestawu wymaga zastosowania **topologii gwiaździstej**, w której centralnym węzłem synchronizacji czasowej i wnioskowania AI jest **stacja robocza PC** (lub hybrydowo: **Samsung S25 Ultra + PC**).

| Urządzenie Źródłowe | Medium Transmisyjne | Węzeł Docelowy | Protokół / SDK | Ograniczenia i Uwagi Integracyjne |
| :--- | :--- | :--- | :--- | :--- |
| **Viture Luma Ultra XR** | Przewód USB-C (DP Alt Mode) | Samsung S25 Ultra lub PC (z wyjściem DP USB-C) | DisplayPort / Viture SDK (IMU) | Wymaga portu USB-C obsługującego wyjście wideo (S25 Ultra wspiera natywnie; w PC wymaga karty graficznej z USB-C lub adaptera HDMI/DP $\rightarrow$ USB-C z zasilaniem). |
| **Meta Quest 3** | Wi-Fi 6E/7 lub USB-C 3.2 | Stacja robocza PC | OpenXR / Quest Link / WebRTC | Najlepsza wydajność dla modeli VLM osiągana jest w trybie PCVR (obliczenia na GPU stacji roboczej, strumieniowanie obrazu do gogli). |
| **Muse S Athena** | Bluetooth Low Energy (BLE) | PC lub Samsung S25 Ultra | BlueMuse / BrainFlow $\rightarrow$ **LSL** | Połączenie bezpośrednie z PC wymaga stabilnego adaptera Bluetooth 5.0+. Alternatywnie: S25 Ultra odbiera sygnał BLE (aplikacja *Mind Monitor*) i przesyła go po Wi-Fi (OSC/LSL) do PC. |
| **Tobii Eye Tracker 5** | Przewód USB | Stacja robocza PC | Tobii Stream Engine $\rightarrow$ **LSL** | Wymaga systemu Windows. Działa wyłącznie w trybie stacjonarnym (biurkowym); wymaga kalibracji względem płaszczyzny roboczej. |
| **Ultraleap 3Di** | Przewód USB 3.0 | Stacja robocza PC | Ultraleap Gemini SDK / OpenXR | Przeznaczony do montażu stacjonarnego (nad lub pod przestrzenią roboczą) ze względu na masę i sztywny przewód przemysłowy. |
| **Leap Motion Controller 2** | Przewód USB-C | Meta Quest 3 (Android) lub PC | Ultraleap SDK (Android/Windows) | Może być podłączony bezpośrednio do portu USB-C w Quest 3 (przez hub z zasilaniem) lub do PC podczas pracy z Viture Luma Ultra XR. |

---

## 2. Propozycje Eksperymentów i Protokołów Pomiarowych

Poniższe trzy protokoły badawcze zostały zaprojektowane tak, aby w pełni wykorzystać synergię posiadanych urządzeń, eliminując ich wzajemne ograniczenia (np. brak zintegrowanego eye-trackera w goglach kompensowany jest przez stacjonarny Tobii 5 lub kinematykę dłoni Ultraleap i sygnał EEG z Muse S).

---

### Eksperyment 1: Adaptacyjna Redukcja Szumu Informacyjnego w AR Sterowana Neurofizjologicznym Indeksem Obciążenia Poznawczego

* **Konfiguracja sprzętowa (Stanowisko Biurkowe):**
  * **Wizualizacja:** Viture Luma Ultra XR (podłączone do PC lub S25 Ultra).
  * **Pomiar stanu kognitywnego:** Muse S Athena (EEG + PPG).
  * **Interakcja:** Ultraleap 3Di (zamontowany na statywie biurkowym skierowanym na przestrzeń manipulacji).
  * **Śledzenie uwagi:** Tobii Eye Tracker 5 (skalibrowany na płaszczyznę roboczą biurka).
* **Cel badawczy:** Weryfikacja hipotezy, że dynamiczne upraszczanie interfejsu AR w czasie rzeczywistym na podstawie wskaźników EEG/HRV obniża czas realizacji zadania i liczbę błędów w warunkach wysokiego obciążenia poznawczego.
* **Procedura eksperymentalna:**
  1. **Faza kalibracji (5 min):** Osoba badana zakłada opaskę Muse S Athena, a następnie okulary Viture Luma Ultra XR (brak kolizji mechanicznej dzięki lekkim zausznikom okularów). Rejestrowany jest stan spoczynkowy (2 min z oczami otwartymi, 1 min z zamkniętymi) oraz wykonywane jest zadanie referencyjne *Spatial N-Back* w AR w celu wyznaczenia indywidualnych progów obciążenia poznawczego dla pasm $\theta$ i $\alpha$.
  2. **Zadanie główne (20 min):** Uczestnik wykonuje złożoną procedurę montażu lub diagnostyki układu elektronicznego/mechanicznego na biurku. W polu widzenia okularów Viture wyświetlane są instrukcje krok po kroku, schematy połączeń oraz parametry telemetryczne. Dodatkowo wprowadzany jest dystraktor słuchowy (zadanie wtórne wymagające zapamiętywania komunikatów), aby sztucznie wywołać przeciążenie poznawcze.
  3. **Warunki eksperymentalne (układ wewnątrzgrupowy, 3 bloki w kolejności zrównoważonej):**
     * *Warunek A (Statyczny HUD):* Pełna gęstość informacji wyświetlana przez cały czas trwania zadania.
     * *Warunek B (Adaptacja losowa – grupa kontrolna placebo):* Interfejs zmienia poziom szczegółowości w losowych odstępach czasu.
     * *Warunek C (Adaptacja Cognitive-AI):* Klasyfikator AI na PC analizuje w oknach przesuwnych (długość okna $4\text{ s}$, krok $0.5\text{ s}$) stosunek mocy fal $\theta/\alpha$ (AF7, AF8), zmienność tętna (PPG) oraz rozproszenie fiksacji wzroku (Tobii 5). Gdy indeks obciążenia przekroczy indywidualny próg, silnik Unity płynnie redukuje interfejs (ukrywa wykresy pomocnicze, pozostawiając jedynie kluczowy wskaźnik kolejnego kroku).
* **Mierzone zmienne zależne:**
  * *Neurofizjologiczne:* Znormalizowana moc pasma $\theta$ w kanałach AF7/AF8, indeks zaangażowania $\beta / (\alpha + \theta)$, metryka RMSSD z sygnału PPG.
  * *Behawioralne i kinematyczne:* Czas wykonania procedury, liczba błędów montażowych, wskaźnik szarpnięcia ruchu dłoni (*jerk*) oraz czas zawahania przed chwytem elementu (z Ultraleap 3Di), liczba fiksacji na elementach rozpraszających HUD (z Tobii 5).
  * *Subiektywne:* Kwestionariusz obciążenia pracą NASA-TLX wypełniany po każdym bloku.

---

### Eksperyment 2: Weryfikacja Procedur Manualnych w Czasie Rzeczywistym przez Autonomicznego Agenta VLM z Wykorzystaniem Kinematyki Dłoni

* **Konfiguracja sprzętowa (Stanowisko Przestrzenne MR):**
  * **Wizualizacja i akwizycja sceny:** Meta Quest 3 (połączony z PC przez Wi-Fi 6E).
  * **Śledzenie dłoni:** Leap Motion Controller 2 (zamontowany na froncie Quest 3).
  * **Pomiar stanu afektywnego/stresu:** Muse S Athena (noszona pod paskiem nagłownym gogli).
* **Cel badawczy:** Ocena skuteczności multimodalnego systemu łączącego modele *Vision-Language* (VLM) oraz dane kinematyczne z sensora głębi w predykcji błędów operatora jeszcze przed ich fizycznym dokonaniem (proaktywna interwencja).
* **Procedura eksperymentalna:**
  1. **Przygotowanie:** Uczestnik zakłada opaskę Muse S Athena oraz gogle Meta Quest 3 z zamontowanym sensorem Leap Motion Controller 2. Aplikacja w Unity przesyła strumień wideo z kamer gogli (lub dodatkowej kamery Samsung S25 Ultra ustawionej na statywie nad stanowiskiem) oraz współrzędne szkieletu dłoni do stacji roboczej PC.
  2. **Zadanie główne (25 min):** Badany realizuje wieloetapową procedurę serwisową zawierającą kroki o wysokim ryzyku pomyłki (np. podłączanie przewodów o zbliżonych kolorach lub montaż elementów w określonej kolejności).
  3. **Architektura wnioskowania hybrydowego (Kinematyka + VLM):**
     * Sensor Leap Motion Controller 2 wykrywa w czasie rzeczywistym, po który obiekt fizyczny sięga dłoń użytkownika (wektor ruchu i zbliżenie palców do strefy obiektu) oraz rejestruje mikrozawahania.
     * W momencie zbliżenia dłoni do elementu, wyzwalane jest zapytanie do lokalnego modelu VLM (np. *Qwen2.5-VL* lub *LLaVA* uruchomionego na GPU stacji roboczej) z aktualną klatką obrazu oraz stanem grafu procedury. Model weryfikuje, czy obiekt, po który sięga użytkownik, jest zgodny z bieżącym krokiem instrukcji.
  4. **Warunki eksperymentalne:**
     * *Warunek 1 (Reaktywny):* Agent VLM informuje o błędzie dopiero po jego popełnieniu (gdy obiekt zostanie zamontowany w złym miejscu).
     * *Warunek 2 (Proaktywny – predykcja kinematyczno-wizyjna):* Gdy trajektoria dłoni z Leap Motion wskazuje na ruch w kierunku błędnego elementu, system natychmiast wyświetla w przestrzeni AR ostrzegawczy kontur wokół tego elementu i podświetla właściwy komponent.
* **Mierzone zmienne zależne:**
  * *Efektywność systemu:* Liczba zapobiegniętych błędów (wskaźnik *Error Prevention Rate*), opóźnienie pętli wnioskowania VLM (od intencji ruchu do wyświetlenia wskazówki AR).
  * *Reakcja psychofizjologiczna:* Zmiana czołowej asymetrii fal alfa (FAA) oraz nagłe skoki tętna (PPG z Muse S) w odpowiedzi na komunikaty korygujące agenta (badanie poziomu frustracji wywołanej interwencją AI).
  * *Subiektywne:* Skala zaufania do automatyzacji (*Trust in Automation Scale*) oraz ocena użyteczności (SUS).

---

### Eksperyment 3: Korelacja Mikro-ruchów Dłoni, Okulometrii i Fal Mózgowych w Detekcji Stanu Niepewności Decyzyjnej w Interfejsach AR

* **Konfiguracja sprzętowa (Stanowisko Hybrydowe):**
  * **Wizualizacja i obliczenia brzegowe:** Samsung S25 Ultra + Viture Luma Ultra XR (wykorzystanie mocy NPU smartfona do lokalnej inferencji).
  * **Sensoryka:** Muse S Athena + Tobii Eye Tracker 5 + Ultraleap 3Di.
* **Cel badawczy:** Opracowanie wielomodalnego modelu uczenia maszynowego (fuzja danych EEG + Eye-Tracking + Hand Kinematics) zdolnego do klasyfikacji stanu niepewności poznawczej i dezorientacji użytkownika bez konieczności angażowania ciężkich obliczeniowo modeli VLM.
* **Procedura eksperymentalna:**
  1. **Paradygmat zadania:** Użytkownik rozwiązuje serię zadań klasyfikacji i sortowania przestrzennego w środowisku AR (np. identyfikacja uszkodzonych komponentów na podstawie niejednoznacznych lub niepełnych danych wyświetlanych w okularach Viture). Poziom niejednoznaczności bodźców jest stopniowany (od oczywistych po wysoce niejednoznaczne).
  2. **Akwizycja zsynchronizowana (LSL):** Wszystkie strumienie danych (256 Hz EEG z Muse S, 90 Hz Gaze z Tobii 5, 120 Hz Hand Tracking z Ultraleap 3Di) są rejestrowane synchronicznie w pliku `.xdf`.
  3. **Etykietowanie danych (Ground Truth):** Po każdej próbie użytkownik dokonuje gestu w przestrzeni (rozpoznawanego przez Ultraleap 3Di), wskazując swoją decyzję oraz oceniając w skali 1–5 pewność podjętej decyzji (*Confidence Rating*).
* **Analiza danych i modelowanie AI:**
  * Ekstrakcja cech multimodalnych z ostatnich $3\text{ sekund}$ przed podjęciem decyzji:
    * *Z Ultraleap 3Di:* Wskaźnik zawahania (czas przebywania dłoni w zawieszeniu nad obiektem przed wykonaniem ruchu zatwierdzającego), mikrowahania trajektorii (zmiany znaku wektora prędkości).
    * *Z Tobii Eye Tracker 5:* Liczba przełączeń spojrzenia (*gaze transitions*) między obiektem fizycznym a etykietą AR, wydłużenie średniego czasu fiksacji.
    * *Z Muse S Athena:* Wzrost mocy w paśmie $\theta$ w obszarze czołowym (korelujący z konfliktem poznawczym w przedniej korze zakrętu obręczy – ACC).
  * Trening lekkiej architektury sieci neuronowej (np. wielogałęziowa sieć *1D-CNN + BiLSTM* lub *Temporal Fusion Transformer*) oraz kwantyzacja modelu do formatu **ONNX / TensorFlow Lite** w celu uruchomienia go bezpośrednio na procesorze NPU smartfona **Samsung S25 Ultra** w czasie rzeczywistym.
