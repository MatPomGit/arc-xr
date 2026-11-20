# Granice aparatury i ważności pomiarów

**Stan: plan**, nie raport wykonanej kalibracji.

- **Standardowy Meta Quest 3** nie ma wbudowanego eye trackingu. Nie opieraj HMD-pilotaży P01, P03 i P06 na rzekomych pomiarach wzroku z tego urządzenia.
- **Tobii Eye Tracker 5** służy do śledzenia wzroku przy monitorze. Dane z eksperymentu ekranowego i gogli nie są tą samą modalnością ani bezpośrednią integracją.
- W P04 i P05 można proponować zewnętrzną kalibrację obiektów lub ich znane współrzędne; bez testu SDK nie wolno zakładać dostępu do surowej głębi ani dokładnych anchorów urządzenia.
- P03 wymaga zmierzonej, nie deklarowanej latencji renderowania, limitu ekspozycji i kryteriów przerwania. Samo ustawienie opóźnienia w kodzie nie potwierdza opóźnienia doświadczanego.
- W P02 etykiety stanu afektywnego i frustracji wymagają niezależnego źródła i rozdzielenia sesji przy treningu oraz ocenie.

Przed zadaniem pomiarowym zapisuj: potwierdzony model urządzenia, system i wersję SDK, rozdzielczość/częstotliwość, test połączenia, geometrię, wersję kalibracji, znacznik czasu, utratę próbek i warunki pomiaru. Ujemny wynik testu możliwości blokuje wykorzystanie tej funkcji w protokole.

Szczegółowe notatki robocze: [aparatura](../aparatura_ar_ai.md) i [plan minimalny](../../manuscripts/mvp_plan.md). Nie przenoś prywatnych identyfikatorów urządzeń do publicznego `pages/`.
