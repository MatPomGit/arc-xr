# P04 — eksperymenty i pomiary

**Status:** planowana publikacja; hipotezy i procedury nie są jeszcze prerejestrowane. Nie przeprowadzono tutaj eksperymentów, nie ma wyników empirycznych ani zatwierdzenia komisji etycznej.

## Projekt wykonywalnych etapów

1. Zdefiniować ramy współrzędnych i procedurę kalibracji transformacji.
2. Przygotować zestaw instrukcji i referencyjne anotacje obiektów 3D.
3. Zaimplementować trzy warianty porównawcze bez przecieku scen.
4. Dodać stan abstencji i komunikat o potrzebie doprecyzowania polecenia.

## Proponowana konfiguracja

Benchmark scen z kontrolowaną geometrią i zestawem niejednoznacznych instrukcji; bazowe VLM 2D, VLM + głębia oraz model z mechanizmem abstencji.

Jednostki rejestrowane: uczestnik/scena, sesja, warunek, próba, znacznik czasu, wersja konfiguracji, status jakości pomiaru. Nazwy narzędzi, wersje urządzeń i konkretne parametry nie zostały jeszcze ustalone.

## Wymagane artefakty każdego uruchomienia

Dokument konfiguracji (w tym seed, jeśli dotyczy), identyfikatory wersji danych/modelu/kodu, manifest podziału na grupy, raport kompletności i synchronizacji, log wykluczeń, skrypt odtworzeniowy oraz rezultaty zagregowane bez danych osobowych.

Nie umieszczać w repozytorium surowych nagrań uczestników. Etapy z ludźmi realizować wyłącznie po zamknięciu wymagań z [protokołu](../protocol/README.md).
