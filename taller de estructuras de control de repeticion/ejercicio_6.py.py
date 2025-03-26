# division 2 numeros
dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))
if divisor == 0:
    print("Error: El divisor no puede ser cero.")
else:
    cociente = 0 
    residuo = dividendo
    while residuo >= divisor:
        residuo -= divisor
        cociente += 1  
    print(f"Cociente: {cociente}")
    print(f"Residuo: {residuo}")



   

