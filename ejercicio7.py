''' Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario. '''

def calculadora(a, b, operacion):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplicacion":
        return a * b
    elif operacion == "division":
        return a / b
    else:
        return "Operación no válida"

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (suma, resta, multiplicacion, division): ")
resultado = calculadora(a, b, operacion)
print(f"El resultado de la {operacion} es: {resultado}")
