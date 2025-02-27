def calcular_descuento(nombre_cliente, monto_compra):
    # Definir el descuento según el monto de la compra
    if monto_compra < 50000:
        descuento = 0
    elif 50000 <= monto_compra <= 100000:
        descuento = 0.05  # 5%
    elif 100000 < monto_compra <= 700000:
        descuento = 0.11  # 11%
    elif 700000 < monto_compra <= 1500000:
        descuento = 0.18  # 18%
    else:
        descuento = 0.25  # 25%
    
    # Calcular el monto a pagar y el descuento recibido
    monto_descuento = monto_compra * descuento
    monto_pagar = monto_compra - monto_descuento
    
    # Mostrar el resultado
    print(f"Nombre del cliente: {nombre_cliente}")
    print(f"Monto de la compra: {monto_compra} COP")
    print(f"Descuento recibido: {monto_descuento} COP")
    print(f"Monto a pagar: {monto_pagar} COP")

# Ejemplo de uso
nombre = input("Ingrese el nombre del cliente: ")
monto = int(input("Ingrese el monto de la compra en COP: "))

calcular_descuento(nombre, monto)







