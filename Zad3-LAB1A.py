"""Zad3. Narysuj schemat blokowy algorytmu, który sprawdza czy podana przez użytkownika wartość
występuje w tablicy jednowymiarowej. """

tablicaJednowymiarowa = [1,2,3,4,5]


x = int(input("Podaj szukaną liczbe: "))

if x in tablicaJednowymiarowa:
        print("Liczba ",x," jest w tablicy jednowymiarowej." )
else:
        print("Liczba nie zawiera się w tablicy jednowymiarowej") 