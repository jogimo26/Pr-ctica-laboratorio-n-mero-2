inicio = int(input("Proporcione el inicio del rango para el cual se van a ver los números pares: "))
fin = int(input("Proporcione el final del rango para el cual se van a ver los números pares: "))
print("Los números pares en el rango indicado son: \n")

if inicio % 2 == 0:
    for i in range(inicio,fin,2):
        print(i,end=" ")
else:
    for i in range(inicio+1,fin,2):
        print(i,end=" ")
print("\nHasta aquí!!!")