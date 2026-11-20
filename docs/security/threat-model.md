# Model zagrożeń ARC-XR

**Stan: NOT_ASSESSED.** Poniższa mapa jest listą ryzyk do sprawdzenia, nie raportem potwierdzonego zabezpieczenia. Przed eksperymentem oceniaj prawdopodobieństwo, skutek, właściciela ryzyka, kontrolę i jej dowód.

| Granica | Zagrożenie | Wymagany dowód |
| --- | --- | --- |
| Wideo, EEG, gaze, głos | Reidentyfikacja i nieuprawniony dostęp | Zgoda, minimalizacja, retencja, kontrola dostępu i test eksportu |
| Gogle HMD i Unity | Dyskomfort, błędy okluzji i latencja | Pomiar opóźnienia, kryteria przerwania, ocena etyczna |
| Tobii Eye Tracker 5 | Błędne utożsamienie eksperymentu ekranowego z HMD | Zgodność geometrii, konfiguracji i urządzenia ze scenariuszem |
| VLM/agent | Halucynacje, prompt injection w obrazie, niebezpieczne instrukcje | Separacja danych od poleceń, abstencja, potwierdzenie operatora |
| Repo, PR, CI | Wykradzenie sekretów i wykonanie kodu na stałym runnerze | Izolacja, minimalne uprawnienia, brak sekretów w PR |
| GitHub Pages | Przypadkowa publikacja protokołów, instrukcji agentów i historii | `pages/`, allowlista, przegląd źródeł i wynikowego HTML |
| Dane naukowe | Przeciek grup, błędna jednostka analizy, selekcja metryk | Zamrożony plan, audyt podziałów, pełny SHA i negatywne wyniki |

Dla każdego scenariusza podaj konkretny komponent, wersję SDK, warunek błędu, test negatywny i ryzyko po kontroli. Brak weryfikacji oznacz `NOT_RUN` lub `UNAVAILABLE`, nie `PASS`. Nie publikuj prywatnych identyfikatorów urządzeń ani danych uczestników w repo.

Powiązane: [SECURITY.md](../../SECURITY.md), [granice aparatury](../architecture/measurement-boundaries.md), [ADR](../adr/0002-research-and-device-safety.md), [incydenty](incident-response.md).
