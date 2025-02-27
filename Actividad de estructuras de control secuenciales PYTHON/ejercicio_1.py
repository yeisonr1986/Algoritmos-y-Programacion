def calcular_inversion(principal, tasa_interes, anos):
    # Calcular el monto final con los intereses compuestos
    monto_final = principal * (1 + tasa_interes) ** anos
    
    # Calcular los intereses generados
    intereses = monto_final - principal
    
    # Verificar si los intereses superan los $100,000 COP
    if intereses > 100000:
        print(f"Los intereses exceden los 100.000 COP. Se reinvierten.")
        principal = monto_final  # Reinvierte los intereses
        return calcular_inversion(principal, tasa_interes, anos)  # Llama recursivamente
    else:
        return monto_final, intereses

# Parámetros de entrada
principal = int(input("Introduce el monto de la inversión inicial (50000): "))
tasa_interes = int(input("Introduce la tasa de interés anual (en %): ")) / 100  # Convertir a decimal
anos = int(input("Introduce el número de años de la inversión: "))

# Calcular el monto final
monto_final, intereses = calcular_inversion(principal, tasa_interes, anos)

# Mostrar resultados
print(f"\nMonto final después de {anos} años: {monto_final:.2f} 50000")
print(f"Intereses generados: {intereses:.2f} 50000")

