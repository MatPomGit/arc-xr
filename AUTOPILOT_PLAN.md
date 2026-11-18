# ARC-XR: plan prac dla Research Autopilot

**Wersja:** 0.1.0, 2026-11-18. **Status:** plan, nie uruchomiony pipeline ani zadanie kontrolera.

Ten plan opisuje priorytety pracy nad sześcioma badaniami. Nie stanowi autoryzacji nowych automatyzacji, runnerów, kontaktów z uczestnikami, wysyłania publikacji ani wydatków. Przed pracą należy odczytać aktualny stan [PROJECT_STATE.yaml](PROJECT_STATE.yaml), bieżące Issues/PR i [AGENTS.md](AGENTS.md).

## Priorytety i bramki

1. **M0: Uporządkowanie repozytorium.** Utrzymać jeden katalog `manuscripts/`, stabilne identyfikatory P01 do P06, jedno źródło stanu, minimalne reguły agentów i zgodne linki. Kryterium: kompletna struktura bez utraty zawartości oraz przegląd zmiany.
2. **M1: Przegląd literatury.** Dla każdego PXX zebrać zweryfikowane prace pierwotne, różnice metodologiczne i granice nowości. Kryterium: pochodzenie źródeł i brak zmyślonych cytowań.
3. **M2: Protokół i etyka.** Ustalić główny punkt końcowy, estymand, próbkowanie, grupowanie, wielkość efektu, liczebność, plan braków danych, koszt interwencji i zasady bezpieczeństwa. Kryterium: decyzje i wymagane zgody zatwierdzone przez autora, zanim pojawią się badania potwierdzające.
4. **M3: Reprodukowalna implementacja.** Dodać tylko potrzebny kod pomiarowy i walidacyjny, testy na syntetycznych danych oraz wersjonowane manifesty eksperymentów. Kryterium: dokładny SHA, odrębne testy i poprawna kontrola pochodzenia.
5. **M4: Badanie i analiza.** Wykonywać dozwolone eksperymenty, rejestrować niepowodzenia, wyniki negatywne i niepewność; rozdzielać pilot, symulację i badania z uczestnikami. Kryterium: audytowalny raport i niezależna ocena naukowa.
6. **M5: Manuskrypt i decyzja redakcyjna.** Przygotować artykuł, załączniki, ograniczenia i sprawdzoną listę czasopism. Wysłanie wyłącznie po wyraźnej zgodzie autora i sprawdzeniu bramek formalnych.

## Kolejka prac

Najpierw naprawiaj istniejące blokady i otwarte PR. Nie rozpoczynaj nowego PR, gdy limity są wyczerpane. Wspólny kontroler Research Autopilot pozostaje jedynym źródłem zadań cyklicznych, leasingów i dowodów. Nie tworzyć lokalnego autopilota w `arc-xr`.

## Stan realizacji

Dla M0 źródłem aktualnego statusu migracji jest [Issue #2](https://github.com/MatPomGit/arc-xr/issues/2) oraz [PR #3](https://github.com/MatPomGit/arc-xr/pull/3). Przed uznaniem etapu za ukończony należy potwierdzić scalenie do `main`, zgodność struktury z kryteriami i wymagane bramki recenzji. Przygotowanie dokumentacji nie oznacza ukończenia M0.

Bieżący stan badań i bramek naukowych określa [PROJECT_STATE.yaml](PROJECT_STATE.yaml). Etapy M1 do M5 nie są automatycznie uznawane za wykonane przez dodanie planu. Integracja projektu z kontrolerem wymaga odrębnego, zweryfikowanego potwierdzenia.

Zmiana treści protokołu, hipotezy lub kolejności priorytetów wymaga aktualizacji źródła stanu i powiązanego Issue, nie tylko komentarza w PR.
