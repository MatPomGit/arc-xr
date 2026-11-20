# Standard dokumentacji ARC-XR

Kanoniczne źródła: [AGENTS](../AGENTS.md) (współpraca i ryzyko), [RESEARCH](../RESEARCH.md) (metodologia), [PROJECT_STATE](../PROJECT_STATE.yaml) (stan), [REPRODUCIBILITY](../REPRODUCIBILITY.md) (dowody), [ARCHITECTURE](../ARCHITECTURE.md) (granice komponentów), [ADR](adr/README.md) (decyzje techniczne), [SECURITY](../SECURITY.md) (ochrona danych) i [GOVERNANCE](../GOVERNANCE.md) (kompetencje). Nie duplikuj rejestru prac i dowodów w dokumentach opisowych.

## Limity znaków

`config/documentation-policy.json` ustala limity **znaków Unicode** (ze spacjami i końcami wierszy), nie bajtów. Walidator `python scripts/validate_documentation.py` jest uruchamiany przez CI.

| Dokument | Limit |
| --- | ---: |
| `AGENTS.md`, `README.md`, `ARCHITECTURE.md` | 12 000 |
| `SECURITY.md`, procedura agentów, runbook | 10 000 |
| `GOVERNANCE.md` | 7 000 |
| `CODE_OF_CONDUCT.md`, `SUPPORT.md` | 6 000 |
| Pojedynczy ADR | 6 500 |
| Rozdział architektury lub bezpieczeństwa | 8 500 |
| Publiczna strona | 6 000 |
| Szczegółowe istniejące notatki aparatury | 24 000 |
| Istniejący szkic mobile gaze | 16 000 |

Notatki o aparaturze i pomysłach badawczych mają wyjątki, ponieważ są **materiałem źródłowym**, nie dokumentacją administracyjną. Budżety nie ograniczają `manuscripts/PXX/`, protokołów, bibliografii, danych, kodu i publikacji naukowych. Nie skracaj wyników i uzasadnień naukowych dla spełnienia limitu. Redundancję usuwaj przez jeden dokument kanoniczny i link, a nie zwiększanie limitów.

## Aktualizacja

Przy zmianie interfejsów aplikacji i bibliotek aktualizuj architekturę oraz kontrakt danych; przy zmianie aparatury aktualizuj granice pomiaru i dowody, a przy ryzyku bezpieczeństwa model zagrożeń oraz ADR. Przy zmianie planu badań aktualizuj właściwy protokół i `PROJECT_STATE.yaml`, nie tylko opis. Publiczne opisy mają pozostawać w odrębnym `pages/`.

Skan tekstu i status `PASS` nie dowodzą naukowej skuteczności ani poufności rzeczywiście opublikowanej strony.
