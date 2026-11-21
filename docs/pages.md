# Publiczna witryna ARC-XR

**Źródłem strony jest tylko osobny katalog `pages/`**, nigdy `docs/` ani `manuscripts/`. Minimalny `mkdocs.yml` wskazuje `docs_dir: pages`, `site_dir: site`. Strona zawiera zwięzły, neutralny opis programu przeznaczony dla zewnętrznego odbiorcy.

Zasób, który ma znaleźć się w witrynie, musi być jawnie wymieniony w `config/pages-policy.json`. `scripts/validate_pages.py` odrzuca niezatwierdzone pliki, symlinki, traversal, nieznane opcje MkDocs, instrukcje agentów, notatki redakcyjne, placeholdery, niedopuszczalne linki wewnętrzne i niektóre formaty sekretów. Każde rozszerzenie listy wymaga uzasadnienia i recenzji.

Publiczna strona nie może zawierać poleceń do agentów, sposobów prowadzenia repozytorium, opisów wewnętrznej koordynacji, technicznych notatek dla autora, prywatnych identyfikatorów urządzeń, danych uczestników lub niezaakceptowanych prac. Nie twórz `CONTRIBUTING.md` i nie publikuj dokumentacji o współtworzeniu repo.

**Repozytorium prywatne nie gwarantuje prywatnego Pages.** Przed uruchomieniem witryny skontroluj uprawnienia, domenę, rzeczywistą widoczność, pliki wynikowe HTML, metadane mediów i licencje. W GitHub Pages nie wybieraj `Deploy from a branch` wskazującego `main:/docs` ani root repo. Przegląd statyczny nie wystarcza do uznania publikacji za bezpieczną.

Publikację obsługuje odrębny workflow `.github/workflows/pages-publish.yml`, dostępny wyłącznie w trybie ręcznym (`workflow_dispatch`) na gałęzi `main` i wymagający jawnej autoryzacji `publication_authorized=true`. Weryfikowany jest SHA, zatwierdzony zakres `pages/` oraz wynikowy HTML w `site/`. Nie ma automatycznej publikacji po scaleniu PR. Do wykonania wdrożenia wymagane są właściwe ustawienia źródła GitHub Pages (`GitHub Actions`) i przegląd właścicielski publikowanych treści.


## Logo programu i poszczególnych projektów

Nagłówek witryny ARC XR może prezentować lokalne logo `pages/assets/brand/logo.png` (lub WebP/JPEG). Wykorzystuje do tego opcję MkDocs `theme.logo`. Jeżeli zatwierdzonego pliku nie ma, nagłówek jest tekstowy.

Każdy odrębny projekt naukowy może prezentować własne logo w swojej publicznej karcie. Zalecana lokalna ścieżka kopii zatwierdzonej do umieszczenia w katalogu ARC to `pages/assets/projects/<project_id>.png` (lub WebP/JPEG). Logo projektu nie zastępuje głównego znaku ARC. Projekty nieobecne w publicznym katalogu nie otrzymują kart ani grafik na stronie programu.

Każda opublikowana grafika musi zostać wpisana do `config/pages-policy.json:public_files` i `approved_image_sha256` ze sprawdzonym SHA-256. `python scripts/site_branding.py --apply` aktualizuje nagłówek na podstawie zatwierdzonego pliku programu; CI wymaga później zgodności. Repozytorium nie pobiera automatycznie grafik z innych projektów. Instrukcje edytorskie należą do dokumentacji technicznej, nie do README przeznaczonego dla odbiorcy naukowego.
