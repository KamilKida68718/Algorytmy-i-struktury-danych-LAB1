"""Zadanie 1. Zaproponuj rekurencyjny algorytm obliczania silni dla liczby całkowitej dodatniej n."""


def silnia(n):
    if n > 1:
        return n* silnia(n-1)
    else:
        return 1





n = int(input("Podaj liczbe silni: "))

while n < 0:
    print("Silia nie może być mniejsz od zera.")
    n = int(input("Podaj liczbe dla silni: ")) 

wynik = silnia(n)

print("Silnia jest rowna: ",wynik)