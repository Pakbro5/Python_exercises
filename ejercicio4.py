''' Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario. '''

def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador

palabra = input("Introduce una palabra: ")
num_vocales = contar_vocales(palabra)
print(f"La palabra '{palabra}' tiene {num_vocales} vocales.")