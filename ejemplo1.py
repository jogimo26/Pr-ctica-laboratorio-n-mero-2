numero = int(input("Teclea un número (0 para salir): "))

while numero != 0:
    if numero > 0:
        print("Es positivo\n")
        numero = int(input("Teclea un número (0 para salir): "))
    else:
        print("Es negativo\n")
        numero = int(input("Teclea un número (0 para salir): "))
print("Hemos culminado!... Hasta pronto!")