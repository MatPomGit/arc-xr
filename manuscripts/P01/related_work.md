# P01: przegląd literatury i granice nowości

**Wersja robocza:** 0.2.0, 2026-11-19. **Status:** selektywny przegląd, nie przegląd systematyczny ani prerejestracja. Badania P01 pozostają projektem; nie zgromadzono wyników empirycznych ARC-XR.

## Zakres

Wybrano sześć pozycji z zakresu adaptacji AR, pomiarów fizjologicznych i NASA-TLX. Zestawienie nie wyczerpuje stanu badań. Przed zakończeniem M1 należy udokumentować kwerendę, kryteria selekcji oraz ograniczenia metodologiczne źródeł. Nie wolno przypisywać P01 rezultatów innych autorów.

## Porównanie badań

| Pozycja i źródło pierwotne | Rodzaj / pomiar | Ustalenie istotne dla P01 | Ograniczenie względem wkładu P01 |
| --- | --- | --- | --- |
| **Sun & Liao (2025),** *Design Science*, 11, e49, [doi:10.1017/dsj.2025.10040](https://doi.org/10.1017/dsj.2025.10040) | Badanie interakcji AR: gaze/hand, EDA/SCR i adaptacyjne przerwy | Zmniejszenie wskaźnika skumulowanej odpowiedzi skórno-galwanicznej po adaptacyjnych przerwach; poprawa wykonania zadania nie została wykazana | Interwencją jest odpoczynek, a nie dynamiczna gęstość treści HUD; wskaźnik SCR nie stanowi specyficznej diagnozy obciążenia |
| **Gonnermann-Müller, Leins, Gronau & Kosch (2024),** *ICIS 2024 Proceedings*, [AIS eLibrary](https://aisel.aisnet.org/icis2024/humtechinter/humtechinter/18) | Badanie pierwotne w środowisku szkolenia przemysłowego, N=55, kwestionariusze i okulometria; wskazówki AR z/bez wyróżnienia informacji | Autorzy opisują mniejsze subiektywne obciążenie przy wyróżnieniu istotnej informacji w AR | Nie stanowi bezpośredniego testu zamkniętej pętli multimodalnej estymacji z adaptacją w czasie rzeczywistym |
| **Chiossi, Trautmannsheimer, Ou, Gruenefeld & Mayer (2024),** *IEEE TVCG*, 30(11), 6997-7007, [doi:10.1109/TVCG.2024.3456172](https://doi.org/10.1109/TVCG.2024.3456172) | Badanie porównawcze wyszukiwania obiektów fizycznych i wirtualnych; EEG/ERP, fiksacje, sakkady i wykonanie zadania | Pokazuje konieczność uwzględniania rozdzielności uwagi i złożoności sceny | Nie testuje adaptacyjnego dawkowania informacji sterowanego multimodalną predykcją obciążenia |
| **Suzuki, Wild & Scanlon (2024),** *Journal of Computer Assisted Learning*, 40(2), 375-393, [doi:10.1111/jcal.12882](https://doi.org/10.1111/jcal.12882) | Przegląd systematyczny 23 badań AR z pomiarem fizjologicznym | Zaleca podejście wielometodowe i oddzielanie wpływu urządzenia, zadania oraz rodzaju wskazówek; okulometria często wykorzystywana | Praca wtórna; nie może być traktowana jako własny dowód skuteczności adaptacji P01 |
| **Mathôt (2018),** *Journal of Cognition*, 1(1), art. 16, [doi:10.5334/joc.18](https://doi.org/10.5334/joc.18) | Przegląd fizjologii pupilometrii | Źrenica odzwierciedla również reakcję na luminancję i zmiany poznawcze; nie jest jednoznacznym sensorem obciążenia | Niezbędna kontrola luminancji, artefaktów okulometrycznych i kalibracji; tekst metodologiczny, nie AR |
| **Hart & Staveland (1988),** *Advances in Psychology*, 52, 139-183, [doi:10.1016/S0166-4115(08)62386-9](https://doi.org/10.1016/S0166-4115(08)62386-9), [NASA TLX](https://www.nasa.gov/human-systems-integration-division/nasa-task-load-index-tlx/) | Geneza wielowymiarowej skali subiektywnego obciążenia NASA-TLX | Sześć podskal obciążenia, możliwość komplementarnej walidacji względem zachowania i fizjologii | Kwestionariusz nie zapewnia ciągłej etykiety stanu poznawczego i nie zastępuje obiektywnych metryk błędów |

**Zakres weryfikacji:** metadane, podstawowa metodologia i najważniejsze wnioski sprawdzone w oryginalnych witrynach wydawców/autorów oraz PubMed lub NASA; nie przeprowadzono pełnego systematycznego przeglądu całego korpusu ani oceny ryzyka błędu systematycznego. Wyniki cudzych badań nie są wynikami ARC-XR.

Pełne metadane zawiera [bibliografia](references.bib).

## Zakres potencjalnej nowości

Nie deklarować, że P01 jest „pierwszym fizjologicznie adaptacyjnym systemem AR”; literatura z 2025 r. już obejmuje adaptacyjne przerwy na podstawie SCR. Rozważany **węższy i weryfikowalny wkład** to zamknięta pętla kontroli gęstości informacji HUD, w której:
1. Z góry zdefiniowany, multimodalny estymator obciążenia jest testowany na osobach wykluczonych z treningu, względem równoważnego jednomodalnego baseline'u.
2. Adaptacja UI ma niezależny test przyczynowego wpływu na *z góry wybrany jeden* główny wynik zachowania (kandydat: odsetek błędnych prób zadaniowych, wymagający zatwierdzenia przed badaniem); porównania z HUD statycznym i adaptacją jednomodalną muszą być uczciwe pod względem opóźnienia oraz budżetu obliczeniowego.
3. System rejestruje fałszywe aktywacje, opóźnienie adaptacji, liczbę zmian UI, koszt obliczeniowy oraz możliwość abstencji lub ograniczenia aktualizacji.
4. Eksperyment kontroluje luminancję, trudność zadania, kolejność warunków, zmęczenie i jakość eye trackera; nie wyprowadza diagnostycznych wniosków o stanie psychicznym z pojedynczego sygnału.
5. Plan odróżnia jakość predykcji od efektu interwencji; brak statystycznie istotnej poprawy jest prawidłowym wynikiem.

## Pozostałe prace nad przeglądem

Przed zakończeniem M1 należy rozszerzyć kwerendę o nowsze prace dotyczące adaptacji gęstości informacji, przeprowadzić selekcję według jawnych kryteriów oraz porównać warunki i metryki badań. Potencjalna nowość wymaga dalszej weryfikacji.
