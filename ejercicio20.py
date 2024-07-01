''' Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el
usuario. '''

def total_suma_numeros(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma
  
numeros = list(map(int, input("Introduce una lista de números separados por espacio: ").split()))

suma = total_suma_numeros(numeros)

print(f"La suma de los números en la lista es: {suma}")