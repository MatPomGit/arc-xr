# Komponenty i zależności badań XR

**Status: planowana architektura.** To opis odpowiedzialności, nie deklaracja działającego kodu ani istniejących zależności Git.

| Element | P01–P06 | Granica odpowiedzialności |
| --- | --- | --- |
| Program ARC-XR | Wszystkie | Hipotezy, protokoły, stan i odniesienia do dowodów |
| Sceny Unity/AR | P01, P03, P06 | Interfejs, kontrolowane warunki, rejestr prób i latencji |
| Analizy Python/VLM | P04, P05 | Klasyfikacja referentów i temporalne kroki procedur |
| Eksperyment ekranowy | P02 | Kalibracja predyktora i ocena niezależnych etykiet |
| Warstwa pomiarowa | Odpowiednie prace | Jawny kontrakt czasu, danych, jednostek i wersji sprzętu |
| Wspólne biblioteki | Po uzasadnieniu | Jedna implementacja, wersjonowane API, niezależne testy |

W rzeczywistym wdrożeniu aplikacja powinna być właścicielem UI, sceny i uruchomienia; biblioteka tylko wielokrotnie wykorzystywanego algorytmu/sterownika. Nie tworzyć `app-*` lub `lib-*` przez samo zapisanie planu. Sprzęt i SDK dokumentuje się w autoryzowanych źródłach, bez powielania w publicznej stronie.

Protokół i szkic manuskryptu nadal należą do właściwego `manuscripts/PXX/`, a plan minimalny do [mvp_plan.md](../../manuscripts/mvp_plan.md).
