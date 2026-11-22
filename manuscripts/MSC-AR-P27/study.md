# MSC-AR-P27 — Odporność adaptacyjnego HUD na błędy estymacji obciążenia poznawczego

**Program:** `arc-xr` · **obszar:** `adaptive-cognitive-load` · **rodzaj:** `IDEA` · **etap źródłowy:** `PROTOCOL_IDEA`.

## Projekt badania

**Przedmiot:** Odporność adaptacyjnego HUD na błędy estymacji obciążenia poznawczego.

- **Proponowany wynik główny:** Dodatkowe błędy zadań i liczba niepożądanych zmian HUD w funkcji opóźnienia/dropout i bramkowania jakości
- **Odrębność i ograniczenia:** Robustness adaptacji na błędnych sygnałach, zamiast zwykłej skuteczności statycznego vs adaptacyjnego HUD w MSC-AR-P01.
- **Plan metodologii:** należy ustalić hipotezy, próbę lub scenariusze, procedurę, metryki, plan weryfikacji i analizę wrażliwości; samo istnienie pliku nie oznacza ukończenia badania.
- **Powiązane MSC:** `MSC-AR-P01`, `MSC-AR-P07`.

## Stanowisko badawcze

**`ST-03`**: status `PROPOSED_BY_SCOPE`, kwalifikacja aparatury `NOT_VERIFIED`. Jest to mapa planistyczna, nie raport uruchomionego stanowiska.

## Aplikacje

- **`app-2d-desktop`** (`APP-ARC-01D`): rola `COMPARATOR`, bramka `RESEARCH_GO`, status repozytorium `PLANNED_NOT_CREATED`.
- **`app-xr`** (`APP-ARC-07`): rola `OPTIONAL`, bramka `RESEARCH_GO`, status repozytorium `PLANNED_NOT_CREATED`.

## Biblioteki

- **`lib-audio`**: `SCOPE_CONSOLIDATED_PLAN`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-events`**: `PLANNED_NOT_CREATED`, powiązanie planowane przez `app-2d-desktop`, `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-eye`**: `SCAFFOLD_EXISTS`, powiązanie planowane przez `app-2d-desktop`; wykonanie integracji niezweryfikowane.
- **`lib-study`**: `PLANNED_NOT_CREATED`, powiązanie planowane przez `app-2d-desktop`; wykonanie integracji niezweryfikowane.
- **`lib-track`**: `NEW_SCAFFOLD_EXISTS`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-unity`**: `SCAFFOLD_EXISTS`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-vis`**: `RENAMED_ARCHITECTURE_ONLY`, powiązanie planowane przez `app-2d-desktop`, `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-vlm`**: `SCAFFOLD_EXISTS`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.
- **`OptiCore`**: `PRIVATE_REPOSITORY_EXISTS`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.

## Proweniencja i bramki

Źródło opisuje publiczny projekt [`arc-xr`](https://github.com/MatPomGit/arc-xr); pierwotny identyfikator `PROTO-AR-01`.

Weryfikacja badania wymaga oceny praw do danych, niezależności wyniku, sposobu doboru próby, etyki i bezpieczeństwa stanowiska, o ile dotyczą tematu. Wszystkie zależności oprogramowania są **kandydaturami**, nie zatwierdzonymi wdrożeniami. Nie przedstawiono nieistniejących pomiarów ani statystyk.
