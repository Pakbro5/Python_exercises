''' Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda). '''

def es_un_palindromo(palabra):
    invertir_palabra = palabra[::-1]
    if palabra == invertir_palabra:
        return True 
    else:
        return False  
    
palabra = input("Introduce una palabra: ")
if es_un_palindromo(palabra):
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")