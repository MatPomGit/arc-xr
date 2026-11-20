# ADR-0002: bezpieczeństwo badań i granice aparatury

**Data:** 2026-11-20  
**Status:** proposed

## Kontekst

XR łączy HMD, okulometrię ekranową, modele VLM i interwencje. Błędne założenia o możliwościach urządzeń lub wyjściu modelu mogą prowadzić do nierzetelnych pomiarów lub zagrożeń fizycznych.

## Propozycja

Każda modalność wymaga potwierdzenia sprzętem i wersją SDK. Nie traktować Quest 3 jako urządzenia ze śledzeniem wzroku; Tobii Eye Tracker 5 stanowi osobny układ ekranowy. Pomiary afektywne nie zastępują niezależnego wyniku psychometrycznego. VLM i agent nie mogą działać bez niezależnych bramek bezpieczeństwa, kontroli niepewności i możliwości przerwania.

## Alternatywy i konsekwencje

Bogatsze założenia aparaturowe byłyby tańsze opisowo, ale niemożliwe do obrony empirycznej. Ograniczenia redukują funkcje pilotażu i wymagają jawnego rozdzielenia badań ekranowych od HMD. Implementacja zależy od rzeczywistych testów i oceny etycznej.
