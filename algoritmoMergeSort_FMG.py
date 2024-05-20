def mergeSort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2  # mitad de la lista
        L = lista[:mid]  # Divide la lista en dos mitades
        R = lista[mid:]

        mergeSort(L) #Listas temporales
        mergeSort(R)

        i = j = k = 0

        # Copia los datos a las listas temporales L[] y R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1

        # Verifica si quedan elementos
        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1

#FMG 210120167
        
lista = [69, 34, 25, 13, 22, 7, 90, 26, 145, 89, 1]
mergeSort(lista)

print("La lista ordenada es:")
for i in range(len(lista)):
    print("%d" % lista[i], end=" ")
