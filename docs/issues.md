# Standard GitHub Issues w ARC-XR

**Wersja lokalnego kontraktu:** 1.0.0. **Źródło kanoniczne** to [zarządzanie Issues](https://github.com/MatPomGit/research-autopilot/blob/main/docs/architecture/GITHUB_WORK_MANAGEMENT.md), [klasyfikacja pracy agentów](https://github.com/MatPomGit/research-autopilot/blob/main/docs/autonomy/agent-work-classification.md), [28 typów zadań](https://github.com/MatPomGit/research-autopilot/blob/main/docs/autonomy/TASK_TYPES.md), [taksonomia etykiet](https://github.com/MatPomGit/research-autopilot/blob/main/docs/LABEL_TAXONOMY.md) i [relacje GitHub](https://github.com/MatPomGit/research-autopilot/blob/main/docs/governance/GITHUB_ISSUE_LABELS_AND_RELATIONS.md). Repo nie tworzy kopii tych słowników.

## Zasada jednego sprawdzalnego rezultatu

Nowe zgłoszenie powinno opisywać **jeden wynik** i warunki ukończenia, nie kolejny pomysł bez kryteriów ani jeden Issue na każdy commit. Przed utworzeniem odczytaj aktualne Issues, PR, milestone i powiązania. Kontynuuj istniejące zgłoszenie, jeśli cel i kryteria się pokrywają. `PROJECT_STATE.yaml` jest jedynym stanem programu badawczego P01–P06; Issues nie są alternatywnym rejestrem manuskryptów.

Formularze w `.github/ISSUE_TEMPLATE/` udostępniają: zadanie techniczne/JUMP, błąd (`[fix]`), eksperyment (`[experiment]`) i manuskrypt (`[paper]`). Dla zadania ogólnego dodaj **jeden** prawidłowy tag intencji na początku tytułu, np. `[docs]`, `[test]`, `[develop]`, `[review]`, `[literature]`, `[validate]`, `[simulate]`. Lista 28 wartości jest w centralnym katalogu. Nie twórz pseudotagów `[task]`, `[research]` ani nie używaj ich jako nowych typów.

## DoR, relacje i etapy JUMP

Każde Issue powinno mieć: cel i konkretny artefakt, repozytorium i ścieżki, źródło faktów, aktualny base SHA **sprawdzony przed pracą**, rodzica i zależności, zakres autonomiczny, R0–R3, potrzebne uprawnienia, kryteria odbioru, plan testów exact-SHA, ryzyka i jeden następny bezpieczny krok. Jeśli brak adekwatnej informacji, odnotuj `UNAVAILABLE`, nie twórz pozornego dowodu.

Preferuj **natywne** Parent/Sub-issue oraz Blocked by/Blocking po sprawdzeniu obecnego stanu i faktycznych praw do zapisu. Tekstowe `Parent #N`, `Depends on #N`, `Blocks #N`, `Related #N` i link do PR są jawną alternatywą, ale **nie dowodzą natywnych relacji**. Oznacz to jako `NATIVE_RELATIONS_NOT_APPLIED`. Nie twórz pod-issue tylko dlatego, że plan zawiera etapy `JUMP-01`, `JUMP-02`; etapy pozostają checklistą w aktualnym zadaniu, dopóki nie mają samodzielnego wyniku.

## Kanoniczna klasyfikacja przed wykonaniem

Podczas triage agent dopisuje do **istniejącego Issue**, w pobliżu jego początku, jeden blok o tym samym schemacie co w Autopilocie:

```yaml
<!-- agent-work-classification:v1 -->
work_types: [research, documentation]
execution_mode: mixed
human_approval_required: true
human_approval_reasons: [personal_decision, legal_or_compliance]
resource_requirements: [standard_compute, github]
autonomous_scope: "Przygotowanie opisu, przeglądu źródeł i testów offline."
human_required_scope: "Zatwierdzenie naukowe, etyczne i decyzja o rekrutacji."
<!-- /agent-work-classification -->
```

To **przykład mixed**, nie domyślna klasyfikacja wszystkich zadań. Schemat pozwala na `autonomous`, `autonomous_with_runtime`, `mixed` i `human_required`; wartości pozostałych pól pochodzą z centralnego kontraktu. Agent klasyfikuje faktyczny zakres, a gdy zmienia się zadanie, aktualizuje metadane bez automatycznego osłabiania bramek. Klasyfikacja sama w sobie **nie uruchamia** zadań, nie przyznaje prawa do wydatków, testów na stałych hostach, rekrutacji, publikacji ani merge. Research Autopilot jest jedynym uprawnionym kontrolerem kolejki.

Dla prac XR/AR oddziel przygotowanie protokołu od pomiaru, potwierdzenia aparatury i rekrutacji. Standardowy Meta Quest 3 nie oferuje eye trackingu; Tobii Eye Tracker 5 jest środowiskiem ekranowym, nie czujnikiem gogli. Nie oznaczaj testów fizycznych ani zatwierdzenia przez komisję `PASS`, jeżeli nie przeprowadzono ich rzeczywiście.

## Etykiety i Project

Nadawaj wyłącznie istniejące i zweryfikowane lokalne etykiety: po jednej `type:*` i `priority:*`, najwyżej jednej `status:*`, a `risk:*` i domenowe `xr:*`/`science:*` tylko gdy adekwatne. Nazwy z katalogu centralnego są wzorcem, **nie dowodem, że istnieją w repozytorium**. Nie twórz synonimów i nie wprowadzaj automatycznej synchronizacji bez przeglądu definicji, przypisań i uprawnień. `risk:*` nie zastępuje R0–R3. `status:ready-for-agent` nie jest zgodą na uruchomienie zadania.

GitHub Projects stanowi widok planistyczny tych samych Issues, nie oddzielną kolejkę ani źródło autoryzacji. Nie twórz dla ARC-XR własnego schedulera, automatycznego bota triage, nowych epików kontrolera i dublujących tabel.

## DoD i zamknięcie

W PR/Issue odnotuj base i finalny HEAD SHA, rzeczywiste wyniki testów `PASS/FAIL/NOT_RUN/UNAVAILABLE`, zakres recenzji, wymagane zgody, dokładny wynik merge i ewentualnego wdrożenia. Weryfikacja struktury nie jest dowodem naukowym. Zamknij Issue dopiero, gdy wszystkie jego kryteria są faktycznie spełnione; zielony CI lub scalony PR może pozostawić niezweryfikowane bramki eksperymentalne.

Starsze Issues `#8` i `#10` zachowują własne kryteria i historię. Ich klasyfikacja wymaga odrębnego triage, bez automatycznego podnoszenia statusu naukowego lub kasowania zawartości.
