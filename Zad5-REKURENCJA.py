"""Zadanie 5. Zapoznaj się z problemem wieży Hanoi, a następnie zaproponuję listę kroków, schemat
blokowy oraz implementację algorytmu.
Prosta zabawka dziecięca — na patyku nanizanych jest pewna liczba krążków tak, że na większym
zawsze leży krążek mniejszy. Zadaniem naszym jest umieszczenie wszystkich krążków na sąsiednim
„patyku” (korzystając z jednego tylko „patyka” pomocniczego) w tej samej kolejności. Podczas każdego
ruchu pamiętać trzeba, że krążek większy nie może znaleźć się nigdy na krążku mniejszym.
"""


def towerOfHanoi (lk, p_kijek, k_kijek, s_kijek ):
    if lk == 1:
        print("Przneieś dysk 1 z kijka ", p_kijek,"na kijek ",k_kijek)
        return
    towerOfHanoi(lk-1, p_kijek, s_kijek, k_kijek)
    print("Przenieś dysk ",lk,"z kijka ",p_kijek,"na kijek", k_kijek)
    towerOfHanoi(lk-1, s_kijek, k_kijek, p_kijek)

lk = int(input("Podaj liczbe klocków: "))

towerOfHanoi(lk,'A', 'C', 'B')