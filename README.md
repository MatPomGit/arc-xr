# ARC-XR — badania nad inteligentną rozszerzoną rzeczywistością

ARC-XR jest repozytorium planowanych badań nad adaptacyjnymi interfejsami AR, multimodalnym wnioskowaniem o stanie użytkownika, modelami Vision–Language (VLM), weryfikacją czynności manualnych i komunikacją człowiek–agent. Dokumenty na obecnym etapie są **prospektywnymi projektami**, a nie wynikami badań.

## Wariant minimalny

Badania prowadzić jako niewielkie pilotaże i dwa wspólne środowiska zamiast sześciu nowych systemów. Szczegółowe porównania, pomiary i ograniczenia aparatury: [plan minimalny](manuscripts/mvp_plan.md). Pilotaże nie zastępują badań potwierdzających.

## Dodatkowe propozycje naukowe

[MSC-AR-P26: moment prezentacji wskazówki AR względem fazy ruchu dłoni](docs/research-proposals-2026.md) jest koncepcją do audytu nowości, **poza zatwierdzonym zakresem P01–P06**. Nie zmienia bieżącego planu minimalnych badań ani liczby manuskryptów.

## Publiczny katalog tematyki badań

[Wykaz 27 tematów i ich krótkie omówienia](pages/articles.md) przedstawia siedem planowanych manuskryptów oraz dwadzieścia dodatkowych koncepcji. Publiczna witryna powstaje wyłącznie z wydzielonego katalogu `pages/`.

## Pilotaż migracji do ARC v2

[Mapa migracyjna 27 manuskryptów](docs/migrations/arc-v2-pilot.md) przypina pliki TeX do ich identyfikatorów MSC i wykrywa sześć starszych katalogów wymagających późniejszego przemianowania. Jedna pozycja jest pomocniczym szkicem projektu kanonicznego poza ARC-XR. Audyt: `python3 scripts/audit_arc_v2_pilot.py`. Narzędzie nie zapisuje plików, nie zmienia właścicieli i nie uruchamia publikacji.

## Portfolio publikacji

| ID | Temat | Stan |
| --- | --- | --- |
| [P01](manuscripts/MSC-AR-P01/README.md) | Multimodalna ocena obciążenia poznawczego i adaptacja interfejsu AR | Planowana |
| [P02](manuscripts/MSC-AR-P02/README.md) | Detekcja frustracji i dekoncentracji podczas procedur manualnych w AR | Planowana |
| [P03](manuscripts/MSC-AR-P03/README.md) | Wpływ okluzji i asynchronii renderowania AR na zmęczenie wzrokowo-poznawcze | Planowana |
| [P04](manuscripts/MSC-AR-P04/README.md) | Grounding przestrzenny 3D modeli VLM w zadaniach manipulacyjnych AR | Planowana |
| [P05](manuscripts/MSC-AR-P05/README.md) | Autonomiczny asystent AR do weryfikacji procedur manualnych | Planowana |
| [P06](manuscripts/MSC-AR-P06/README.md) | Multimodalna komunikacja człowiek–agent oraz współdzielenie uwagi w AR | Planowana |

W pierwotnym opisie występowało sześć merytorycznie określonych propozycji, ale numeracja była niespójna (dwie pozycje 3 oraz pusta pozycja 8). Nadano im identyfikatory P01–P06 bez dodawania nieopisanych artykułów.

## Organizacja repozytorium

Każda publikacja w `manuscripts/PXX/` ma własny opis zakresu, szkic manuskryptu, hipotezy, protokół, dokumentację eksperymentów, plan analiz, rejestr wyników oraz katalog figur. Indeks: [manuscripts/README.md](manuscripts/README.md). Wymagania naukowe i zasady udostępniania danych: [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

## Źródła manuskryptów w LaTeX

Katalog [`manuscripts/`](manuscripts/README.md) zawiera **27 odrębnych plików `main.tex`**: sześć podstawowych projektów P01–P06 oraz 21 dodatkowych pozycji z pełnymi identyfikatorami MSC. Wszystkie są szkicami naukowymi; ich opracowanie nie oznacza zebrania danych ani potwierdzonych wyników.

## Standard GitHub Issues

Zadania przyjmujemy przez [formularze Issues](https://github.com/MatPomGit/arc-xr/issues/new/choose): zadanie/JUMP, błąd, eksperyment i manuskrypt. [Standard Issues](docs/issues.md) określa typy intencji, klasyfikację `agent-work-classification:v1`, relacje, kryteria akceptacji i dowody exact SHA. Metadane nie przyznają zgody na wykonanie, a `PROJECT_STATE.yaml` pozostaje jedynym stanem badań P01–P06.

## Zarządzanie badaniami

[AGENTS.md](AGENTS.md) określa zasady pracy agentów i przeglądu PR, [RESEARCH.md](RESEARCH.md) reguły metodologiczne i redakcyjne, [PROJECT_STATE.yaml](PROJECT_STATE.yaml) aktualny stan naukowy, a [AUTOPILOT_PLAN.md](AUTOPILOT_PLAN.md) kolejność prac i bramki. [REPRODUCIBILITY.md](REPRODUCIBILITY.md) zawiera wymagania dotyczące danych i replikacji.

Repozytorium korzysta z zasad zarządzania Research Autopilot, ale samo istnienie dokumentów nie oznacza rejestracji ani aktywnego wykonywania zadań w kontrolerze.

## Architektura, bezpieczeństwo i strona publiczna

[ARCHITECTURE.md](ARCHITECTURE.md) wyjaśnia granice programu, planowanych aplikacji i bibliotek. Szczegóły są w [docs/architecture](docs/architecture/README.md), uzasadnienia decyzji w [ADR](docs/adr/README.md), a [SECURITY.md](SECURITY.md), [GOVERNANCE.md](GOVERNANCE.md) i [model zagrożeń](docs/security/threat-model.md) opisują ochronę danych oraz odpowiedzialność. [Standard dokumentacji](docs/documentation.md) ogranicza długość plików administracyjnych, ale nie manuskryptów.

Publiczny opis programu znajduje się tylko w [pages/index.md](pages/index.md). Repozytorium nie zawiera workflow automatycznie publikującego Pages. Szczegóły: [polityka publikacji](docs/pages.md).

## Zasady

Nie należy traktować propozycji metod ani testów statystycznych jako prerejestracji. Każdy eksperyment z uczestnikami wymaga oceny etycznej i świadomej zgody według właściwych przepisów i procedur instytucji. Rejestrować pochodzenie danych, wersje sprzętu i oprogramowania, kryteria wykluczenia, podziały danych oraz odrębność zbioru testowego. Wyników i cytowań nie wolno uzupełniać bez źródeł i rzeczywistego materiału empirycznego.

Licencja znajduje się w pliku [LICENSE](LICENSE). Jej zakres nie zastępuje zgody na rozpowszechnianie cudzych zbiorów danych ani wizerunku i nagrań uczestników.
