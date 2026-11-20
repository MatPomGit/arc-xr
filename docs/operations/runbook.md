# Runbook ARC-XR

**Stan:** program przed eksperymentami, bez aktywnego pipeline publikacyjnego i bez konfiguracji aparatury zweryfikowanej w tym repo.

## Przygotowanie zmiany

Sprawdź `main` i exact SHA, Issues/PR/draft, `PROJECT_STATE.yaml`, potrzebny protokół oraz klasę ryzyka. Dla dokumentów uruchom:

```bash
python scripts/validate_repository.py
python scripts/validate_documentation.py
python scripts/validate_pages.py
python -m unittest discover -s tests -v
```

Ten zestaw kontroluje strukturę i dokumentację, **nie** jakość pomiaru, poprawność etyczną, urządzenia ani kompilację manuskryptów. Dla nowych implementacji odrębnie uruchom testy platformy Unity/Python i rzeczywistej aparatury po uzyskaniu uprawnienia.

## Badania i reprodukcja

Przed każdym eksperymentem odczytaj właściwy protokół, status zgód, wersję kodu, konfigurację, kalibrację i warunki przerwania. Używaj pustych/syntetycznych danych do testów inżynierskich. Dane uczestników i poufne ścieżki przechowuj poza repo publicznym. Raportuj rzeczywiste liczby prób, brakujące pomiary, niepewność i wykluczenia wraz z wersją analizy.

## Publikacje i witryna

Publikacja manuskryptu wymaga decyzji autora. Strona GitHub Pages korzysta wyłącznie z `pages/`, jawnej allowlisty i osobnej recenzji. Nie ustawiaj publikacji `docs/` z gałęzi głównej ani automatycznego deploymentu po merge. Weryfikacja źródeł i linków nie jest dowodem poprawnego renderu lub poufności.

## Powrót po przerwaniu

W istniejącym Issue/PR zapisz finalny SHA, wykonane testy i ich status, aktualne blokady i minimalną kolejną czynność. Nie twórz niezależnego schedulera ani nie zatrzymuj cudzych obliczeń.

Zasady: [AGENTS.md](../../AGENTS.md), [REPRODUCIBILITY.md](../../REPRODUCIBILITY.md), [Pages](../pages.md).
