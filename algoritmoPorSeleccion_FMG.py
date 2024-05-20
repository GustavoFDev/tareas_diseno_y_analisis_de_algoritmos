def ordenamiento_seleccion(lista, longitud):
    for i in range(0, longitud):
        min_i = i
        valor_min = lista[min_i]
        
        for j in range(i + 1, longitud):
            if valor_min > lista[j]:
                valor_min = lista[j]
                min_i = j
        
        if min_i != i:
            valor_aux = lista[i]
            lista[i] = lista[min_i]
            lista[min_i] = valor_aux

#FMG 210120167
        
lista = [69, 34, 25, 13, 22, 7, 90, 26, 145, 89, 1]
longitud = len(lista)
ordenamiento_seleccion(lista, longitud)

print("La lista ordenada es:")
for i in range(len(lista)):
    print("%d" % lista[i], end=" ")
