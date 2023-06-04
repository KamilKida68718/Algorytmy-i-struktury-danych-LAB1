"""Napisz funkcję rekurencyjną, która odwraca elementy tablicy. """


def odwracanie(list, l ,r):
    if  l>=r:
        return list
    
    else:
        tem = list[l]
        list[l] = list[r]
        list[r] = tem

        return odwracanie(list, l+1, r-1)
    





lista = [1,2,3,4,5]


L = 0
R = len(lista) - 1

print("Moja Lisat: ",lista)

print("Odwrócona lista: ",odwracanie(lista,L,R))


