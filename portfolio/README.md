# Kanoniczne rejestry programu ARC-XR

`portfolio/papers.json` jest jedynym aktywnym rejestrem 27 artykułów z identyfikatorami MSC. Własność `local` oznacza kanoniczny źródłowy TeX w `manuscripts/<MSC-ID>/main.tex`; własność `external` z `redacted=true` oznacza wyłącznie relację do źródła niedostępnego publicznie. Ten drugi rekord nie deklaruje własności lokalnej ani publicznego odnośnika.

`portfolio/projects.json` służy do ewidencjonowania zewnętrznych projektów o jawnej tożsamości, `portfolio/dependencies.json` do wiązania narzędzi, sprzętu i danych z jednym manuskryptem lub projektem, a `areas/index.json` definiuje obszary badań.

`PROJECT_STATE.yaml` jest istniejącym szczegółowym stanem naukowym sześciu podstawowych prac. Jego zachowane skróty P01–P06 nie stanowią drugiego rejestru manuskryptów. Stary manifest źródeł znajduje się w `migration/provenance/` jako nieredagowana bieżąco migawka historyczna. Nie dodawaj osobnych `manuscript_register.md` ani `publication_register.md`.

Walidacja: `python3 scripts/validate_arc_v2_registry.py`, procedura migracji: [opis techniczny](../docs/migrations/arc-v2-pilot.md). Katalog publiczny `pages/` nie jest automatycznym eksportem pełnych danych rejestru.
