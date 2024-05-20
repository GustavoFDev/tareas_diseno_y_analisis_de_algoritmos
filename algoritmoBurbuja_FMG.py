def burbuja(lista, longitud):
    for i in range(0, longitud):
        for j in range(0, longitud):

            if lista[j] > lista[j + 1]:
                guardar_Valor = lista[j]
                
                lista[j] = lista[j + 1]
                lista[j + 1] = guardar_Valor


#FMG 210120167

lista = [64, 34, 25, 12, 22, 11, 90, 26, 100, 89, 1]
longitud = len(lista) - 1

burbuja(lista, longitud)

print("La lista ordenada es:")
for i in range(len(lista)):
    print("%d" % lista[i], end=" ")
