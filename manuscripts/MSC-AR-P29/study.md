# MSC-AR-P29 — plan badania i powiązania

**Temat:** Predykcja subiektywnej niepewności decyzji z mikroruchów dłoni, spojrzenia i EEG

**Program:** `arc-xr`. **Obszar:** `multimodal-decision-uncertainty`. **Typ:** `IDEA` (CANDIDATE). **Stan źródła:** `PROTOCOL_IDEA`. **Tryb integracji:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Cel, wynik główny i granice badania

Przedmiot badania: Predykcja subiektywnej niepewności decyzji z mikroruchów dłoni, spojrzenia i EEG. Kandydatura, bez zatwierdzonego odrębnego protokołu.

- **Główny wynik proponowany:** Błąd przewidywania subiektywnej pewności 1–5 i kalibracja rozkładu ocen przy walidacji na niezależnych uczestnikach
- **Odrębność naukowa:** Metodologiczny wynik dotyczący pewności decyzji, nie przeciążenia w MSC-AR-P01 ani proxy wymagań zadania w MSC-AFFECT-P05.
- **Uzasadnienie klasyfikacji:** Protokół kandydacki; niezależność wobec pomiaru obciążenia i kinematyki dłoni do oceny. | Proponowane doprecyzowanie zakresu portfolio 2026-11-20, wymaga zatwierdzenia naukowego: Źródłowa procedura, bez potwierdzonego osobnego estimandu względem XR P01/Affective P05. Główny wynik do prerejestracji: Nie dotyczy samodzielnego artykułu: protokół pomiarowy do audytu. Tytuł źródłowy zachowano w original_title_pl. | AUTORSKA PROPOZYCJA NOWEGO ARTYKUŁU 2026-11-20: w nowym planie MSC-AR-P29 zdefiniowano odrębny wynik. Nie zmienia to historycznego stanu PROTOCOL_IDEA ani decyzji w repozytorium źródłowym. Aktywacja artykułu wymaga nowej oceny metodolog
- **Powiązane rekordy:** `MSC-AR-P01` (arc-xr:P01), `MSC-AFFECT-P05` (arc-affective:P05)

## Stanowisko badawcze

**Wstępne powiązanie:** `ST-03`. To propozycja na podstawie domeny, a nie potwierdzenie uruchomienia aparatury.

[Stanowiska ARC](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md); [inwentarz prywatny `devices`](https://github.com/MatPomGit/devices).

## Powiązane aplikacje APP

- `app-eeg-neurolyze` (`APP-ARC-03`), `OPTIONAL`, profil `python-eeg`, bramka `RESEARCH_GO`.
- `app-eye-desktop` (`APP-ARC-05`), `SIGNAL_SOURCE`, profil `desktop-webcam`, bramka `DEVICE_RIGHTS`.
- `app-xr` (`APP-ARC-07`), `OPTIONAL`, profil `unity-openxr`, bramka `RESEARCH_GO`.

## Powiązane biblioteki LIB

- `lib-asr`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-events`: planowana zależność pośrednia przez `app-eeg-neurolyze`, `app-eye-desktop`, `app-xr`; brak dowodu integracji.
- `lib-eye`: planowana zależność pośrednia przez `app-eye-desktop`; brak dowodu integracji.
- `lib-image` (historyczna nazwa; wymaga uzgodnienia z `lib-vis`): planowana zależność pośrednia przez `app-eye-desktop`, `app-xr`; brak dowodu integracji.
- `lib-signals` (historyczna nazwa; wymaga uzgodnienia z `lib-sig`): planowana zależność pośrednia przez `app-eeg-neurolyze`; brak dowodu integracji.
- `lib-sim`: planowana zależność pośrednia przez `app-eeg-neurolyze`; brak dowodu integracji.
- `lib-unity`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-vlm`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-voice`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `OptiCore`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.

Relacje APP i LIB pochodzą odpowiednio z `app_publication_links.csv` i `component_dependencies.csv`. Są kandydaturami, nie dowodami wykonania prac. Aktualność nazw `lib-signals`, `lib-image` i `lib-llm` wymaga osobnego uzgodnienia z nowymi repozytoriami.

## Proweniencja, metodologia i bramki

- **UID źródłowy:** `arc-xr:PROTO-AR-03`; repozytorium `MatPomGit/arc-xr`, identyfikator `PROTO-AR-03`.
- **Ścieżka źródłowa:** `docs/aparatura_ar_ai.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/arc-xr/blob/main/docs/aparatura_ar_ai.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
