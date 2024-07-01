''' Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona. '''

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Introduce tu peso en kg: "))

altura = float(input("Introduce tu altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"Tu IMC es: {imc:.2f}")
