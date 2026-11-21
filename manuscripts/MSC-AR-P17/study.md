# MSC-AR-P17 — plan badania i powiązania

**Temat:** Kalibracja niepewności rozpoznania stanu użytkownika a selektywna abstencja adaptatora XR

**Program:** `arc-xr`. **Obszar:** `uncertainty-aware-adaptation`. **Typ:** `IDEA` (CANDIDATE). **Stan źródła:** `IDEA_UNREVIEWED`. **Tryb integracji:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Cel, wynik główny i granice badania

Przedmiot badania: Kalibracja niepewności rozpoznania stanu użytkownika a selektywna abstencja adaptatora XR. Kandydatura, bez zatwierdzonego odrębnego protokołu.

- **Główny wynik proponowany:** Krzywa selektywnego ryzyka i pokrycia decyzji o adaptacji
- **Odrębność naukowa:** Metoda selekcji / ocena prawdopodobieństwa abstencji; nie efekt behawioralny odrzucenia adaptacji.
- **Uzasadnienie klasyfikacji:** Silny związek z rozwinięciem When Should Neuroadaptive XR NOT Adapt. AUDYT DUPLIKACJI: to pierwotna wersja hipotezy rozwiniętej w XR-IDEA-19; nie planować dwóch samodzielnych publikacji. | Proponowane doprecyzowanie zakresu portfolio 2026-11-20, wymaga zatwierdzenia naukowego: Metoda selekcji / ocena prawdopodobieństwa abstencji; nie efekt behawioralny odrzucenia adaptacji. Główny wynik do prerejestracji: Krzywa selektywnego ryzyka i pokrycia decyzji o adaptacji. Tytuł źródłowy zachowano w original_title_pl.
- **Powiązane rekordy:** `MSC-AR-P01` (arc-xr:P01), `MSC-AR-P25` (arc-xr:XR-IDEA-19)

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

- **UID źródłowy:** `arc-xr:XR-IDEA-11`; repozytorium `MatPomGit/arc-xr`, identyfikator `XR-IDEA-11`.
- **Ścieżka źródłowa:** `docs/pomysly.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/arc-xr/blob/main/docs/pomysly.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
