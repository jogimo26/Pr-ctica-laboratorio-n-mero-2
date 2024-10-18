inicio = int(input("Proporcione el inicio del rango para el cual se van a ver los números pares: "))
fin = int(input("Proporcione el final del rango para el cual se van a ver los números pares: "))
print("Los números pares en el rango indicado son: \n")

if inicio % 2 == 0: # Si el número es par entonces va de inicio a fin con incremento 2
    for i in range(inicio,fin,2):
        print(i,end=" ")
else:
    for i in range(inicio+1,fin,2): #Si el número es impar le suma 1 a inicio (para que quede par) y va hasta al fin, con step de 2
        print(i,end=" ")
print("\nHasta aquí!!!")
