"""Zad5. Zaprojektuj algorytm wyszukiwania w tablicy dwuwymiarowej minimalnej wartości w każdym
wierszu. Po znalezieniu minimalnej wartości wstaw ją na początek danego wiersza (poprzez
zamianę miejsc). """


listDwu = [[2,3,-4,5],[100,29,4,0]]

print("Lista dwuwymiarowa: ",listDwu)

for i in listDwu:

    naj = i[0]

    for j in i:
        if j < naj:
            naj = j
            index = i.index(naj)
    
    i[index] = i[0]
    i[0] = naj
   
print("Lista dwuwymiarowa po zamianie miejsc: ",listDwu)