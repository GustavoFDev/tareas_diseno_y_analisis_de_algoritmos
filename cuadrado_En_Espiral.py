def generar_espiral(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(0)
        matriz.append(fila)

    contador = 1
    for capa in range((n+1)//2):
        for ptr in range(capa, n-capa):
            matriz[capa][ptr] = contador
            contador += 1
            
        for ptr in range(capa+1, n-capa):
            matriz[ptr][n-capa-1] = contador
            contador += 1
            
        for ptr in range(capa+1, n-capa):
            matriz[n-capa-1][n-ptr-1] = contador
            contador += 1
        for ptr in range(capa+1, n-capa-1):
            matriz[n-ptr-1][capa] = contador
            contador += 1
    return matriz


def imprimir_espiral(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=', ')
        print("\n")

        


n = int(input("¿De cuanto quieres el cuadrado? "))

espiral = generar_espiral(n)

print("El cuadrado en espiral es el siguiente: ")
imprimir_espiral(espiral)
