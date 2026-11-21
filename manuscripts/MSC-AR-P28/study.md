# MSC-AR-P28 — plan badania i powiązania

**Temat:** Wyprzedzające wykrywanie ryzyka błędu manipulacji z kinematyki dłoni i VLM

**Program:** `arc-xr`. **Obszar:** `spatial-vlm`. **Typ:** `IDEA` (CANDIDATE). **Stan źródła:** `PROTOCOL_IDEA`. **Tryb integracji:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Cel, wynik główny i granice badania

Przedmiot badania: Wyprzedzające wykrywanie ryzyka błędu manipulacji z kinematyki dłoni i VLM. Kandydatura, bez zatwierdzonego odrębnego protokołu.

- **Główny wynik proponowany:** Czułość wykrycia niewłaściwego chwytu przed kontaktem przy ustalonym limicie fałszywych alarmów i czasie wyprzedzenia
- **Odrębność naukowa:** Predykcja ryzyka przed wykonaniem czynności, nie przestrzenne przypisanie VLM MSC-AR-P04 lub detekcja pominiętych kroków MSC-AR-P05.
- **Uzasadnienie klasyfikacji:** Protokół eksperymentu, nie niezależny artykuł; powiązany z P04/P05. AUDYT DUPLIKACJI: to wspólny protokół sceny P04/P05, nie trzecia publikacja. | Proponowane doprecyzowanie zakresu portfolio 2026-11-20, wymaga zatwierdzenia naukowego: Wspólna procedura eksperymentalna dla odrębnych wyników groundingu i kontroli kroków. Główny wynik do prerejestracji: Nie dotyczy samodzielnego artykułu: procedura wspólna P04/P05. Tytuł źródłowy zachowano w original_title_pl. | AUTORSKA PROPOZYCJA NOWEGO ARTYKUŁU 2026-11-20: w nowym planie MSC-AR-P28 zdefiniowano odrębny wynik. Nie zmienia to historycznego stanu PROTOCOL_IDEA ani decyzji w repozytorium źródłow
- **Powiązane rekordy:** `MSC-AR-P04` (arc-xr:P04), `MSC-AR-P05` (arc-xr:P05)

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

- **UID źródłowy:** `arc-xr:PROTO-AR-02`; repozytorium `MatPomGit/arc-xr`, identyfikator `PROTO-AR-02`.
- **Ścieżka źródłowa:** `docs/aparatura_ar_ai.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/arc-xr/blob/main/docs/aparatura_ar_ai.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
