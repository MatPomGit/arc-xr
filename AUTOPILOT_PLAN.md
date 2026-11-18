# ARC-XR: plan prac dla Research Autopilot

**Wersja:** 0.1.0, 2026-11-18. **Status:** plan, nie uruchomiony pipeline ani zadanie kontrolera.

Ten plan opisuje priorytety pracy nad sześcioma badaniami. Nie stanowi autoryzacji nowych automatyzacji, runnerów, kontaktów z uczestnikami, wysyłania publikacji ani wydatków. Przed pracą należy odczytać aktualny stan [PROJECT_STATE.yaml](PROJECT_STATE.yaml), bieżące Issues/PR i [AGENTS.md](AGENTS.md).

## Priorytety i bramki

1. **M0: Uporządkowanie repozytorium.** Utrzymać jeden katalog `manuscripts/`, stabilne identyfikatory P01–P06, jedno źródło stanu, minimalne reguły agentów i zgodne linki. Kryterium: kompletna struktura bez utraty zawartości oraz przegląd zmiany.
2. **M1: Przegląd literatury.** Dla każdego PXX zebrać zweryfikowane prace pierwotne, różnice metodologiczne i granice nowości. Kryterium: pochodzenie źródeł i brak zmyślonych cytowań.
3. **M2: Protokół i etyka.** Ustalić główny punkt końcowy, estymand, próbkowanie, grupowanie, wielkość efektu, liczebność, plan braków danych, koszt interwencji i zasady bezpieczeństwa. Kryterium: decyzje i wymagane zgody zatwierdzone przez autora, zanim pojawią się badania potwierdzające.
4. **M3: Reprodukowalna implementacja.** Dodać tylko potrzebny kod pomiarowy i walidacyjny, testy na syntetycznych danych oraz wersjonowane manifesty eksperymentów. Kryterium: dokładny SHA, odrębne testy i poprawna kontrola pochodzenia.
5. **M4: Badanie i analiza.** Wykonywać dozwolone eksperymenty, rejestrować niepowodzenia, wyniki negatywne i niepewność; rozdzielać pilot, symulację i badania z uczestnikami. Kryterium: audytowalny raport i niezależna ocena naukowa.
6. **M5: Manuskrypt i decyzja redakcyjna.** Przygotować artykuł, załączniki, ograniczenia i sprawdzoną listę czasopism. Wysłanie wyłącznie po wyraźnej zgodzie autora i sprawdzeniu bramek formalnych.

## Kolejka prac

Najpierw naprawiaj istniejące blokady i otwarte PR. Nie rozpoczynaj nowego PR, gdy limity są wyczerpane. Wspólny kontroler Research Autopilot pozostaje jedynym źródłem zadań cyklicznych, leasingów i dowodów. Nie tworzyć lokalnego autopilota w `arc-xr`.

## Stan na 2026-11-18

- M0: struktura P01–P06 istnieje; migracja do `manuscripts/` w przygotowaniu do przeglądu.
- M1–M5: NIEZAKOŃCZONE, bez twierdzeń o wynikach empirycznych.
- Integracja z wykonawczym kontrolerem: NIEZWERYFIKOWANA.

Zmiana treści protokołu, hipotezy lub kolejności priorytetów wymaga aktualizacji źródła stanu i powiązanego Issue, nie tylko komentarza w PR.
