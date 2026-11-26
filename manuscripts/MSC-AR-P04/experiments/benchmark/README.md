# MSC-AR-P04 — benchmark techniczny v0.2.0

Scientific owner: Mateusz Pomianek (MatPomGit).
Powiązane zadanie: [Issue #10](https://github.com/MatPomGit/arc-xr/issues/10).
Status: prototyp techniczny, inferencja rzeczywista NOT_RUN.

## Odtworzenie

Python 3.13, Pillow 12.3.0. Z katalogu benchmark:

    python -m pip install -r requirements.txt
    python -m unittest discover -v
    python scenes.py generated --seed 42 --n 30
    ollama list
    python run_vlm.py run generated pilot.jsonl --model qwen3-vl:8b --split development --limit 2
    python run_vlm.py score generated pilot.jsonl

Wybierz dokładną nazwę już zainstalowanego modelu multimodalnego. Adapter nie pobiera modeli. Wymaga działającego lokalnego Ollama. Katalog generated oraz plik logu muszą nie istnieć przed odpowiednimi operacjami. Generator odtwarza 30 scen, 60 instrukcji, PNG RGB, geometrię JSON, manifest SHA-256 i oddzielny ground_truth.json; 10 scen development i 20 test. Artefakty generowane i logi są lokalne, nie są śledzone w Git.

## Projekt i ograniczenia

Ten sam VLM porównywany w warunkach RGB i RGB+geometry. Estymator: średnia po scenach z parowanych różnic trafności, przedział bootstrapowy przez resampling scen. Abstencja liczona jako niepoprawne wskazanie; błąd wykonania blokuje estymację. Pilotaż dwóch scen to osiem żądań, nie badanie potwierdzające. Zbiór testowy stosować dopiero po ustaleniu modelu, promptów i reguł oceny. Geometria zawiera wysokość celowo niewidoczną w RGB, więc obecne fixtures sprawdzają mechanizm techniczny, a nie przewagę w rzeczywistym AR. Model digest rejestrowany na początku; nie zmieniać modelu podczas wykonania. Seed i temperatura nie gwarantują deterministyczności GPU.

## Dowody wcześniejsze

Windows Python 3.13: użytkownik przekazał wynik 4/4 testów generatora i 7/7 testów ewaluatora. Wcześniejszy lokalny test adaptera z mockiem 4/4 PASS. Nie są to dowody CI dla aktualnego SHA. Nie wykonano inferencji na rzeczywistym modelu. Następny etap: izolowana walidacja źródeł repozytorium i pilotaż development, następnie realistyczne sceny perspektywiczne z okluzją i bez przecieku danych. Protokół naukowy pozostaje niezatwierdzony.
