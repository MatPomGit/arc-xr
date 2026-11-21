# ARC-XR: kontrakt pracy agentów

Zakres obejmuje wszystkie pliki repozytorium. Obowiązują przepisy, uprawnienia, bieżąca dyspozycja właściciela oraz ochrona danych. Stosuj aktualne zasady [Research Autopilot](https://github.com/MatPomGit/research-autopilot/blob/main/AGENTS.md) i jego [procedurę Issues/PR](https://github.com/MatPomGit/research-autopilot/blob/main/docs/governance/AGENT_WORKFLOW_RULES.md), jeśli nie są sprzeczne z regułami ARC-XR. Dokument nie nadaje nowych uprawnień do infrastruktury, kosztów ani publikacji.

## Przed rozpoczęciem zadania

1. Przeczytaj `README.md`, `RESEARCH.md`, `PROJECT_STATE.yaml`, `AUTOPILOT_PLAN.md` oraz odpowiedni `manuscripts/MSC-AR-PNN/protocol/README.md`.
2. Sprawdź aktualny stan `main`, Issues, otwarte PR, gałęzie zadaniowe oraz potencjalne konflikty prac. Wykorzystaj istniejący Issue/PR, zamiast powielać zadania.
3. Ustal kryteria odbioru, ryzyko (R0 do R3), dokładny SHA bazowy, dozwolone skutki uboczne oraz możliwe testy. Zachowaj limity: najwyżej 4 otwarte PR i 4 aktywne gałęzie zadaniowe w repozytorium; sprawdź również limit portfelowy 5 otwartych PR.
4. Stosuj najmniejszą możliwą zmianę. Nie buduj osobnych kolejek, schedulerów, routerów modeli, rejestrów dowodów ani mechanizmów scalania. Research Autopilot pozostaje jedynym kontrolerem działań autonomicznych.

## Rzetelność i bezpieczeństwo

- Pracuj w trybie zero-spend. Nie uruchamiaj odpłatnych API, płatnych runnerów ani zewnętrznych usług bez osobnej autoryzacji.
- Nie uruchamiaj niezweryfikowanego kodu PR na trwałym HomeServerze lub Andromedzie. Nie zakładaj, że dostęp do runnera oznacza zgodę na jego wykorzystanie.
- Nie publikuj danych uczestników, nagrań biometrycznych, sekretów, identyfikatorów ani nieuprawnionych obrazów. Stosuj `REPRODUCIBILITY.md`.
- Zawsze odróżniaj: hipotezy, protokół, symulację, rzeczywisty pomiar, zweryfikowane wyniki, przegląd, scalenie i wdrożenie. Brak dowodu nie jest wynikiem pozytywnym.
- Badania z udziałem osób, przechwytywanie sygnałów i interwencje AR wymagają właściwej oceny etycznej i zgód. Nie prowadź niebezpiecznych interwencji ani nie przedstawiaj modeli afektywnych jako diagnostyki klinicznej.
- Rejestruj wersje danych, identyfikatory sesji, podziały na grupy, metryki, niepewność, konfiguracje i pełny SHA kodu. Nie fabrykuj danych, cytowań ani osiągnięć.
- Przed napisaniem wniosków przeglądaj źródła pierwotne i ograniczenia; w `PROJECT_STATE.yaml` aktualizuj tylko potwierdzony stan.

## PR, recenzja i scalanie

- Issues definiują zadania, PR gromadzą zmiany i dowody. Nie tworzyć raportowego PR po każdym teście.
- Weryfikacje oznaczać `PASS`, `FAIL`, `SKIPPED`, `UNAVAILABLE`, `NOT_APPLICABLE` albo `NOT_RUN`; odnosić je do dokładnego SHA. Przegląd tekstu i struktury nie zastępuje testów kodu ani dowodu empirycznego.
- Autor zmiany nie może samodzielnie poświadczyć niezależnej recenzji technicznej. Wymagane są bieżące dowody, werdykt i pochodzenie recenzji. Dla R2/R3 wymagane jest osobne upoważnienie do scalania przez agenta.
- Przed scaleniem sprawdź stan PR, aktualny HEAD, wymaganą recenzję, dostępne kontrole i ochronę gałęzi. Nie używaj force-push ani nie usuwaj cudzych gałęzi.
- Nie utożsamiaj `merged` z wdrożeniem, publikacją naukową lub wynikiem eksperymentu.

## Redakcja i autorstwo

Pisz poprawną polszczyzną, pełnymi zdaniami i zwięźle. Zachowuj anglojęzyczne nazwy techniczne, gdy są standardem danej dyscypliny. Wysyłka do redakcji, kontakt z wydawcą, opłaty i publikowanie danych wymagają wyraźnej zgody autora. Przestrzegaj [RESEARCH.md](RESEARCH.md).

## Uzupełnienie: definicje ryzyka i gotowości

**DoR:** cel i kryteria odbioru, właściciel, dokładny base SHA, powiązany Issue/PR, wpływ na badania i użytkownika, klasa R0–R3, uprawnienia, testy i rollback. **DoD:** zweryfikowane kryteria na exact HEAD SHA, zmieniona dokumentacja, niezależny review, poprawne bramki i potwierdzenie uprawnionego merge. Publikacja i pomiary to odrębne etapy.

| Klasa | Zakres i minimalny dowód |
| --- | --- |
| **R0** | Korekta redakcyjna bez zmiany znaczenia: aktualny diff, linki i SHA |
| **R1** | Drobna zmiana bez wpływu na API, CI, bezpieczeństwo i protokół: adekwatny test |
| **R2** | Polityka agentów, CI, struktura, kontrakty, kod: testy exact SHA, niezależny review |
| **R3** | Dane uczestników, udostępnianie, publikacja, uprawnienia, zmiana protokołu badania: odrębna zgoda i kontrola wycofania |

Stosuj szczegółową [procedurę](.github/AGENT_WORKFLOW.md). `COMMENTED/ACCEPT` nie jest formalnym GitHub `APPROVED`; własna recenzja nie jest niezależna.

**Dostępność materiałów:** `docs/` i `manuscripts/` są dokumentacją projektu, a `pages/` jedynym źródłem publicznej witryny. Żadnych instrukcji dla agentów, treści edytorskich, porad o współtworzeniu repozytorium, prywatnych danych ani surowych pomiarów w Pages. Zobacz [politykę](docs/pages.md). Nie twórz `CONTRIBUTING.md`.


## GitHub Issues: nowy kontrakt

Stosuj [docs/issues.md](docs/issues.md) oraz formularze `.github/ISSUE_TEMPLATE/`. Przed otwarciem Issue sprawdź istniejące Issues i PR. Jeden rezultat = jedno zadanie, a JUMP jest krokiem wewnątrz zadania, nie nową kolejką. Używaj jednego poprawnego tagu typu zadania, np. `[docs]`, `[fix]`, `[paper]`, `[experiment]`, `[test]`, bez tworzenia własnych synonimów.

Agent podczas triage uzupełnia blok `agent-work-classification:v1`. Metadata, formularz, `status:ready-for-agent` i etykiety nie uruchamiają wykonania. Natywne Parent/Sub-issues i Blocked by potwierdzaj przez GitHub; przy samych odnośnikach tekstowych zapisz `NATIVE_RELATIONS_NOT_APPLIED`. Nie dodawaj automatycznych etykiet ani nie osłabiaj bramek `human_approval_required`. Research Autopilot jest jedynym upoważnionym kontrolerem.
