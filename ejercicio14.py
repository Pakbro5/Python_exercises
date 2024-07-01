''' Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%. '''

def calcular_precio_final(precio):
    descuento = 0.20
    return precio * (1 - descuento)

precio = float(input("Introduce el precio del artículo: "))

precio_final = calcular_precio_final(precio)

print(f"El precio final después de aplicar el descuento del 20% es: {precio_final:.2f}")
