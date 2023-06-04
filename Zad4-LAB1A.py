"""Zad4. Zaprojektuj algorytm wyszukiwania w tablicy jednowymiarowej minimalnej wartości. """

tabJedno = [-2, -10, 0, 4,55, -121]

najLiczba = tabJedno[0]

for i in tabJedno:
    if i < najLiczba:
        najLiczba = i

print("Najmniejsza liczba w tablicy jednowymiarowej to: ", najLiczba)