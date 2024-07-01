''' Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros. '''

def conversor_millas_a_kilometros(millas):
    distancia = millas * 1.60934
    return distancia

millas = float(input("Introduce la distancia en millas: "))
kilometros = conversor_millas_a_kilometros(millas)
print(f"{millas} millas son {kilometros} kilómetros")