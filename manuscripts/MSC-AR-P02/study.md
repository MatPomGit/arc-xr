# MSC-AR-P02 — plan badania i powiązania

**Temat:** Frustracja i dekoncentracja w procedurach manualnych AR

**Program:** `arc-xr`. **Obszar:** `immersive-interaction`. **Typ:** `MANUSCRIPT` (MANUSCRIPT). **Stan źródła:** `PLANNED`. **Tryb integracji:** `LINK_ONLY`.

## Cel, wynik główny i granice badania

Przedmiot badania: Frustracja i dekoncentracja w procedurach manualnych AR. Istnieje ślad źródłowego manuskryptu; stan dowodów wymaga weryfikacji.

- **Główny wynik proponowany:** Nieokreślony w rejestrze. Wymaga zdefiniowania metryki, estymandu i jednostki analizy przed rozpoczęciem badania.
- **Odrębność naukowa:** Należy porównać źródłowy protokół z pokrewnymi manuskryptami przed formalizacją hipotezy.
- **Uzasadnienie klasyfikacji:** Klasyfikacja wg pytania badawczego: Główny kontrast: interakcja i dekoncentracja użytkownika w zadaniach AR. Status źródła: PLANNED. Nie oznacza zatwierdzonych danych ani gotowości publikacji.
- **Powiązane rekordy:** Nie zarejestrowano.

## Stanowisko badawcze

**Wstępne powiązanie:** `ST-03`. To propozycja na podstawie domeny, a nie potwierdzenie uruchomienia aparatury.

[Stanowiska ARC](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md); [inwentarz prywatny `devices`](https://github.com/MatPomGit/devices).

## Powiązane aplikacje APP

- `app-2d-desktop` (`APP-ARC-01D`), `COMPARATOR`, profil `desktop-browser`, bramka `RESEARCH_GO`.
- `app-eye-desktop` (`APP-ARC-05`), `SIGNAL_SOURCE`, profil `desktop-webcam`, bramka `DEVICE_RIGHTS`.
- `app-xr` (`APP-ARC-07`), `OPTIONAL`, profil `unity-openxr`, bramka `RESEARCH_GO`.

## Powiązane biblioteki LIB

- `lib-asr`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-events`: planowana zależność pośrednia przez `app-2d-desktop`, `app-eye-desktop`, `app-xr`; brak dowodu integracji.
- `lib-eye`: planowana zależność pośrednia przez `app-2d-desktop`, `app-eye-desktop`; brak dowodu integracji.
- `lib-image` (historyczna nazwa; wymaga uzgodnienia z `lib-vis`): planowana zależność pośrednia przez `app-2d-desktop`, `app-eye-desktop`, `app-xr`; brak dowodu integracji.
- `lib-study`: planowana zależność pośrednia przez `app-2d-desktop`; brak dowodu integracji.
- `lib-unity`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-vlm`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-voice`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `OptiCore`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.

Relacje APP i LIB pochodzą odpowiednio z `app_publication_links.csv` i `component_dependencies.csv`. Są kandydaturami, nie dowodami wykonania prac. Aktualność nazw `lib-signals`, `lib-image` i `lib-llm` wymaga osobnego uzgodnienia z nowymi repozytoriami.

## Proweniencja, metodologia i bramki

- **UID źródłowy:** `arc-xr:P02`; repozytorium `MatPomGit/arc-xr`, identyfikator `P02`.
- **Ścieżka źródłowa:** `manuscripts/P02/README.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/arc-xr/blob/main/manuscripts/P02/README.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
