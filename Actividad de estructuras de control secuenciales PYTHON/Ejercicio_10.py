def calcular_aumento(categoria, sueldo_bruto):
    # Definir los aumentos según la categoría
    if categoria == 1:
        aumento_porcentaje = 0.10  # 10%
    elif categoria == 2:
        aumento_porcentaje = 0.15  # 15%
    elif categoria == 3:
        aumento_porcentaje = 0.20  # 20%
    elif categoria == 4:
        aumento_porcentaje = 0.40  # 40%
    elif categoria == 5:
        aumento_porcentaje = 0.60  # 60%
    else:
        print("Categoría no válida.")
        return

    # Calcular el aumento y el nuevo sueldo bruto
    aumento = sueldo_bruto * aumento_porcentaje
    nuevo_sueldo = sueldo_bruto + aumento
    
    # Mostrar el resultado
    print(f"Categoría: {categoria}")
    print(f"Nuevo sueldo bruto: {nuevo_sueldo} COP")

# Ejemplo de uso
categoria = int(input("Ingrese la categoría del trabajador (1 a 5): "))
sueldo_bruto = int(input("Ingrese el sueldo bruto del trabajador en COP: "))









