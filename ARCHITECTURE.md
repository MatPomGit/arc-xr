# Architektura programu badawczego ARC-XR

**Status:** projekt architektury, nieudokumentowana jeszcze implementacja. Kanoniczny stan naukowy określa [PROJECT_STATE.yaml](PROJECT_STATE.yaml). Repozytorium jest właścicielem programu P01–P06, protokołów i szkiców manuskryptów, a nie domyślnie sześciu samodzielnych aplikacji.

## Granice i odpowiedzialności

`manuscripts/MSC-AR-P01`–`MSC-AR-P06` przechowują odrębne pytania, hipotezy, plany analiz i rejestry wyników. [RESEARCH.md](RESEARCH.md) reguluje poprawność naukową, a [REPRODUCIBILITY.md](REPRODUCIBILITY.md) zamrożenie dowodów. Przyszłe aplikacje i biblioteki powinny mieć jedno kanoniczne źródło kodu, własną wersję i testy; ARC-XR utrzymuje do nich odnośniki z konkretnym SHA lub wydaniem. Nie kopiuj źródeł do każdego manuskryptu.

Propozycja minimalnego podziału wynikająca z [zaakceptowanego kierunku pilotaży](manuscripts/mvp_plan.md):

| Środowisko | Manuskrypty | Odpowiedzialność i granice |
| --- | --- | --- |
| Unity/AR | P01, P03, P06 | Wspólne środowisko z osobnymi scenami, interwencjami i pomiarami; brak okulometrii w standardowym Quest 3 |
| Python/VLM | P04, P05 | Sceny referencyjne, porównania 2D i 3D, analiza kolejności czynności; brak założenia o dostępnej surowej głębi Quest 3 |
| Eksperyment ekranowy | P02 | Personalizacja predyktora w kolejnych sesjach; pomiary ekranowe z Tobii są odrębne od HMD |

To **proponowane interfejsy**, nie potwierdzone działające aplikacje, istniejące repozytoria `app-*` czy biblioteki `lib-*`. Nie twórz nazw, wersji i adresów projektów bez rzeczywistego wpisu w rejestrze.

## Przepływ dowodów

Protokół i hipotezy → etyka i kryteria włączenia → zamrożona konfiguracja → pomiar → kontrola jakości → analiza → wyniki z niepewnością → manuskrypt. Eksperymentalny kod oraz dane uczestników przechowuje się poza publicznym Git w uprawnionych lokalizacjach; w repo pozostają tylko zgodne z prawem metadane, schematy, skrypty i dowody wolne od informacji identyfikujących.

Każdy wynik wymaga powiązania z `manuscript_id`, identyfikatorem sesji bez danych osobowych, SHA kodu, wersją sprzętu i konfiguracją oraz wersją danych. Nie wolno traktować symulacji, testu technicznego i badania z uczestnikami jako równoważnych.

## Dokumenty szczegółowe

[Komponenty](docs/architecture/components.md), [granice pomiaru](docs/architecture/measurement-boundaries.md), [przepływy i dowody](docs/architecture/data-flow.md), [ADR](docs/adr/README.md), [model zagrożeń](docs/security/threat-model.md), [runbook](docs/operations/runbook.md).

`docs/` jest dokumentacją roboczą. Publiczna witryna ma osobne `site/`, jawne zasoby i **nie publikuje** instrukcji agentowych ani dokumentów programowych z repo. Zobacz [politykę Pages](docs/pages.md).
