''' Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario. '''

def contador_pares_impares(lista):
    pares = sum(1 for numero in lista if numero % 2 == 0)
    impares = len(lista) - pares
    return pares, impares
  
numeros = list(map(int, input("Introduce una lista de números separados por espacio: ").split()))
pares, impares = contador_pares_impares(numeros)
print(f"En la lista hay {pares} números pares y {impares} números impares.")