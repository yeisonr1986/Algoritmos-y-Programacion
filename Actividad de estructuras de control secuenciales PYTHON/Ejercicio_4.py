# Solicitar el monto total de la compra
monto_compra = int(input("Ingresa el monto total de la compra en COP: "))

# Inicializar las variables
monto_invertir_empresa = 0
monto_pagar_credito = 0
monto_prestado_banco = 0
monto_intereses = 0

# Si el monto de la compra excede de 5.000.000 COP
if monto_compra > 5000000:
    # La empresa invertirá un 5% de su dinero
    monto_invertir_empresa = monto_compra * 0.05
    # Pedirá un préstamo al banco del 30% del monto total
    monto_prestado_banco = monto_compra * 0.30
    # El resto lo pagará a crédito al fabricante (65%)
    monto_pagar_credito = monto_compra * 0.65
else:
    # Si el monto no excede de 5.000.000 COP
    # La empresa invertirá un 70% de su dinero
    monto_invertir_empresa = monto_compra * 0.70
    # El 30% restante lo pagará a crédito al fabricante
    monto_pagar_credito = monto_compra * 0.30

# El fabricante cobra un 20% de intereses sobre el monto a crédito
monto_intereses = monto_pagar_credito * 0.20

# Imprimir los resultados
print(f"\nMonto a invertir de los fondos de la empresa: {monto_invertir_empresa:.2f} COP")
print(f"Monto a pagar a crédito: {monto_pagar_credito:.2f} COP")
print(f"Monto a pagar por intereses: {monto_intereses:.2f} COP")

# Si se pidió préstamo al banco, mostrar el monto prestado
if monto_prestado_banco > 0:
    print(f"Monto prestado al banco: {monto_prestado_banco:.2f} COP")


