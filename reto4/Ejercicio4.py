# Sistema de control de temperatura para un horno industrial manteniendo la temperatura dentro de un rango de más o menos 10% de la temperatura deseada
import random

TemperaturaDeseada = int(input("Ingrese la temperatura deseada para el horno: "))
Tmax = TemperaturaDeseada + (TemperaturaDeseada*(10/100))
Tmin = TemperaturaDeseada - (TemperaturaDeseada*(10/100))
TemperaturaActual = random.randint(1,300)
print(f"La temperatura actual del horno es {TemperaturaActual}")

for i in range(1,TemperaturaDeseada,1): #usar un bucle while
    Potencia = 0.1*(TemperaturaDeseada-TemperaturaActual)
    print(f"La potencia de calentamiento es {Potencia}")
    TemperaturaActual += Potencia
    print(f"La temperatura actual es: {TemperaturaActual}")