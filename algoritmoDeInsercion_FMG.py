def ordenamiento_insercion(lista, longitud):
    for i in range(1, longitud):
        valor_1 = lista[i]
        valor_2 = i - 1
        
        while valor_2 >= 0 and valor_1 < lista[valor_2]:
            lista[valor_2 + 1] = lista[valor_2]
            valor_2 -= 1
        lista[valor_2 + 1] = valor_1
        
#FMG 210120167


lista = [64, 34, 25, 12, 22, 11, 90, 26, 100, 89, 1]
longitud = len(lista)
ordenamiento_insercion(lista, longitud)

print("La lista ordenada es:")
for i in range(len(lista)):
    print("%d" % lista[i], end=" ")




