# saldo cajero
saldo = 1000.0
while True:
    print("\n--- Cajero Automático ---")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")
    if opcion == "1":
        deposito = int(input("Ingrese el monto a depositar: "))
        if deposito > 0:
            saldo += deposito
            print(f"Has depositado ${deposito:.2f}. Saldo actual: ${saldo:.2f}")
        else:
            print("El monto debe ser positivo.")
    elif opcion == "2": 
        retiro = int(input("Ingrese el monto a retirar: "))
        if retiro > saldo:
            print("Saldo insuficiente para realizar el retiro.")
        elif retiro <= 0:
            print("El monto debe ser positivo.")
        else:
            saldo -= retiro
            print(f"Has retirado ${retiro:.2f}. Saldo actual: ${saldo:.2f}")
    elif opcion == "3":  # Consultar saldo
        print(f"Tu saldo actual es: ${saldo:.2f}")
    elif opcion == "4":  # Salir
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción entre 1 y 4.")



   

