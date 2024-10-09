contador = 1
inicio = int(input("Ingrese el número desde donde desea ver los ID de inventario: "))
for contador in range(inicio,inicio+10,1):
    print(f"El ID de inventario es: {contador}")
    contador += 1
print("Hemos culminado!... Hasta pronto!")