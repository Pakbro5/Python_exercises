''' Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros. '''

def conversor_dolares_a_euros(dolares):
      conversion = 0.85
      return dolares * conversion
    
dolares = float(input("Introduce la cantidad en dólares: "))

euros = conversor_dolares_a_euros(dolares)

print(f"La cantidad total de dolares convertidos a euros son: {euros}")