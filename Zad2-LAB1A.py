"""Zad2. Zaproponuj algorytm wczytywania ciągu n liczb całkowitych (N>0) i wyznaczania ilości liczb
ujemnych w tym ciągu. """

ciąg = [-2,4,-4,-5,3,7]
print("Ciąg liczb:",ciąg)

n = len(ciąg)

if n > 0:
    ile_u = 0
    for j in ciąg:
        if j < 0 :
            ile_u +=1
            

print("Ilość liczb ujemnych: ",ile_u)
