import random

TemperaturaDeseada = int(input("Ingrese la temperatura deseada para el horno: "))
Tmax = TemperaturaDeseada + (TemperaturaDeseada*(10/100)) # Temperatura de error máxima
Tmin = TemperaturaDeseada - (TemperaturaDeseada*(10/100)) # Temperatura de error mínima
TemperaturaActual = random.randint(1,300) # Da una temperatura actual al azar al horno
print(f"La temperatura actual del horno es {TemperaturaActual}")

for i in range(1,TemperaturaDeseada,1): # Usar un bucle while
    Potencia = 0.1*(TemperaturaDeseada-TemperaturaActual)
    print(f"La potencia de calentamiento es: {Potencia}")
    TemperaturaActual += Potencia # Se le añade la potencia, porque si se multiplica llegaría eventualmente la temperatura a infinito y la potencia a -infinito
    print(f"La temperatura actual es: {TemperaturaActual}")
