#Gustavo Flores Mejia 210120167

def tipo_cuadrilatero(lados):
    lado1, lado2, lado3, lado4 = lados

    if lado1 == lado2 == lado3 == lado4:
        return "Cuadrado"
    elif (lado1 == lado2 and lado3 == lado4) or (lado1 == lado3 and lado2 == lado4) or (lado1 == lado4 and lado2 == lado3):
        return "Rectangulo"
    else:
        return "Otro tipo de cuadrilatero"

lados = []

for i in range(4):
    lado = int(input(f"Ingresa la longitud del lado {i+1}: "))
    lados.append(lado)

resultado = tipo_cuadrilatero(lados)
print(f"El cuadrilatero es un {resultado}.")

