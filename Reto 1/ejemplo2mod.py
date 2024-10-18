contador = 1
inicio = int(input("Ingrese el número desde donde desea ver los ID de inventario: "))
for contador in range(inicio,inicio+10,1): # Modificación al ejemplo 2, lo que hace es, dentro de un rango comprendido entre inicio y inicio+10 sacar la ID de inventario
    print(f"El ID de inventario es: {contador}")
    contador += 1
print("Hemos culminado!... Hasta pronto!")
