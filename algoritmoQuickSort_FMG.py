def particion(lista, bajo, alto):
    i = (bajo - 1)  # Índice del elemento más pequeño
    pivote = lista[alto]  # Pivote

    for j in range(bajo, alto):

        if lista[j] <= pivote:
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
    return (i + 1)

def quickSort(lista, bajo, alto):
    if len(lista) == 1:
        return lista
    if bajo < alto:

        pi = particion(lista, bajo, alto)

 
        quickSort(lista, bajo, pi - 1)
        quickSort(lista, pi + 1, alto)

#FMG 210120167
        
lista = [69, 34, 25, 13, 22, 7, 90, 26, 145, 89, 1]
longitud = len(lista)
quickSort(lista, 0, longitud - 1)

print("La lista ordenada es:")
for i in range(len(lista)):
    print("%d" % lista[i], end=" ")
