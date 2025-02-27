# Solicitar el sueldo del trabajador
sueldo = int(input("Ingresa el sueldo del trabajador (en COP): "))

# Calcular el aumento según el sueldo
if sueldo < 900000:
    aumento = sueldo * 0.15  # 15% de aumento
else:
    aumento = sueldo * 0.12  # 12% de aumento

# Calcular el nuevo sueldo
nuevo_sueldo = sueldo + aumento

# Imprimir el nuevo sueldo
print(f"El nuevo sueldo del trabajador es: {nuevo_sueldo:.2f} COP")

