''' Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no. '''

def edad_usuario(edad):
    return edad >= 18
  
edad = int(input("Introduce la edad: "))
if edad_usuario(edad):
    print("Es mayor de edad")
else:
    print("No es mayor de edad")