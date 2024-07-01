''' Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.). '''

def dia_de_la_semana(numero):
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    if 1 <= numero <= 7:
        return dias[numero - 1]
    else:
        return "Número no válido"


numero = int(input("Introduce un número del 1 al 7: "))

dia = dia_de_la_semana(numero)

print(f"El día de la semana es: {dia}")

    

    