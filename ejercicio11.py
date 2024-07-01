''' Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual. '''

def calcular_edad_usurio(año_nacimiento):
    año_actual = 2024
    return año_actual - año_nacimiento

año_nacimiento = int(input("Introduce tu año de nacimiento: "))

edad = calcular_edad_usurio(año_nacimiento)

print(f"Tu edad es: {edad} años")    