# MSC-AR-P26 — plan badania i powiązania

**Temat:** Faza ruchu dłoni a optymalny moment wyświetlania instrukcji w AR

**Program:** `arc-xr`. **Obszar:** `motor-phase-timing-ar-guidance`. **Typ:** `IDEA` (CANDIDATE). **Stan źródła:** `NEW_CROSS_PROGRAM_IDEA_HOLD`. **Tryb integracji:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Cel, wynik główny i granice badania

Przedmiot badania: Faza ruchu dłoni a optymalny moment wyświetlania instrukcji w AR. Kandydatura, bez zatwierdzonego odrębnego protokołu.

- **Główny wynik proponowany:** Nieokreślony w rejestrze. Wymaga zdefiniowania metryki, estymandu i jednostki analizy przed rozpoczęciem badania.
- **Odrębność naukowa:** Należy porównać źródłowy protokół z pokrewnymi manuskryptami przed formalizacją hipotezy.
- **Uzasadnienie klasyfikacji:** [Nowa propozycja burzy mózgów 2026-11-20, priorytet B] Identyczne wskazówki AR przed ruchem vs podczas ruchu przy tej samej liczbie podpowiedzi, primary błędy kolejności. Leap opcjonalny po kwalifikacji; standardowy Quest 3 bez gaze. Sprawdzić ISMAR/CHI 2025 prior art, odrębne od weryfikacji kroków P05. Wkład i nowość niezatwierdzone; nie tworzyć manuskryptu przed audytem. Propozycja znajduje się w dokumentacji programu, w otwartym PR, bez wpisu do katalogu zatwierdzonych publikacji.
- **Powiązane rekordy:** `MSC-AR-P05` (arc-xr:P05), `MSC-AFFECT-P05` (arc-affective:P05), `MSC-AR-P28` (arc-xr:PROTO-AR-02)

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

- **UID źródłowy:** `arc-xr:XR-IDEA-20`; repozytorium `MatPomGit/arc-xr`, identyfikator `XR-IDEA-20`.
- **Ścieżka źródłowa:** `docs/research-proposals-2026.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/arc-xr/blob/12c6204b684fe649d14f78c7fcfa62ca70d3f018/docs/research-proposals-2026.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
