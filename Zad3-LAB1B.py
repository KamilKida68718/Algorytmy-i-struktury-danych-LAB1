"""ZadNapisz program sortowania liczb naturalnych „leksykograficznie” względem rozwinięć
dziesiętnych. Przykład:
Wejście: 1, 2, 3, 11, 21, 111, 231
Wyjście: 1, 11, 111, 2, 21, 231, 3"""


list =[1,2,3,11,21,111,231]

list.sort(key=str)

print("Posortowana lista: ",list)