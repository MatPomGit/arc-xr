# Przepływ danych, dowodów i granice zaufania

**Status: projekt kontraktu przedimplementacyjnego.**

`manuscripts/PXX/protocol/` → zatwierdzenie naukowe i etyczne → wersja aplikacji/SDK oraz sprzętu → kalibracja → akwizycja sesji → QA → zatwierdzony plan analiz → wynik i niepewność → `manuscripts/PXX/results/`.

| Granica | Metadane dopuszczone w publicznym Git | Informacje poza repo |
| --- | --- | --- |
| Protokół | Definicje warunków, miar, kryteriów przerwania i wersji | Formularze z danymi osób badanych |
| Urządzenia | Klasa sprzętu, wersje SDK, rzeczywisty test możliwości | Poufne identyfikatory i konfiguracja dostępu |
| Akwizycja | Schemat pól, jednostki, niezidentyfikowany manifest | Surowe wideo, audio, okulometria, dane uczestników |
| Analiza | Kod, exact-SHA, parametry i model podziału danych | Nieuprawnione kopie zbiorów i identyfikatorów |
| Manuskrypt | Zweryfikowane agregaty po uzyskaniu prawa publikacji | Wrażliwe dane i materiały bez zgody |

Próba musi być przypisana do wersji warunku, monotonicznego znacznika czasu, identyfikatora sesji bez danych osobowych, numeru oprogramowania i konfiguracji. Przy integracji wielu modalności trzeba zmierzyć dryf i opóźnienia, a nie zakładać idealnej synchronizacji.

Modele VLM mogą emitować błędne polecenia lub odczytywać wrogie instrukcje z obrazu. Ich wyniki pozostają danymi; wykonanie działań i ingerencja w bezpieczeństwo wymagają niezależnej kontroli. Szczegóły: [model zagrożeń](../security/threat-model.md), [REPRODUCIBILITY](../../REPRODUCIBILITY.md).
