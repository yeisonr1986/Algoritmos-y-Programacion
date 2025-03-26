# Leer numero
numero = int(input("Ingrese un número entero positivo: "))
if numero <= 0:
    print("El número debe ser un entero positivo.")
else:
    suma = 0  
    for divisor in range(1, numero):
        if numero % divisor == 0: 
            suma += divisor
    if suma == numero:
        print(f"{numero} es un número perfecto.")
    else:
        print(f"{numero} no es un número perfecto.")


   

