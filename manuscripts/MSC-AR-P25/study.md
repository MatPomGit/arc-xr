# MSC-AR-P25 — Behawioralny koszt wstrzymania adaptacji XR wobec adaptacji statycznej i reaktywnej

**Program:** `arc-xr` · **obszar:** `uncertainty-aware-adaptation` · **rodzaj:** `IDEA` · **etap źródłowy:** `DETAILED_CONCEPT`.

## Projekt badania

**Przedmiot:** Behawioralny koszt wstrzymania adaptacji XR wobec adaptacji statycznej i reaktywnej.

- **Proponowany wynik główny:** Odsetek błędów zadań i koszt zbędnych interwencji u użytkownika
- **Odrębność i ograniczenia:** Weryfikacja skutku polityki odmowy w badaniu użytkowników; osobne pytanie wobec kalibracji predykatora XR-IDEA-11.
- **Plan metodologii:** należy ustalić hipotezy, próbę lub scenariusze, procedurę, metryki, plan weryfikacji i analizę wrażliwości; samo istnienie pliku nie oznacza ukończenia badania.
- **Powiązane MSC:** `MSC-AR-P17`, `MSC-AR-P01`.

## Stanowisko badawcze

**`ST-03`**: status `PROPOSED_BY_SCOPE`, kwalifikacja aparatury `NOT_VERIFIED`. Jest to mapa planistyczna, nie raport uruchomionego stanowiska.

## Aplikacje

- **`app-2d-desktop`** (`APP-ARC-01D`): rola `OPTIONAL`, bramka `RESEARCH_GO`, status repozytorium `PLANNED_NOT_CREATED`.
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

Źródło opisuje publiczny projekt [`arc-xr`](https://github.com/MatPomGit/arc-xr); pierwotny identyfikator `XR-IDEA-19`.

Weryfikacja badania wymaga oceny praw do danych, niezależności wyniku, sposobu doboru próby, etyki i bezpieczeństwa stanowiska, o ile dotyczą tematu. Wszystkie zależności oprogramowania są **kandydaturami**, nie zatwierdzonymi wdrożeniami. Nie przedstawiono nieistniejących pomiarów ani statystyk.
