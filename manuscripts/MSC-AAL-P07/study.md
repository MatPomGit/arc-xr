# MSC-AAL-P07 — plan badania i powiązania

**Temat:** Pomoc przestrzenna AR wobec interfejsu 2D w wykonywaniu bezpiecznych czynności domowych

**Program:** `arc-xr`. **Obszar:** `spatial-adl-guidance`. **Typ:** `IDEA` (CANDIDATE). **Stan źródła:** `NEW_CROSS_DOMAIN_IDEA_HOLD`. **Tryb integracji:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Cel, wynik główny i granice badania

Przedmiot badania: Pomoc przestrzenna AR wobec interfejsu 2D w wykonywaniu bezpiecznych czynności domowych. Kandydatura, bez zatwierdzonego odrębnego protokołu.

- **Główny wynik proponowany:** Nieokreślony w rejestrze. Wymaga zdefiniowania metryki, estymandu i jednostki analizy przed rozpoczęciem badania.
- **Odrębność naukowa:** Należy porównać źródłowy protokół z pokrewnymi manuskryptami przed formalizacją hipotezy.
- **Uzasadnienie klasyfikacji:** Nowy warunkowy kontrast AR vs 2D przy tej samej treści i niezależnym wyniku poprawności procedury w wirtualnym domu. Odrębność od XR P05 i AAL P02 wymaga audytu nowości. Najpierw nieaktywne atrapy urządzeń, bez ryzykownych działań i bez niezaplanowanych badań ludzi.
- **Powiązane rekordy:** `MSC-AAL-P02` (carehome-aal:AAL-P02), `MSC-AR-P05` (arc-xr:P05), `MSC-AR-P06` (arc-xr:P06)

## Stanowisko badawcze

**Wstępne powiązanie:** `ST-06`. To propozycja na podstawie domeny, a nie potwierdzenie uruchomienia aparatury.

[Stanowiska ARC](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md); [inwentarz prywatny `devices`](https://github.com/MatPomGit/devices).

## Powiązane aplikacje APP

- `app-2d-desktop` (`APP-ARC-01D`), `COMPARATOR`, profil `desktop-browser`, bramka `RESEARCH_GO`.
- `app-xr` (`APP-ARC-07`), `OPTIONAL`, profil `unity-openxr`, bramka `RESEARCH_GO`.
- `app-carehome` (`APP-ARC-09`), `OPTIONAL`, profil `aal-simulator`, bramka `RESEARCH_GO`.

## Powiązane biblioteki LIB

- `lib-adapt`: planowana zależność pośrednia przez `app-carehome`; brak dowodu integracji.
- `lib-asr`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-events`: planowana zależność pośrednia przez `app-2d-desktop`, `app-xr`, `app-carehome`; brak dowodu integracji.
- `lib-eye`: planowana zależność pośrednia przez `app-2d-desktop`; brak dowodu integracji.
- `lib-image` (historyczna nazwa; wymaga uzgodnienia z `lib-vis`): planowana zależność pośrednia przez `app-2d-desktop`, `app-xr`; brak dowodu integracji.
- `lib-llm` (historyczna nazwa; wymaga uzgodnienia z `lib-vlm`): planowana zależność pośrednia przez `app-carehome`; brak dowodu integracji.
- `lib-sim`: planowana zależność pośrednia przez `app-carehome`; brak dowodu integracji.
- `lib-study`: planowana zależność pośrednia przez `app-2d-desktop`; brak dowodu integracji.
- `lib-unity`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-vlm`: planowana zależność pośrednia przez `app-xr`, `app-carehome`; brak dowodu integracji.
- `lib-voice`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `OptiCore`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.

Relacje APP i LIB pochodzą odpowiednio z `app_publication_links.csv` i `component_dependencies.csv`. Są kandydaturami, nie dowodami wykonania prac. Aktualność nazw `lib-signals`, `lib-image` i `lib-llm` wymaga osobnego uzgodnienia z nowymi repozytoriami.

## Proweniencja, metodologia i bramki

- **UID źródłowy:** `cross-arc:CROSS-ARC-02`; repozytorium `MatPomGit/research-autopilot`, identyfikator `CROSS-ARC-02`.
- **Ścieżka źródłowa:** `docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/research-autopilot/blob/c397169d8630090f38bacf091947cc47083f006c/docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
