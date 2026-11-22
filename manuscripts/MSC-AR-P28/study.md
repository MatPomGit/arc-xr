# MSC-AR-P28 — Wyprzedzające wykrywanie ryzyka błędu manipulacji z kinematyki dłoni i VLM

**Program:** `arc-xr` · **obszar:** `spatial-vlm` · **rodzaj:** `IDEA` · **etap źródłowy:** `PROTOCOL_IDEA`.

## Projekt badania

**Przedmiot:** Wyprzedzające wykrywanie ryzyka błędu manipulacji z kinematyki dłoni i VLM.

- **Proponowany wynik główny:** Czułość wykrycia niewłaściwego chwytu przed kontaktem przy ustalonym limicie fałszywych alarmów i czasie wyprzedzenia
- **Odrębność i ograniczenia:** Predykcja ryzyka przed wykonaniem czynności, nie przestrzenne przypisanie VLM MSC-AR-P04 lub detekcja pominiętych kroków MSC-AR-P05.
- **Plan metodologii:** należy ustalić hipotezy, próbę lub scenariusze, procedurę, metryki, plan weryfikacji i analizę wrażliwości; samo istnienie pliku nie oznacza ukończenia badania.
- **Powiązane MSC:** `MSC-AR-P04`, `MSC-AR-P05`.

## Stanowisko badawcze

**`ST-03`**: status `PROPOSED_BY_SCOPE`, kwalifikacja aparatury `NOT_VERIFIED`. Jest to mapa planistyczna, nie raport uruchomionego stanowiska.

## Aplikacje

- **`app-xr`** (`APP-ARC-07`): rola `OPTIONAL`, bramka `RESEARCH_GO`, status repozytorium `PLANNED_NOT_CREATED`.

## Biblioteki

- **`lib-audio`**: `SCOPE_CONSOLIDATED_PLAN`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-events`**: `PLANNED_NOT_CREATED`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-track`**: `NEW_SCAFFOLD_EXISTS`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-unity`**: `SCAFFOLD_EXISTS`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-vis`**: `RENAMED_ARCHITECTURE_ONLY`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-vlm`**: `SCAFFOLD_EXISTS`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.
- **`OptiCore`**: `PRIVATE_REPOSITORY_EXISTS`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.

## Proweniencja i bramki

Źródło opisuje publiczny projekt [`arc-xr`](https://github.com/MatPomGit/arc-xr); pierwotny identyfikator `PROTO-AR-02`.

Weryfikacja badania wymaga oceny praw do danych, niezależności wyniku, sposobu doboru próby, etyki i bezpieczeństwa stanowiska, o ile dotyczą tematu. Wszystkie zależności oprogramowania są **kandydaturami**, nie zatwierdzonymi wdrożeniami. Nie przedstawiono nieistniejących pomiarów ani statystyk.
