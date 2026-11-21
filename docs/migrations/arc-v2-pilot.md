# Pilotaż migracji ARC-XR do standardu ARC v2

Aktualny punkt odniesienia to `main` SHA `87c9603f5a18359ae1d3477122b800c0631eb20a`. Zarejestrowano 27 źródeł `main.tex`, z których 26 reprezentuje kanoniczne lokalne plany naukowe. Jeden dokument jest szkicem pomocniczym do manuskryptu o zewnętrznym właścicielu kanonicznym. Żaden dokument nie jest dowodem publikacji ani wykonania badania.

## Mapa i zakres

Jedyną mapą **tej operacji migracyjnej** jest [arc-v2-pilot-map.json](../../migration/arc-v2-pilot-map.json). Zawiera 27 ID MSC, rzeczywiste ścieżki, proponowane ścieżki docelowe, obszary z publicznego katalogu, role i Git blob SHA źródeł. Nie jest kolejnym rejestrem redagowanym ręcznie ani źródłem prawdy o statusie publikacji. Po migracji kanonicznym rejestrem programu powinien być `portfolio/papers.json`.

Sześć katalogów `P01`–`P06` wymaga zachowania zawartości oraz przeniesienia do `MSC-AR-P01`–`MSC-AR-P06`, wraz z aktualizacją rzeczywistych odnośników, testów i dokumentacji. Dwadzieścia lokalnych katalogów `MSC-*` nie wymaga zmian lokalizacji źródłowego `main.tex`. Dodatkowy szkic przekrojowy pozostaje `external_companion`, bez tworzenia drugiego właściciela.

Przypisano obszary badawcze na podstawie istniejących publicznych kart artykułów: `adaptation` (11), `affect` (6), `perception` (4), `procedures` (3), `collaboration` (3). Wszystkie 27 tytułów odpowiadają nagłówkom publicznych kart, bez nadawania nowych tytułów i bez zmiany zakresów.

## Audyt i następny krok

Uruchom `python3 -B scripts/audit_arc_v2_pilot.py` lub testy repozytorium. Audyt weryfikuje sumy obiektów Git dla wszystkich 27 plików, kompletność mapy, jednoznaczność ID, zgodność katalogów i właścicieli oraz brak prywatnych odnośników w rekordzie pomocniczym. Jest wyłącznie odczytowy i **nie wykonuje migracji**.

Do właściwego wdrożenia wymagane są: dostępna i zintegrowana wersja szablonu ARC v2, zmapowanie istniejących wielopoziomowych ustawień `PROJECT_STATE.yaml`, przeniesienie źródeł ze śledzeniem blob SHA, aktualizacja wszystkich testów i linków oraz dowody CI na dokładnym HEAD. Nie wolno zastąpić istniejącego `PROJECT_STATE.yaml` szablonowym stanem płaskim bez świadomej migracji jego treści. Katalog artykułów Pages powinien nadal korzystać wyłącznie z osobnego `pages/`.

Dane własności prywatnego projektu zewnętrznego nie są dalej powielane w bieżącym publicznym manifeście. Poprzednie commity Git mogą nadal zawierać historyczne odniesienia; ich ewentualne usunięcie wymaga odrębnej decyzji dotyczącej przepisywania historii. Nie wykonuj takiej operacji automatycznie.

Status: **PREFLIGHT_ONLY**. `apply`, Release, Pages deployment, migracja produkcyjna i merge: **NOT_RUN**.
