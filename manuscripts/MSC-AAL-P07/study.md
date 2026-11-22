# MSC-AAL-P07 — Pomoc przestrzenna AR wobec interfejsu 2D w wykonywaniu bezpiecznych czynności domowych

**Program:** `arc-xr` · **obszar:** `spatial-adl-guidance` · **rodzaj:** `IDEA` · **etap źródłowy:** `NEW_CROSS_DOMAIN_IDEA_HOLD`.

## Projekt badania

**Przedmiot:** Pomoc przestrzenna AR wobec interfejsu 2D w wykonywaniu bezpiecznych czynności domowych.

- **Proponowany wynik główny:** Wymaga określenia estymandu, głównej miary i jednostki analizy przed rozpoczęciem zbierania danych.
- **Odrębność i ograniczenia:** Przed zatwierdzeniem wymagany przegląd źródłowego protokołu i pokrewnych publikacji.
- **Plan metodologii:** należy ustalić hipotezy, próbę lub scenariusze, procedurę, metryki, plan weryfikacji i analizę wrażliwości; samo istnienie pliku nie oznacza ukończenia badania.
- **Powiązane MSC:** `MSC-AAL-P02`, `MSC-AR-P05`, `MSC-AR-P06`.

## Stanowisko badawcze

**`ST-03`**: status `PROPOSED_BY_SCOPE`, kwalifikacja aparatury `NOT_VERIFIED`. Jest to mapa planistyczna, nie raport uruchomionego stanowiska.

## Aplikacje

- **`app-2d-desktop`** (`APP-ARC-01D`): rola `COMPARATOR`, bramka `RESEARCH_GO`, status repozytorium `PLANNED_NOT_CREATED`.
- **`app-xr`** (`APP-ARC-07`): rola `OPTIONAL`, bramka `RESEARCH_GO`, status repozytorium `PLANNED_NOT_CREATED`.
- **`app-carehome`** (`APP-ARC-09`): rola `OPTIONAL`, bramka `RESEARCH_GO`, status repozytorium `PLANNED_NOT_CREATED`.

## Biblioteki

- **`lib-adapt`**: `PLANNED_NOT_CREATED`, powiązanie planowane przez `app-carehome`; wykonanie integracji niezweryfikowane.
- **`lib-audio`**: `SCOPE_CONSOLIDATED_PLAN`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-events`**: `PLANNED_NOT_CREATED`, powiązanie planowane przez `app-2d-desktop`, `app-xr`, `app-carehome`; wykonanie integracji niezweryfikowane.
- **`lib-eye`**: `SCAFFOLD_EXISTS`, powiązanie planowane przez `app-2d-desktop`; wykonanie integracji niezweryfikowane.
- **`lib-sim`**: `PLANNED_NOT_CREATED`, powiązanie planowane przez `app-carehome`; wykonanie integracji niezweryfikowane.
- **`lib-study`**: `PLANNED_NOT_CREATED`, powiązanie planowane przez `app-2d-desktop`; wykonanie integracji niezweryfikowane.
- **`lib-track`**: `NEW_SCAFFOLD_EXISTS`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-unity`**: `SCAFFOLD_EXISTS`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-vis`**: `RENAMED_ARCHITECTURE_ONLY`, powiązanie planowane przez `app-2d-desktop`, `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-vlm`**: `SCAFFOLD_EXISTS`, powiązanie planowane przez `app-xr`, `app-carehome`; wykonanie integracji niezweryfikowane.
- **`OptiCore`**: `PRIVATE_REPOSITORY_EXISTS`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.

## Proweniencja i bramki

Dane o niepublicznych repozytoriach i pełnej historii pochodzenia znajdują się poza dokumentacją publiczną.

Weryfikacja badania wymaga oceny praw do danych, niezależności wyniku, sposobu doboru próby, etyki i bezpieczeństwa stanowiska, o ile dotyczą tematu. Wszystkie zależności oprogramowania są **kandydaturami**, nie zatwierdzonymi wdrożeniami. Nie przedstawiono nieistniejących pomiarów ani statystyk.
