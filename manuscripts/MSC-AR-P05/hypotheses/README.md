# P05 — hipotezy i operacjonalizacja

**Status:** planowana publikacja; hipotezy i procedury nie są jeszcze prerejestrowane. Nie przeprowadzono tutaj eksperymentów, nie ma wyników empirycznych ani zatwierdzenia komisji etycznej.

## H1 (robocza)

Model VLM z temporalnym grafem stanu procedury skuteczniej identyfikuje pominięte kroki niż VLM bez jawnego modelu sekwencji.

## H2 (robocza)

Wizualne wskazówki AR wyzwalane po potwierdzeniu błędu poprawiają odsetek poprawnych korekt względem informacji wyłącznie tekstowej.

## Pytanie główne i pomiar

Czy rozumowanie oparte na temporalnym grafie procedury zmniejsza liczbę pominiętych błędów i fałszywych alarmów względem analizy samego strumienia wideo?

Planowany główny punkt końcowy: Czułość wykrywania pominiętych kroków przy zadanym limicie fałszywych alarmów na procedurę.

Dodatkowe punkty końcowe: Opóźnienie detekcji, F1 błędów, czas korekty, błędy po korekcie, dostępność śladu decyzyjnego.

## Warunki zamrożenia hipotez

Przed zbieraniem danych należy wskazać jednostkę analizy (osoba, sesja, scena lub próba), kierunek kontrastu, efekt minimalnie istotny, regułę odrzucenia hipotezy zerowej i sposób kontroli wielokrotnego testowania. W protokole należy odróżnić hipotezy potwierdzające od analiz eksploracyjnych. Nie utożsamiać korelacji pomiaru fizjologicznego z przyczynowym wpływem interwencji.
