# Publiczna witryna ARC-XR

**Źródłem strony jest tylko osobny katalog `pages/`**, nigdy `docs/` ani `manuscripts/`. Minimalny `mkdocs.yml` wskazuje `docs_dir: pages`, `site_dir: site`. Strona zawiera zwięzły, neutralny opis programu przeznaczony dla zewnętrznego odbiorcy.

Zasób, który ma znaleźć się w witrynie, musi być jawnie wymieniony w `config/pages-policy.json`. `scripts/validate_pages.py` odrzuca niezatwierdzone pliki, symlinki, traversal, nieznane opcje MkDocs, instrukcje agentów, notatki redakcyjne, placeholdery, niedopuszczalne linki wewnętrzne i niektóre formaty sekretów. Każde rozszerzenie listy wymaga uzasadnienia i recenzji.

Publiczna strona nie może zawierać poleceń do agentów, sposobów prowadzenia repozytorium, opisów wewnętrznej koordynacji, technicznych notatek dla autora, prywatnych identyfikatorów urządzeń, danych uczestników lub niezaakceptowanych prac. Nie twórz `CONTRIBUTING.md` i nie publikuj dokumentacji o współtworzeniu repo.

**Repozytorium prywatne nie gwarantuje prywatnego Pages.** Przed uruchomieniem witryny skontroluj uprawnienia, domenę, rzeczywistą widoczność, pliki wynikowe HTML, metadane mediów i licencje. W GitHub Pages nie wybieraj `Deploy from a branch` wskazującego `main:/docs` ani root repo. Przegląd statyczny nie wystarcza do uznania publikacji za bezpieczną.

Publikację obsługuje odrębny workflow `.github/workflows/pages-publish.yml`, dostępny wyłącznie w trybie ręcznym (`workflow_dispatch`) na gałęzi `main` i wymagający jawnej autoryzacji `publication_authorized=true`. Weryfikowany jest SHA, zatwierdzony zakres `pages/` oraz wynikowy HTML w `site/`. Nie ma automatycznej publikacji po scaleniu PR. Do wykonania wdrożenia wymagane są właściwe ustawienia źródła GitHub Pages (`GitHub Actions`) i przegląd właścicielski publikowanych treści.
