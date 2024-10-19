# Resistencias por medio de un bucle
# Se usa un bucle while para manejar la parte de la elección por parte del usuario
print("Ingrese un número con el cual calcular las resistencias, las elecciones son: \n 1. Resistencias en serie \n 2. Resistencias en paralelo \n 3. Resistencias mixtas (R1, R2 en serie, R3 en paralelo) \n 4. Resistencias mixtas (R1, R3 en serie, R2 en paralelo) \n 5. Resistencias mixtas (R2, R3 en serie, R1 en paralelo)")
variable = int(input("Ingrese su elección, ingrese 0 para salir: "))

while variable > 0 and variable <= 5: # Bucle con condiición, limita lo que puede escoger el usuario
    if variable == 1: # Resistencias en serie
        print("Qué valor tienen sus resistencias a calcular?")
        R1 = float(input("Por favor ingrese el valor de R1: "))
        R2 = float(input("Por favor ingrese el valor de R2: "))
        R3 = float(input("Por favor ingrese el valor de R3: "))
        LimSuperior = float(input("Ingrese el límite superior (en Ω) para las resistencias a calcular: ")) # Límite superior dado por el usuario, como es establecido en el documento
        Rtotal = R1+R2+R3 # Procedimiento de la Req
        print("El factor de corrección de esta operación es de aumento de 5%.")
        Rtotal += (0.05*Rtotal) # Factor de corrección
        if Rtotal > LimSuperior: # Validación de límites
            Rtotal += 20
            print(f"ADVERTENCIA: La resistencia total se ha tenido que corregir debido a que la resistencia total en serie calculada ha sido de más de {LimSuperior} Ω. El nuevo valor de la resistencia total es: {Rtotal}")
        else:
            print("El valor total de su resistencia es: ", Rtotal)
    elif variable == 2: # Resistencias en paralelo
        print("Qué valor tienen sus resistencias a calcular?")
        R1 = float(input("Por favor ingrese el valor de R1: "))
        R2 = float(input("Por favor ingrese el valor de R2: "))
        R3 = float(input("Por favor ingrese el valor de R3: "))
        LimInferior = float(input("Ingrese el límite inferior (en Ω) para las resistencias a calcular: ")) # Límite inferior dado por el usuario, como es establecido en el documento
        Rtotal = (1 / ((1/R1) + (1/R2) + (1/R3))) # Procedimiento de la Req
        print("El factor de corrección de esta operación es de disminución de 10%.") 
        Rtotal =- (0.1*Rtotal) # Factor de corrección, se le resta a Rtotal el valor de 0.1*Rtotal, o sea, el 10% de la Rtotal
        if Rtotal < LimInferior: # Validación de límites
            Rtotal -= 2
            print(f"ADVERTENCIA: La resistencia total se ha tenido que corregir debido a que la resistencia total en serie calculada ha sido de menos de {LimInferior} Ω. El nuevo valor de la resistencia total es: {Rtotal}")
        else:
            print("El valor total de su resistencia es: ",Rtotal)
    elif variable == 3: # Mixtas, R1 y R2 en serie, R3 en paralelo
        print("Qué valor tienen sus resistencias a calcular?")
        R1 = float(input("Por favor ingrese el valor de R1: "))
        R2 = float(input("Por favor ingrese el valor de R2: "))
        R3 = float(input("Por favor ingrese el valor de R3: "))
        Rtotal = (1 / ((1/(R1+R2)) + (1/R3))) # Procedimiento de la Req
        print("No hay un factor de corrección para esta operación.")
        print("El valor total de su resistencia es: ",Rtotal)
    elif variable == 4: # Mixtas, R1 y R3 en serie, R2 en paralelo
        print("Qué valor tienen sus resistencias a calcular?")
        R1 = float(input("Por favor ingrese el valor de R1: "))
        R2 = float(input("Por favor ingrese el valor de R2: "))
        R3 = float(input("Por favor ingrese el valor de R3: "))    
        Rtotal = (1 / ((1/(R1+R3)) + (1/R2))) # Procedimiento de la Req
        print("No hay un factor de corrección para esta operación.")
        print("El valor total de su resistencia es: ",Rtotal)
    elif variable == 5: # Mixtas, R2 y R3 en serie, R1 en paralelo
        print("Qué valor tienen sus resistencias a calcular?")
        R1 = float(input("Por favor ingrese el valor de R1: "))
        R2 = float(input("Por favor ingrese el valor de R2: "))
        R3 = float(input("Por favor ingrese el valor de R3: ")) 
        Rtotal = 1 / ((1/(R2+R3)) + (1/R1)) # Procedimiento de la Req
        print("No hay un factor de corrección para esta operación.")
        print("El valor total de su resistencia es: ",Rtotal)
    elif variable == 0: # Salida
        print("Gracias por usar el programa!")
        break
    variable = int(input("Ingrese su elección, ingrese 0 para salir: "))
