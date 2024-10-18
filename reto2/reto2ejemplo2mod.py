numero = int(input("Ingrese un número: "))
limite = int(input("Ingrese el límite de los números impares siguientes a ver: "))
contador = 1
print("Los números impares siguientes son: \n")

for i in range(numero,limite,1): # Bucle de inicio a fin
    if i % 2 == 0: # Verificar si es par, si no lo es se omite esto
        print(i,end="\n")
    contador += 1
print("Hemos culminado!... Hasta pronto!")
