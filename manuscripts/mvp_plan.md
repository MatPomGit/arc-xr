# ARC-XR: minimalny plan badań P01–P06

**Wersja:** 0.1.0 (2026-11-19). **Status:** kierunek uproszczenia zaakceptowany, ale hipotezy i protokoły nie są zamrożone. Brak zweryfikowanych danych empirycznych, prerejestracji i decyzji etycznej. [Zadanie #10](https://github.com/MatPomGit/arc-xr/issues/10).

## Zasada minimum viable research

W każdym badaniu przewidzieć jeden główny kontrast, jeden zdefiniowany przed analizą wynik główny i najprostszy adekwatny model. W pilotażu preferować dwa warunki. Nie dodawać nowych czujników, ciężkich sieci ani autonomicznych agentów bez wykazanej konieczności.

Pilotaż około 5–8 osób może ocenić wykonalność, ergonomię i rejestrowanie danych, ale nie zastępuje właściwego badania potwierdzającego, analizy mocy/precyzji ani wymaganej oceny etycznej. Warianty uproszczone nie potwierdzają automatycznie rozbudowanych hipotez z istniejących szkiców manuskryptów.

## Minimalne eksperymenty

| ID | Porównanie minimalne | Proponowany wynik główny | Odłożone rozszerzenie |
| --- | --- | --- | --- |
| P01 | Statyczny HUD vs HUD z prostą regułą adaptacji zachowania | Odsetek błędnych prób | Multimodalny estymator i trzy warunki; pilotaż nie testuje dotychczasowych H1/H2 |
| P02 | Predyktor globalny vs model indywidualnie kalibrowany na kolejnych sesjach | Macro-F1 względem niezależnych samoopisów frustracji | Uczenie ciągłe i mikrointerwencje |
| P03 | Renderowanie referencyjne vs jeden kontrolowany poziom opóźnienia | Zmiana wyniku wcześniej wybranej skali dyskomfortu wzrokowego | Pełny układ okluzja × opóźnienie |
| P04 | Ten sam VLM 2D vs VLM z jawną geometrią 3D | Odsetek poprawnie wskazanych obiektów | Precyzyjne kotwiczenie, abstencja i złożone sceny |
| P05 | Wykrywanie kroków bez pamięci vs z prostą sekwencją stanów | Czułość pominięć przy ustalonym limicie fałszywych alarmów | Rozbudowane grafy i aktywne instrukcje |
| P06 | Prosty kursor przestrzenny vs prosty awatar | Czas poprawnego ustanowienia wspólnego obiektu | Gesty, mowa i pełny agent |

Każdy wynik główny, próg i jednostkę analizy zatwierdzić przed badaniem. Nie wybierać korzystniejszych metryk po zobaczeniu danych. Rozdzielać ocenę skuteczności predykcji od przyczynowego wpływu interwencji.

## Dwa lekkie środowiska

**Unity/AR:** jedna bazowa aplikacja dla P01, P03 i P06, ale odrębne sceny, warunki i analizy. P02 może wykorzystywać prosty eksperyment ekranowy.

**Python/VLM:** wspólna baza skalibrowanych scen, referencji przestrzennych i małych skryptów dla P04/P05. P04 bada wskazanie obiektu, P05 kolejność kroków. Raportować współdzielenie nagrań i prób między publikacjami.

## Granice aparatury

Standardowy Meta Quest 3 nie ma eye trackingu. Tobii Eye Tracker 5 działa przy monitorze; nie jest zintegrowanym okulometrem Quest 3. Minimalne badania AR nie mogą wymagać eye trackingu HMD. Ekranowy pilotaż z Tobii to odrębne środowisko i nie zastępuje walidacji wewnątrz gogli.

P04 może opierać się na znanych pozycjach obiektów lub skalibrowanych znacznikach, bez zakładania dostępu do surowych map głębi Quest 3. W P03 mierzyć faktyczną latencję, ograniczać ekspozycję i stosować kryteria przerwania.

## Minimalne dane i kontrola jakości

Wystarczają schematyczne CSV/JSON z anonimowymi identyfikatorami sesji/prób, wersją aplikacji i sprzętu, warunkiem, timestampem, wynikiem i odrzuceniami. Rejestrować SHA kodu, parametry, podziały trening/test oraz efekty i przedziały niepewności. Dane osobowe, biometryczne i nagrania nie trafiają do publicznego Git.

Bez płatnych API, dodatkowych schedulerów i nowych agentów. Research Autopilot pozostaje wspólnym kontrolerem, ale integracja wymaga osobnego potwierdzenia. Plan nie upoważnia do rekrutacji, wydatków ani wysyłki artykułu.

## Kolejność

1. P04 i P06: szybkie prototypy i testy techniczne.
2. P01 i P03: próby techniczne, a następnie badania po spełnieniu bramek etycznych.
3. P05 i P02: po walidacji danych i etykiet.

Stan naukowy: [PROJECT_STATE.yaml](../PROJECT_STATE.yaml).
