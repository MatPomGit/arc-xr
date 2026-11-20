# ARC-XR — badania nad inteligentną rozszerzoną rzeczywistością

ARC-XR jest repozytorium planowanych badań nad adaptacyjnymi interfejsami AR, multimodalnym wnioskowaniem o stanie użytkownika, modelami Vision–Language (VLM), weryfikacją czynności manualnych i komunikacją człowiek–agent. Dokumenty na obecnym etapie są **prospektywnymi projektami**, a nie wynikami badań.

## Wariant minimalny

Badania prowadzić jako niewielkie pilotaże i dwa wspólne środowiska zamiast sześciu nowych systemów. Szczegółowe porównania, pomiary i ograniczenia aparatury: [plan minimalny](manuscripts/mvp_plan.md). Pilotaże nie zastępują badań potwierdzających.

## Dodatkowe propozycje naukowe

[XR-IDEA-20: moment prezentacji wskazówki AR względem fazy ruchu dłoni](docs/research-proposals-2026.md) jest koncepcją do audytu nowości, **poza zatwierdzonym zakresem P01–P06**. Nie zmienia bieżącego planu minimalnych badań ani liczby manuskryptów.

## Portfolio publikacji

| ID | Temat | Stan |
| --- | --- | --- |
| [P01](manuscripts/P01/README.md) | Multimodalna ocena obciążenia poznawczego i adaptacja interfejsu AR | Planowana |
| [P02](manuscripts/P02/README.md) | Detekcja frustracji i dekoncentracji podczas procedur manualnych w AR | Planowana |
| [P03](manuscripts/P03/README.md) | Wpływ okluzji i asynchronii renderowania AR na zmęczenie wzrokowo-poznawcze | Planowana |
| [P04](manuscripts/P04/README.md) | Grounding przestrzenny 3D modeli VLM w zadaniach manipulacyjnych AR | Planowana |
| [P05](manuscripts/P05/README.md) | Autonomiczny asystent AR do weryfikacji procedur manualnych | Planowana |
| [P06](manuscripts/P06/README.md) | Multimodalna komunikacja człowiek–agent oraz współdzielenie uwagi w AR | Planowana |

W pierwotnym opisie występowało sześć merytorycznie określonych propozycji, ale numeracja była niespójna (dwie pozycje 3 oraz pusta pozycja 8). Nadano im identyfikatory P01–P06 bez dodawania nieopisanych artykułów.

## Organizacja repozytorium

Każda publikacja w `manuscripts/PXX/` ma własny opis zakresu, szkic manuskryptu, hipotezy, protokół, dokumentację eksperymentów, plan analiz, rejestr wyników oraz katalog figur. Indeks: [manuscripts/README.md](manuscripts/README.md). Wymagania naukowe i zasady udostępniania danych: [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

## Zarządzanie badaniami

[AGENTS.md](AGENTS.md) określa zasady pracy agentów i przeglądu PR, [RESEARCH.md](RESEARCH.md) reguły metodologiczne i redakcyjne, [PROJECT_STATE.yaml](PROJECT_STATE.yaml) aktualny stan naukowy, a [AUTOPILOT_PLAN.md](AUTOPILOT_PLAN.md) kolejność prac i bramki. [REPRODUCIBILITY.md](REPRODUCIBILITY.md) zawiera wymagania dotyczące danych i replikacji.

Repozytorium korzysta z zasad zarządzania Research Autopilot, ale samo istnienie dokumentów nie oznacza rejestracji ani aktywnego wykonywania zadań w kontrolerze.

## Zasady

Nie należy traktować propozycji metod ani testów statystycznych jako prerejestracji. Każdy eksperyment z uczestnikami wymaga oceny etycznej i świadomej zgody według właściwych przepisów i procedur instytucji. Rejestrować pochodzenie danych, wersje sprzętu i oprogramowania, kryteria wykluczenia, podziały danych oraz odrębność zbioru testowego. Wyników i cytowań nie wolno uzupełniać bez źródeł i rzeczywistego materiału empirycznego.

Licencja znajduje się w pliku [LICENSE](LICENSE). Jej zakres nie zastępuje zgody na rozpowszechnianie cudzych zbiorów danych ani wizerunku i nagrań uczestników.
