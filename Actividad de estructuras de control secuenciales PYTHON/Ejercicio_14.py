def calcular_pago(lectura_anterior, lectura_actual):
    # Calcular el consumo en Kwh
    consumo = lectura_actual - lectura_anterior
    
    # Definir las tarifas según el rango de consumo
    if 0 <= consumo <= 100:
        tarifa = 4600  # 4.600 COP/Kwh
    elif 101 <= consumo <= 300:
        tarifa = 8000  # 8.000 COP/Kwh
    elif 301 <= consumo <= 500:
        tarifa = 10000  # 10.000 COP/Kwh
    else:
        tarifa = 12000  # 12.000 COP/Kwh
    
    # Calcular el monto a pagar
    monto_luz = consumo * tarifa
    
    # Mostrar el resultado
    print(f"Consumo de energía eléctrica: {consumo} Kwh")
    print(f"Tarifa por Kwh: {tarifa} COP")
    print(f"Monto a pagar por consumo de energía eléctrica: {monto_luz} COP")
    
    # Calcular el servicio de aseo urbano (supuesto: costo fijo)
    servicio_aseo = 5000  # Costo fijo del servicio de aseo urbano (por ejemplo)
    
    # Calcular el monto total
    monto_total = monto_luz + servicio_aseo
    print(f"Monto por servicio de aseo urbano: {servicio_aseo} COP")
    print(f"Total a pagar (luz + aseo): {monto_total} COP")

# Ejemplo de uso
lectura_anterior = int(input("Ingrese la lectura anterior del medidor (Kwh): "))
lectura_actual = int(input("Ingrese la lectura actual del medidor (Kwh): "))

calcular_pago(lectura_anterior, lectura_actual)









