# ARC XR — nowe propozycje badań nad adaptacyjnymi wskazówkami przestrzennymi

**Wersja:** 1.1.0 | **Data:** 2026-11-20 | **Status:** propozycja naukowa, nie zamrożony protokół i nie zgłoszony manuskrypt.  
**Program:** ARC XR. **Identyfikator:** `ARC-XR-AR-P25`.

## ARC-XR-AR-P25 — Faza ruchu dłoni a skuteczność instrukcji w AR

**Tytuł roboczy (EN):** *Motor-Phase-Dependent Timing of Augmented Reality Guidance During Manual Tasks*.

**Pytanie:** Czy wskazówka AR wyświetlona tuż przed rozpoczęciem ruchu powoduje mniej błędów sekwencji niż identyczna wskazówka wyświetlona podczas ruchu, gdy liczba i poprawność wskazówek są takie same?

**Hipoteza testowalna:** Porównując `pre-action` i `mid-action`, wcześniejsza wskazówka poprawia poprawność kroku, ponieważ ogranicza koszt przełączenia uwagi podczas wykonywania działania. Kontrast nie może polegać wyłącznie na zróżnicowaniu jakości informacji.

**Wspólne stanowisko:** Wykorzystać jedną prostą scenę Unity/OpenXR, neutralne wirtualne obiekty oraz istniejący rejestr czynności i wersji warunków. Na początku moment rozpoczęcia/kontaktu można określić zdarzeniami kontrolera lub precyzyjnie zdefiniowanym wejściem użytkownika. Ultraleap/Leap Motion to **opcjonalne rozszerzenie**, wymagające kwalifikacji urządzenia, SDK i pomiaru jitteru. Standardowy Quest 3 **nie ma eye trackingu**; nie zakładać wykorzystania Tobii Eye Tracker 5 jako czujnika spojrzenia wewnątrz HMD.

**Najmniejszy eksperyment:** Dwa warunki, ten sam zestaw prostych czynności, to samo miejsce, tekst, liczba i czas ekspozycji wskazówek z wyjątkiem ich położenia względem fazy ruchu. Randomizować kolejność i zestawy zadań, kontrolować uczenie, czas animacji i liczbę przerw. Protokół określa wcześniej, jak rozpoznawać fazę ruchu i jak obsługiwać błędnie wykryty kontakt.

**Wynik główny:** Odsetek błędnych kroków / błędów sekwencji, z jednostką analizy trial i uczestnik. Pomocniczo opóźnienie reakcji, wstrzymanie trajektorii, czas ukończenia i dyskomfort. Nie przypisywać efektywności na podstawie testów syntetycznych; pilotaż 5–8 osób może wykazać wyłącznie wykonalność, nie efekt potwierdzający.

**Granica względem istniejącego portfolio:** [P05](../manuscripts/P05/README.md) sprawdza automatyczną weryfikację kroków procedury, natomiast ten temat dotyczy **momentu podania prawidłowej wskazówki** i wpływu na człowieka. W badaniach kinematyki dłoni poza XR oceniana jest informacja o wymaganiach poznawczych, a tutaj mechanizm czasowego przełączania uwagi. Istnieją badania nad timingiem i wiarygodnością AR; konieczny niezależny przegląd stanu badań, szczególnie ISMAR/CHI, aby nie powielać opisanego już efektu.

**Bramki:** audyt podobieństwa do P05, zamrożony kontrast i outcome, pomiar latencji rzeczywistego renderowania, komfort ekspozycji oraz odpowiednia etyka/zapewnienie zgody na udział. Bez automatycznego pobierania kamer HMD ani zapisu wrażliwych danych.

## Status portfolio

`ARC-XR-AR-P25` ma status **IDEA_HOLD**. To pomysł opcjonalny względem aktualnego minimalnego planu P01–P06. Nie zwiększa liczby zatwierdzonych manuskryptów ani zrealizowanych badań. Wspólna scena i kod pozostają częścią istniejącej architektury; nie tworzyć osobnego systemu bez wykazania potrzeby.