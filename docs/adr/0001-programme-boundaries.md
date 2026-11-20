# ADR-0001: odrębność programu, aplikacji i bibliotek

**Data:** 2026-11-20  
**Status:** proposed

## Kontekst

Sześć planowanych manuskryptów ARC-XR korzysta z podobnych funkcji AR, modeli i aparatury. Kopiowanie kodu do każdego artykułu utrudniłoby reprodukcję, ale tworzenie sześciu aplikacji i bibliotek bez potrzeby zwiększyłoby złożoność.

## Propozycja

Program ARC-XR zachowuje dokumenty naukowe, a po ich faktycznym utworzeniu aplikacje i biblioteki są niezależnymi właścicielami kodu. Wariant minimalny to jedno środowisko Unity/AR (P01/P03/P06), jedno Python/VLM (P04/P05) i osobny eksperyment ekranowy P02. Powiązania mają wskazywać konkretny wersjonowany artefakt, nie niezdefiniowaną nazwę repozytorium.

## Alternatywy i konsekwencje

Monolit skróci początek, lecz miesza logikę badań; sześć wdrożeń naraz zwiększy koszty. Dwie wspólne platformy wymagają kontroli niezależności wyników i wersjonowania. Przed akceptacją ADR potwierdzić rzeczywistą potrzebę kodu oraz mapę zależności.
