# P01: przegląd literatury i granice nowości

**Wersja robocza:** 0.2.1, 2026-11-19. **Status:** selektywny przegląd, nie przegląd systematyczny ani prerejestracja. Badania P01 pozostają projektem; nie zgromadzono wyników empirycznych ARC-XR.

## Zakres

Przeanalizowano sześć pozycji dotyczących adaptacyjnej AR, pomiarów fizjologicznych i NASA-TLX. Jest to wybór celowy, a nie wyczerpująca kwerenda. Przed zakończeniem M1 trzeba udokumentować strategię wyszukiwania, kryteria selekcji i ograniczenia badań pierwotnych. Wyników innych autorów nie wolno przedstawiać jako wyników ARC-XR.

## Indeks porównywanych publikacji

| Źródło | Zakres istotny dla P01 |
| --- | --- |
| [Sun i Liao (2025)](https://doi.org/10.1017/dsj.2025.10040) | Przerwy w AR sterowane odpowiedzią elektrodermalną. |
| [Gonnermann-Müller i in. (2024)](https://aisel.aisnet.org/icis2024/humtechinter/humtechinter/18/) | Wyróżnianie wskazówek w przemysłowej AR. |
| [Chiossi i in. (2024)](https://doi.org/10.1109/TVCG.2024.3456172) | Wyszukiwanie wzrokowe i EEG/okulometria w rzeczywistości mieszanej. |
| [Suzuki i in. (2024)](https://doi.org/10.1111/jcal.12882) | Przegląd fizjologicznych miar obciążenia w AR. |
| [Mathôt (2018)](https://doi.org/10.5334/joc.18) | Podstawy interpretacji pupilometrii. |
| [Hart i Staveland (1988)](https://doi.org/10.1016/S0166-4115(08)62386-9) | Wielowymiarowy pomiar NASA-TLX. |

## Analiza źródeł i ograniczeń

### Sun i Liao (2025)

Autorzy badali interakcję z AR z wykorzystaniem sygnałów związanych z ruchem wzroku i dłoni oraz aktywności elektrodermalnej (EDA/SCR). Adaptacyjne przerwy uruchamiano na podstawie wskaźnika skumulowanej odpowiedzi skórno-galwanicznej. Autorzy opisali zmniejszenie tego wskaźnika po interwencji, lecz nie wykazali poprawy wykonania zadania.

Dla P01 jest to przykład adaptacji fizjologicznej, dlatego nie można deklarować pierwszeństwa w tej kategorii. Interwencja polegała jednak na wprowadzaniu przerw, a nie na bieżącej regulacji gęstości treści HUD. SCR nie jest swoistą miarą obciążenia poznawczego.

### Gonnermann-Müller i współautorzy (2024)

W badaniu dotyczącym szkolenia przemysłowego w AR porównano prezentację wskazówek z wyróżnieniem istotnych informacji i bez takiego wyróżnienia. Wykorzystano kwestionariusze oraz okulometrię; opis badania podaje próbę 55 uczestników. Autorzy raportowali mniejsze deklarowane obciążenie w warunku wyróżniania informacji.

Zestawienie uzasadnia kontrolowanie widoczności wskazówek w P01. Nie jest jednak bezpośrednim testem zamkniętej pętli multimodalnej estymacji obciążenia i dynamicznej adaptacji interfejsu w czasie rzeczywistym.

### Chiossi i współautorzy (2024)

Autorzy analizowali wyszukiwanie obiektów fizycznych i wirtualnych w rzeczywistości mieszanej. Badano potencjały związane ze zdarzeniami (ERP), fiksacje, sakkady oraz wykonanie zadania.

Wyniki uzasadniają uwzględnianie złożoności sceny i rozdzielania uwagi podczas projektowania P01. Praca nie stanowi jednak eksperymentu z adaptacyjną gęstością treści HUD sterowaną multimodalnym modelem obciążenia.

### Suzuki, Wild i Scanlon (2024)

W przeglądzie systematycznym 23 badań przedstawiono fizjologiczne sposoby oceny obciążenia w AR. Autorzy zwracali uwagę na heterogeniczność metod oraz potrzebę podejścia wielometodowego i kontroli wpływu urządzeń, zadań oraz wskazówek. Okulometria należała do stosowanych technik.

Jest to źródło wtórne przydatne do uzasadnienia projektu pomiarowego, a nie dowód skuteczności konkretnej adaptacji proponowanej w P01. Nie należy przenosić zagregowanych obserwacji z przeglądu na przewidywany wynik eksperymentu.

### Mathôt (2018)

Praca omawia fizjologię i psychologiczne zastosowania pupilometrii. Reakcja źrenicy zależy między innymi od luminancji i procesów poznawczych, dlatego jej zmian nie można jednoznacznie utożsamiać z poziomem obciążenia.

W P01 należy kontrolować luminancję sceny i HUD, jakość kalibracji okulometru oraz artefakty pomiarowe. Jest to źródło metodologiczne, a nie badanie oceniające skuteczność adaptacyjnej AR.

### Hart i Staveland (1988)

Autorzy przedstawili podstawy NASA-TLX, kwestionariusza obejmującego sześć wymiarów subiektywnego obciążenia zadaniem. Skala może uzupełniać pomiary behawioralne i fizjologiczne.

NASA-TLX nie jest jednak ciągłą etykietą stanu poznawczego w każdej klatce ani zamiennikiem obiektywnego wyniku zadaniowego. W P01 należy traktować go jako miarę dodatkową, nie alternatywny główny punkt końcowy.

## Granice interpretacji

Podane metadane i główne przesłanki metodologiczne powiązano z publikacjami wydawców oraz materiałami źródłowymi. Nie wykonano pełnego przeglądu systematycznego, oceny ryzyka błędu systematycznego ani metaanalizy. Wszystkie przywołane wyniki pochodzą z badań zewnętrznych.

Rekordy dla sześciu opisanych prac znajdują się w [bibliografii BibTeX](references.bib).

## Zakres potencjalnej nowości

Nie deklarować, że P01 jest „pierwszym fizjologicznie adaptacyjnym systemem AR”; literatura z 2025 r. już obejmuje adaptacyjne przerwy na podstawie SCR. Rozważany **węższy i weryfikowalny wkład** to zamknięta pętla kontroli gęstości informacji HUD, w której:
1. Z góry zdefiniowany, multimodalny estymator obciążenia jest testowany na osobach wykluczonych z treningu, względem równoważnego jednomodalnego baseline'u.
2. Adaptacja UI ma niezależny test przyczynowego wpływu na *z góry wybrany jeden* główny wynik zachowania (kandydat: odsetek błędnych prób zadaniowych, wymagający zatwierdzenia przed badaniem); porównania z HUD statycznym i adaptacją jednomodalną muszą być uczciwe pod względem opóźnienia oraz budżetu obliczeniowego.
3. System rejestruje fałszywe aktywacje, opóźnienie adaptacji, liczbę zmian UI, koszt obliczeniowy oraz możliwość abstencji lub ograniczenia aktualizacji.
4. Eksperyment kontroluje luminancję, trudność zadania, kolejność warunków, zmęczenie i jakość eye trackera; nie wyprowadza diagnostycznych wniosków o stanie psychicznym z pojedynczego sygnału.
5. Plan odróżnia jakość predykcji od efektu interwencji; brak statystycznie istotnej poprawy jest prawidłowym wynikiem.

## Pozostałe prace nad przeglądem

Przed zakończeniem M1 należy rozszerzyć kwerendę o nowsze prace dotyczące adaptacji gęstości informacji, przeprowadzić selekcję według jawnych kryteriów oraz porównać warunki i metryki badań. Potencjalna nowość wymaga dalszej weryfikacji.
