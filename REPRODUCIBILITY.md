# Standard rzetelności i odtwarzalności ARC-XR

## Stan badań

Wszystkie P01–P06 są na etapie planowania. Projekty metodologiczne nie stanowią zatwierdzonej prerejestracji, zgody bioetycznej, zakończonego pomiaru ani publikacji.

## Wymagany pakiet przed rekrutacją

1. Zamrożona wersja hipotez, definicji zmiennych, punktu końcowego i planu statystycznego, z uzasadnioną liczebnością próby.
2. Właściwa ocena etyczna, świadoma zgoda, zasady wycofania, retencji danych i ewentualnej rejestracji w OSF.
3. Zapis wersji HMD, eye trackera, kamery, aplikacji, modeli, konfiguracji i kalibracji.
4. Schemat identyfikatorów uczestników, sesji, scen i prób oraz rozdzielenie zbiorów treningowego, walidacyjnego i końcowego testowego.
5. Plan obsługi braków danych, odrzuconych prób, efektów kolejności, wielokrotnych porównań i analiz eksploracyjnych.

## Reguły danych i repozytorium

- Nie commitować surowych nagrań głosu, twarzy, okulometrii ani identyfikatorów osób.
- Zanonimizowane/agregowane wyniki udostępniać dopiero po weryfikacji zgody, licencji i ryzyka reidentyfikacji.
- Każde publiczne twierdzenie empiryczne wiązać z dokładną wersją danych, kodem, konfiguracją i śladem analizy.
- Każdą zmienioną po obejrzeniu danych hipotezę lub analizę oznaczać jako eksploracyjną.
- W badaniach adaptacyjnego AR oddzielać jakość modelu predykcyjnego od skutku interwencji; walidować na jednostce odpowiadającej celowi generalizacji.
- W badaniach VLM/agentów zapewnić możliwość abstencji lub potwierdzenia przez użytkownika przy niskiej pewności; nie dopuszczać automatycznych niebezpiecznych działań.

## Minimalne potwierdzenie wyniku

W rejestrze odpowiedniej pracy, `manuscripts/MSC-AR-PNN/results/README.md` (gdzie `PNN` oznacza podstawowe P01 do P06), dokumentować nazwę i definicję wyniku, zbiór i jego pochodzenie, liczbę uczestników/sesji/prób, skrypt i hash wersji, przedziały ufności, wykluczenia, ograniczenia oraz oznaczenie **observed** albo **planned**. Nie generować syntetycznych liczb jako „wyników badań”.
