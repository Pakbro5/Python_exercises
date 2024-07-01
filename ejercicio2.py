''' Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta. '''

def calcular_total_mas_propina(total_cuenta):
    propina = total_cuenta * 0.15
    total_pagar = total_cuenta + propina
    return total_pagar

total_cuenta = float(input("Introduce el total de la cuenta: "))

total_pagar = calcular_total_mas_propina(total_cuenta)

print(f"El total a pagar, incluyendo la propina, es: {total_pagar:.2f}")

  
    