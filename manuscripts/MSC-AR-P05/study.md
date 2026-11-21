# MSC-AR-P05 — plan badania i powiązania

**Temat:** Weryfikacja poprawności sekwencji manualnej w AR na podstawie dowodów wizualnych

**Program:** `arc-xr`. **Obszar:** `immersive-interaction`. **Typ:** `MANUSCRIPT` (MANUSCRIPT). **Stan źródła:** `PLANNED`. **Tryb integracji:** `LINK_ONLY`.

## Cel, wynik główny i granice badania

Przedmiot badania: Weryfikacja poprawności sekwencji manualnej w AR na podstawie dowodów wizualnych. Istnieje ślad źródłowego manuskryptu; stan dowodów wymaga weryfikacji.

- **Główny wynik proponowany:** Odsetek wykrytych błędów kolejności działań i błędnych alarmów
- **Odrębność naukowa:** Weryfikacja etapów procedury, nie grounding obiektów P04 ani faza podania wskazówki MSC-AR-P25.
- **Uzasadnienie klasyfikacji:** Klasyfikacja wg pytania badawczego: Wkład XR: temporalna kontrola kroków procedury i wskazówki przestrzenne. Status źródła: PLANNED. Nie oznacza zatwierdzonych danych ani gotowości publikacji. | Proponowane doprecyzowanie zakresu portfolio 2026-11-20, wymaga zatwierdzenia naukowego: Weryfikacja etapów procedury, nie grounding obiektów P04 ani faza podania wskazówki MSC-AR-P25. Główny wynik do prerejestracji: Odsetek wykrytych błędów kolejności działań i błędnych alarmów. Tytuł źródłowy zachowano w original_title_pl. Nie zmienia to zatwierdzonego tytułu manuskryptu źródłowego ani zamrożonego protokołu.
- **Powiązane rekordy:** `MSC-AR-P28` (arc-xr:PROTO-AR-02)

## Stanowisko badawcze

**Wstępne powiązanie:** `ST-03`. To propozycja na podstawie domeny, a nie potwierdzenie uruchomienia aparatury.

[Stanowiska ARC](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md); [inwentarz prywatny `devices`](https://github.com/MatPomGit/devices).

## Powiązane aplikacje APP

- `app-xr` (`APP-ARC-07`), `OPTIONAL`, profil `unity-openxr`, bramka `RESEARCH_GO`.

## Powiązane biblioteki LIB

- `lib-asr`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-events`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-image` (historyczna nazwa; wymaga uzgodnienia z `lib-vis`): planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-unity`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-vlm`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-voice`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `OptiCore`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.

Relacje APP i LIB pochodzą odpowiednio z `app_publication_links.csv` i `component_dependencies.csv`. Są kandydaturami, nie dowodami wykonania prac. Aktualność nazw `lib-signals`, `lib-image` i `lib-llm` wymaga osobnego uzgodnienia z nowymi repozytoriami.

## Proweniencja, metodologia i bramki

- **UID źródłowy:** `arc-xr:P05`; repozytorium `MatPomGit/arc-xr`, identyfikator `P05`.
- **Ścieżka źródłowa:** `manuscripts/P05/README.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/arc-xr/blob/main/manuscripts/P05/README.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
