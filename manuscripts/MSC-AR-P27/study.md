# MSC-AR-P27 — plan badania i powiązania

**Temat:** Odporność adaptacyjnego HUD na błędy estymacji obciążenia poznawczego

**Program:** `arc-xr`. **Obszar:** `adaptive-cognitive-load`. **Typ:** `IDEA` (CANDIDATE). **Stan źródła:** `PROTOCOL_IDEA`. **Tryb integracji:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Cel, wynik główny i granice badania

Przedmiot badania: Odporność adaptacyjnego HUD na błędy estymacji obciążenia poznawczego. Kandydatura, bez zatwierdzonego odrębnego protokołu.

- **Główny wynik proponowany:** Dodatkowe błędy zadań i liczba niepożądanych zmian HUD w funkcji opóźnienia/dropout i bramkowania jakości
- **Odrębność naukowa:** Robustness adaptacji na błędnych sygnałach, zamiast zwykłej skuteczności statycznego vs adaptacyjnego HUD w MSC-AR-P01.
- **Uzasadnienie klasyfikacji:** Protokół eksperymentu, nie niezależny artykuł; pokrywa się z P01. AUDYT DUPLIKACJI: protokół P01 z powiązaną ideą XR-IDEA-01, nie osobny paper. | Proponowane doprecyzowanie zakresu portfolio 2026-11-20, wymaga zatwierdzenia naukowego: Dokument protokołu, nie drugi manuskrypt o adaptacji interfejsu AR. Główny wynik do prerejestracji: Nie dotyczy samodzielnego artykułu: implementacja procedury P01. Tytuł źródłowy zachowano w original_title_pl. | AUTORSKA PROPOZYCJA NOWEGO ARTYKUŁU 2026-11-20: w nowym planie MSC-AR-P27 zdefiniowano odrębny wynik. Nie zmienia to historycznego stanu PROTOCOL_IDEA ani decyzji w repozytorium źródłowym. Aktywacja art
- **Powiązane rekordy:** `MSC-AR-P01` (arc-xr:P01), `MSC-AR-P07` (arc-xr:XR-IDEA-01)

## Stanowisko badawcze

**Wstępne powiązanie:** `ST-03`. To propozycja na podstawie domeny, a nie potwierdzenie uruchomienia aparatury.

[Stanowiska ARC](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md); [inwentarz prywatny `devices`](https://github.com/MatPomGit/devices).

## Powiązane aplikacje APP

- `app-2d-desktop` (`APP-ARC-01D`), `COMPARATOR`, profil `desktop-browser`, bramka `RESEARCH_GO`.
- `app-xr` (`APP-ARC-07`), `OPTIONAL`, profil `unity-openxr`, bramka `RESEARCH_GO`.

## Powiązane biblioteki LIB

- `lib-asr`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-events`: planowana zależność pośrednia przez `app-2d-desktop`, `app-xr`; brak dowodu integracji.
- `lib-eye`: planowana zależność pośrednia przez `app-2d-desktop`; brak dowodu integracji.
- `lib-image` (historyczna nazwa; wymaga uzgodnienia z `lib-vis`): planowana zależność pośrednia przez `app-2d-desktop`, `app-xr`; brak dowodu integracji.
- `lib-study`: planowana zależność pośrednia przez `app-2d-desktop`; brak dowodu integracji.
- `lib-unity`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-vlm`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-voice`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `OptiCore`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.

Relacje APP i LIB pochodzą odpowiednio z `app_publication_links.csv` i `component_dependencies.csv`. Są kandydaturami, nie dowodami wykonania prac. Aktualność nazw `lib-signals`, `lib-image` i `lib-llm` wymaga osobnego uzgodnienia z nowymi repozytoriami.

## Proweniencja, metodologia i bramki

- **UID źródłowy:** `arc-xr:PROTO-AR-01`; repozytorium `MatPomGit/arc-xr`, identyfikator `PROTO-AR-01`.
- **Ścieżka źródłowa:** `docs/aparatura_ar_ai.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/arc-xr/blob/main/docs/aparatura_ar_ai.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
