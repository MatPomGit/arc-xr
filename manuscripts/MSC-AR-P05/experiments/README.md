# P05 — eksperymenty i pomiary

**Status:** planowana publikacja; hipotezy i procedury nie są jeszcze prerejestrowane. Nie przeprowadzono tutaj eksperymentów, nie ma wyników empirycznych ani zatwierdzenia komisji etycznej.

## Projekt wykonywalnych etapów

1. Zdefiniować formalny graf stanów, warunki wstępne i przejścia procedury.
2. Przygotować anonimizowane strumienie egocentryczne z adnotacjami zdarzeń.
3. Wdrożyć poziomy pewności i możliwość potwierdzenia przez operatora.
4. Porównać skuteczność i bezpieczeństwo interwencji AR na odwracalnych zadaniach.

## Proponowana konfiguracja

Zbiór referencyjnych przebiegów prawidłowych i nieprawidłowych procedur z anotacją kroków i czasu; offline benchmark detekcji, następnie kontrolowane badanie interwencji.

Jednostki rejestrowane: uczestnik/scena, sesja, warunek, próba, znacznik czasu, wersja konfiguracji, status jakości pomiaru. Nazwy narzędzi, wersje urządzeń i konkretne parametry nie zostały jeszcze ustalone.

## Wymagane artefakty każdego uruchomienia

Dokument konfiguracji (w tym seed, jeśli dotyczy), identyfikatory wersji danych/modelu/kodu, manifest podziału na grupy, raport kompletności i synchronizacji, log wykluczeń, skrypt odtworzeniowy oraz rezultaty zagregowane bez danych osobowych.

Nie umieszczać w repozytorium surowych nagrań uczestników. Etapy z ludźmi realizować wyłącznie po zamknięciu wymagań z [protokołu](../protocol/README.md).
