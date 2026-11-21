# Migracja 27 źródeł ARC-XR do rejestru ARC v2

**Punkt źródłowy:** `main` `87c9603f5a18359ae1d3477122b800c0631eb20a`. Migracja została zintegrowana z `main`. Nie stanowi zgody na publikację GitHub Pages ani dowodu wykonania eksperymentów.

## Migracja źródeł i własności

Przeniesiono kompletne sześć katalogów `manuscripts/P01`–`P06` do `manuscripts/MSC-AR-P01`–`MSC-AR-P06`, zachowując obiekty Git (w tym źródła LaTeX, protokoły i bibliografię). Pozostałe 21 katalogów `MSC-*` nie wymagało zmiany nazw. Każdy z 27 plików `main.tex` jest nadal weryfikowany przez Git blob SHA z [pinned migration map](../../migration/arc-v2-pilot-map.json).

Kanoniczny rejestr znajduje się wyłącznie w [portfolio/papers.json](../../portfolio/papers.json) i zawiera 26 lokalnych artykułów `primary` oraz jeden zewnętrzny artykuł `related`. W publicznym ARC-XR nie przechowuje się adresu prywatnego repozytorium właściciela zewnętrznego. Rekord powiązany nie deklaruje lokalnego kanonicznego TeX. Dane pochodzenia poprzedniego standardu zostały zachowane w [historycznej migawce](../../migration/provenance/source-manifest-v1.json); nie są drugim aktywnym rejestrem.

Stan publikacyjny to 7 szkiców (`draft`) i 20 koncepcji (`concept`). Stan naukowy jest oddzielny i nie wynika automatycznie z posiadania plików TeX. Nie zatwierdzono `public_listing` dla żadnej z nowych pozycji w rejestrze v2. Publiczne karty tematyczne w `pages/` pozostają dotychczasowym, ręcznie recenzowanym materiałem.

## Zachowanie informacji historycznych

`PROJECT_STATE.yaml` nadal przechowuje oryginalny, zagnieżdżony stan sześciu głównych prac. Skróty `P01`–`P06` zachowano wyłącznie jako zgodność operacyjną; identyfikatory kanoniczne zaczynają się od `MSC-AR-`. Nie zastąpiono szczegółowego stanu badawczego płaskim przykładem z szablonu.

Mapowanie 27 pozycji do pięciu obszarów: `adaptation` 11, `affect` 6, `perception` 4, `procedures` 3 i `collaboration` 3.

## Walidacja i integracja

`python3 scripts/audit_arc_v2_pilot.py` sprawdza kompletność, mapowanie, ścieżki i SHA 27 źródeł. `python3 scripts/validate_arc_v2_registry.py` kontroluje schematy JSON, niezmienniki kanonicznej własności, stan naukowy i powiązania z historyczną migawką. Wymaga `python -m pip install -r requirements-research.txt`. CI instaluje zależności w odrębnym wirtualnym środowisku.

Dla zintegrowanej migracji wymagane są zielone testy i kompilacja 27 plików LaTeX na dokładnym SHA oraz kontrola techniczna; niezależne review jest opcjonalne. Przed ponowną zmianą źródeł należy zweryfikować rejestr i uprawnienia. Migracja nie publikuje Pages, nie tworzy wydań ani nie wykonuje badań.
