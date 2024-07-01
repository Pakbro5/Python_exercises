''' Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100. '''

def suma_numeros_pares():
    return sum(i for i in range(1, 101) 
               if i % 2 == 0)

print(f"La suma de todos los números pares del 1 al 100 es: {suma_numeros_pares()}")