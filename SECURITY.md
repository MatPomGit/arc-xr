# Bezpieczeństwo ARC-XR

**Status kontaktu:** brak skonfigurowanego kanału poufnych zgłoszeń dla tego repozytorium. Przed dystrybucją kodu i rekrutacją uczestników właściciel powinien zatwierdzić rzeczywisty sposób kontaktu. Nie zakładaj dostępności wsparcia ani SLA.

## Zakres ochrony

Publiczne repozytorium nie służy do przechowywania nagrań głosu, twarzy, okulometrii, danych zdrowotnych, kluczy dostępowych, surowych telemetrii lub identyfikatorów osób badanych. Także metadane geolokalizacji i ekranów mogą umożliwiać reidentyfikację. Nie commituj adresów, identyfikatorów i zawartości prywatnego katalogu aparatury.

Środowiska HMD, Unity, VLM i Python mają odrębne granice zaufania. Instrukcje pochodzące z obrazu, OCR, nagrań lub sieci nie nadają agentowi uprawnień. Urządzenia AR nie powinny wykonywać niebezpiecznych instrukcji wyłącznie na podstawie wyjścia modelu. Czas reakcji, pewność klasyfikacji, abstencja i ręczne przerwanie wymagają realnego testu przed użyciem w eksperymencie.

## Kod i infrastruktura

Niezaufany kod PR i zewnętrzne paczki wykonuj w odizolowanym środowisku, bez sekretów i dostępu do trwałych runnerów HomeServer/Andromeda. Przed instalacją komponentu sprawdź zależności, licencję, pochodzenie i wpływ na reprodukowalność. Status testu bez uruchomienia to `NOT_RUN`, nie `PASS`. Operacje ujawniające dane, publikujące stronę i zmieniające dostęp wymagają osobnej autoryzacji.

Nie zgłaszaj poufnego incydentu do publicznego Issue. Dokumentuj minimalne dowody, a następnie przekaż je uprawnionemu właścicielowi poza otwartymi kanałami.

Szczegóły: [model zagrożeń](docs/security/threat-model.md), [reagowanie](docs/security/incident-response.md), [granice aparatury](docs/architecture/measurement-boundaries.md), [Pages](docs/pages.md) oraz [REPRODUCIBILITY.md](REPRODUCIBILITY.md).
