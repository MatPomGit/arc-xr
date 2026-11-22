# MSC-AR-P29 — Predykcja subiektywnej niepewności decyzji z mikroruchów dłoni, spojrzenia i EEG

**Program:** `arc-xr` · **obszar:** `multimodal-decision-uncertainty` · **rodzaj:** `IDEA` · **etap źródłowy:** `PROTOCOL_IDEA`.

## Projekt badania

**Przedmiot:** Predykcja subiektywnej niepewności decyzji z mikroruchów dłoni, spojrzenia i EEG.

- **Proponowany wynik główny:** Błąd przewidywania subiektywnej pewności 1–5 i kalibracja rozkładu ocen przy walidacji na niezależnych uczestnikach
- **Odrębność i ograniczenia:** Metodologiczny wynik dotyczący pewności decyzji, nie przeciążenia w MSC-AR-P01 ani proxy wymagań zadania w MSC-AFFECT-P05.
- **Plan metodologii:** należy ustalić hipotezy, próbę lub scenariusze, procedurę, metryki, plan weryfikacji i analizę wrażliwości; samo istnienie pliku nie oznacza ukończenia badania.
- **Powiązane MSC:** `MSC-AR-P01`, `MSC-AFFECT-P05`.

## Stanowisko badawcze

**`ST-03`**: status `PROPOSED_BY_SCOPE`, kwalifikacja aparatury `NOT_VERIFIED`. Jest to mapa planistyczna, nie raport uruchomionego stanowiska.

## Aplikacje

- **`app-eeg-neurolyze`** (`APP-ARC-03`): rola `OPTIONAL`, bramka `RESEARCH_GO`, status repozytorium `ALTERNATE_EXISTING_APP`, istniejący odpowiednik `eeg-neurolyze`.
- **`app-eye-desktop`** (`APP-ARC-05`): rola `SIGNAL_SOURCE`, bramka `DEVICE_RIGHTS`, status repozytorium `PLANNED_NOT_CREATED`.
- **`app-xr`** (`APP-ARC-07`): rola `OPTIONAL`, bramka `RESEARCH_GO`, status repozytorium `PLANNED_NOT_CREATED`.

## Biblioteki

- **`lib-audio`**: `SCOPE_CONSOLIDATED_PLAN`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-events`**: `PLANNED_NOT_CREATED`, powiązanie planowane przez `app-eeg-neurolyze`, `app-eye-desktop`, `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-eye`**: `SCAFFOLD_EXISTS`, powiązanie planowane przez `app-eye-desktop`; wykonanie integracji niezweryfikowane.
- **`lib-sig`**: `RENAMED_PARTIAL_CORE`, powiązanie planowane przez `app-eeg-neurolyze`; wykonanie integracji niezweryfikowane.
- **`lib-sim`**: `PLANNED_NOT_CREATED`, powiązanie planowane przez `app-eeg-neurolyze`; wykonanie integracji niezweryfikowane.
- **`lib-track`**: `NEW_SCAFFOLD_EXISTS`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-unity`**: `SCAFFOLD_EXISTS`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-vis`**: `RENAMED_ARCHITECTURE_ONLY`, powiązanie planowane przez `app-eye-desktop`, `app-xr`; wykonanie integracji niezweryfikowane.
- **`lib-vlm`**: `SCAFFOLD_EXISTS`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.
- **`OptiCore`**: `PRIVATE_REPOSITORY_EXISTS`, powiązanie planowane przez `app-xr`; wykonanie integracji niezweryfikowane.

## Proweniencja i bramki

Źródło opisuje publiczny projekt [`arc-xr`](https://github.com/MatPomGit/arc-xr); pierwotny identyfikator `PROTO-AR-03`.

Weryfikacja badania wymaga oceny praw do danych, niezależności wyniku, sposobu doboru próby, etyki i bezpieczeństwa stanowiska, o ile dotyczą tematu. Wszystkie zależności oprogramowania są **kandydaturami**, nie zatwierdzonymi wdrożeniami. Nie przedstawiono nieistniejących pomiarów ani statystyk.
