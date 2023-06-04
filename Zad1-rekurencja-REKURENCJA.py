"""Zadanie 1. Zapoznaj się z poniższym algorytmem NWD, a następnie zaproponuj schemat blokowy
algorytmu oraz jego implementację (rozwiązanie należy zaproponować w formie iteracyjnej
i rekurencyjnej).
Algorytm Euklidesa służy do wyznaczania największego wspólnego dzielnika dwóch liczb całkowitych.
Największy wspólny dzielnik dwóch liczb a i b, to taka liczba, która dzieli te liczby bez reszty i jest ona
możliwie największa. Można go zastosować do skracania ułamków lub wyznaczenia najmniejszej
wspólnej wielokrotności NWW.
Wersja I – nieoptymalna postać algorytmu, polega na wybraniu większej z dwóch liczb i zamianie na
różnicę większej i mniejszej. Czynność powtarzamy do momentu uzyskania dwóch takich samych
wartości.
1. Podaj a, b
2. Jeżeli a=b to idź do K5
3. Jeżeli a>b, 𝑎 ← 𝑎 − 𝑏
4. else b ← b − a
5. Wypisz a
6. Koniec
Wykonaj analizę dla danych wejściowych NWD(12,18), NWD(28,24).
Wersja II - zoptymalizowany algorytm Euklidesa dla dwóch liczb naturalnych a i b. W każdym przejściu
pętli wykonujemy dwie operacje: 𝑎 = 𝑏 oraz 𝑏 = 𝑎 𝑚𝑜𝑑 𝑏. Czynności te powtarzamy do momentu,
gdy zmienna 𝑏 osiągnie wartość zero. Zmienna 𝑎 będzie przechowywać wtedy największy wspólny
dzielnik liczb podanych na wejściu.
Zaproponuj algorytm dla wersji iteracyjnej oraz rekurencyjnej."""


def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    else:
        return a
    
a = int(input("Podaj pierwszą liczbe: "))
b = int(input("Podaj drugą liczbe: "))



print("Największy dzielnik to ",nwd(a,b))