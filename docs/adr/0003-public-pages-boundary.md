# ADR-0003: oddzielenie publicznej witryny od repozytorium

**Data:** 2026-11-20  
**Status:** proposed

## Kontekst

ARC-XR zawiera AGENTS, plany, protokoły, notatki techniczne, historyczne szkice oraz dokumenty mogące zawierać informacje nieprzeznaczone dla odbiorcy zewnętrznego. Domyślny eksport `docs/` ujawniłby te treści wraz z przyszłymi materiałami.

## Propozycja

Publiczne GitHub Pages może powstawać wyłącznie z `site/`, po jawnej akceptacji każdego zasobu w `config/pages-policy.json`, walidacji strukturalnej i osobnej decyzji właściciela. `docs/`, `manuscripts/`, `.github/` i inne pliki robocze nie stają się częścią strony. Nie dodawać workflow automatycznego publikowania na merge.

## Alternatywy i konsekwencje

Eksport całego repo uprościłby budowę strony, ale naruszałby granice danych i ujawniał instrukcje agentowe. Osobny katalog wymaga świadomego przygotowania publicznych opisów i przeglądu renderowanego HTML.
