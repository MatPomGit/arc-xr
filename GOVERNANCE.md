# Zarządzanie ARC-XR

ARC-XR utrzymuje program sześciu badań P01–P06. **Właściciel naukowy** odpowiada za hipotezy, metodologię, ocenę etyczną, autorstwo i decyzję o wysłaniu artykułu. **Opiekun kodu** odpowiada za odtwarzalność, testy i kontrakty techniczne, w granicach udzielonych uprawnień. **Niezależny recenzent** weryfikuje odpowiednie twierdzenia i artefakty na finalnym SHA. Agent nie może przyznawać sobie uprawnień właściciela.

## Kanoniczne źródła

`PROJECT_STATE.yaml` określa fazę badawczą, bramki i statusy; `RESEARCH.md` reguły naukowe; `manuscripts/MSC-AR-PNN/` protokoły i manuskrypty; `AUTOPILOT_PLAN.md` plan (nie działający scheduler); `REPRODUCIBILITY.md` dowody. `ARCHITECTURE.md` opisuje granice rozwiązań, a [ADR](docs/adr/README.md) uzasadnienia techniczne. Dokumenty nie powinny powielać równoległego rejestru manuskryptów.

W przyszłym portfelu `MSC-*` obowiązuje jedna kanoniczna własność każdego manuskryptu. Rozważane nowe prace, w tym pozycje z otwartych draft PR, **nie stają się siódmym zatwierdzonym badaniem** bez decyzji naukowej i zmiany `PROJECT_STATE.yaml`.

## Bramki

Klasy R0–R3, DoR/DoD, WIP i sposób współpracy znajdują się w [AGENTS.md](AGENTS.md) i [procedurze](.github/AGENT_WORKFLOW.md). Scalenie PR nie jest zgodą na rekrutację, pomiar, publikację artykułu ani strony Pages. R2/R3 wymagają rzeczywistego przeglądu zgodnego z uprawnieniami i w razie potrzeby osobnej decyzji właściciela. `COMMENTED/ACCEPT` nie zastępuje GitHub `APPROVED`.

Dane, licencje i wizerunek uczestników nie trafiają do publicznego Git. Zobacz [SECURITY.md](SECURITY.md) oraz [zasady Pages](docs/pages.md).
