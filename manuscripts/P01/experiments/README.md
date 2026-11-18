# P01 — eksperymenty i pomiary

**Status:** planowana publikacja; hipotezy i procedury nie są jeszcze prerejestrowane. Nie przeprowadzono tutaj eksperymentów, nie ma wyników empirycznych ani zatwierdzenia komisji etycznej.

## Projekt wykonywalnych etapów

1. Zdefiniować etykiety obciążenia niezależne od sygnałów użytych do predykcji.
2. Zaprojektować manipulację gęstością HUD i mechanizm bezpiecznej zmiany LoD.
3. Zmierzyć opóźnienie całego toru akwizycja–inferencja–renderowanie.
4. Przygotować test międzyosobniczy oraz zrównoważony eksperyment z użytkownikami.

## Proponowana konfiguracja

Kontrolowane badanie z powtarzanymi pomiarami: HUD statyczny, adaptacja jednomodalna, adaptacja multimodalna; kolejność warunków zrównoważona. Oddzielna walidacja algorytmu i ocena wpływu interwencji na zachowanie.

Jednostki rejestrowane: uczestnik/scena, sesja, warunek, próba, znacznik czasu, wersja konfiguracji, status jakości pomiaru. Nazwy narzędzi, wersje urządzeń i konkretne parametry nie zostały jeszcze ustalone.

## Wymagane artefakty każdego uruchomienia

Dokument konfiguracji (w tym seed, jeśli dotyczy), identyfikatory wersji danych/modelu/kodu, manifest podziału na grupy, raport kompletności i synchronizacji, log wykluczeń, skrypt odtworzeniowy oraz rezultaty zagregowane bez danych osobowych.

Nie umieszczać w repozytorium surowych nagrań uczestników. Etapy z ludźmi realizować wyłącznie po zamknięciu wymagań z [protokołu](../protocol/README.md).
