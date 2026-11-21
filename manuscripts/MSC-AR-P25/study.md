# MSC-AR-P25 — plan badania i powiązania

**Temat:** Behawioralny koszt wstrzymania adaptacji XR wobec adaptacji statycznej i reaktywnej

**Program:** `arc-xr`. **Obszar:** `uncertainty-aware-adaptation`. **Typ:** `IDEA` (CANDIDATE). **Stan źródła:** `DETAILED_CONCEPT`. **Tryb integracji:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Cel, wynik główny i granice badania

Przedmiot badania: Behawioralny koszt wstrzymania adaptacji XR wobec adaptacji statycznej i reaktywnej. Kandydatura, bez zatwierdzonego odrębnego protokołu.

- **Główny wynik proponowany:** Odsetek błędów zadań i koszt zbędnych interwencji u użytkownika
- **Odrębność naukowa:** Weryfikacja skutku polityki odmowy w badaniu użytkowników; osobne pytanie wobec kalibracji predykatora XR-IDEA-11.
- **Uzasadnienie klasyfikacji:** Rozwinięcie pomysłu 11: cztery warunki Static/Performance/Neuroadaptive/Uncertainty-Aware; nie odrębny artykuł bez nowości. AUDYT DUPLIKACJI: rozwinięcie XR-IDEA-11 w jeden pełniejszy protokół; wskazać wspólne pochodzenie, nie mnożyć manuskryptów. | Proponowane doprecyzowanie zakresu portfolio 2026-11-20, wymaga zatwierdzenia naukowego: Weryfikacja skutku polityki odmowy w badaniu użytkowników; osobne pytanie wobec kalibracji predykatora XR-IDEA-11. Główny wynik do prerejestracji: Odsetek błędów zadań i koszt zbędnych interwencji u użytkownika. Tytuł źródłowy zachowano w original_title_pl.
- **Powiązane rekordy:** `MSC-AR-P17` (arc-xr:XR-IDEA-11), `MSC-AR-P01` (arc-xr:P01)

## Stanowisko badawcze

**Wstępne powiązanie:** `ST-03`. To propozycja na podstawie domeny, a nie potwierdzenie uruchomienia aparatury.

[Stanowiska ARC](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md); [inwentarz prywatny `devices`](https://github.com/MatPomGit/devices).

## Powiązane aplikacje APP

- `app-2d-desktop` (`APP-ARC-01D`), `OPTIONAL`, profil `desktop-browser`, bramka `RESEARCH_GO`.
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

- **UID źródłowy:** `arc-xr:XR-IDEA-19`; repozytorium `MatPomGit/arc-xr`, identyfikator `XR-IDEA-19`.
- **Ścieżka źródłowa:** `docs/pomysly.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/arc-xr/blob/main/docs/pomysly.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
