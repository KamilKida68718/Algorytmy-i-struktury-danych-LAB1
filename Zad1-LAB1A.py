"""Zad1.arysuj schemat blokowy algorytmu wyznaczającego pierwiastki równania kwadratowego. 
"""

from math import sqrt

a = int(input("Podaj pierwszą liczbe: "))
b = int(input("Podaj drugą liczbe: "))
c = int(input("Podaj trzecią liczbe: "))

while a ==0:
    print("Pierwsza liczba nie może być zerem, spróbuj ponownie")
    a = int(input("ierwsza lkiczba:" ))

d = (b**2) - (4*a*c)

if d < 0:
    print("Brak miejsc zerowych")

elif d == 0:
    x = -b/2*a
    
    print("Równanie kwadratowe ma 1 miejsce zerowe:")
    print(x)

elif d > 0:
    x1 = (-b - sqrt(d))/2*a
    x2 = (-b + sqrt(d))/2*a

    print("Równanie kwadratowe ma 2 miejsca zerowe:")
    print(x1)
    print(x2)