"""Zadanie 4. Zaproponuj rekurencyjny algorytm zamiany liczby dziesiętnej na binarną. Należy
zaprojektować schemat blokowy oraz implementacje."""


def bin(n):
    
    if n >1:
        bin(n//2)
    print(n %2, end ="")



n = 34

bin(n)