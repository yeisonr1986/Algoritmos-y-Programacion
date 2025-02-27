

def desglosar_cantidad(cantidad):
    # Definir los valores de los billetes y monedas en COP
    billetes_y_monedas = [
        (100000, "Billetes de 100.000 COP"),
        (50000, "Billetes de 50.000 COP"),
        (20000, "Billetes de 20.000 COP"),
        (10000, "Billetes de 10.000 COP"),
        (5000, "Billetes de 5.000 COP"),
        (2000, "Billetes de 2.000 COP"),
        (1000, "Billetes de 1.000 COP"),
        (500, "Monedas de 500 COP"),
        (200, "Monedas de 200 COP"),
        (100, "Monedas de 100 COP"),
        (50, "Monedas de 50 COP")
    ]
    
    # Iterar sobre las denominaciones de billetes y monedas
    for valor, nombre in billetes_y_monedas:
        cantidad_billetes_o_monedas = cantidad // valor
        if cantidad_billetes_o_monedas > 0:
            print(f"{cantidad_billetes_o_monedas} {nombre}")
        cantidad %= valor  # Actualizamos la cantidad restante

# Ejemplo de uso
cantidad = int(input("Ingrese una cantidad en COP: "))
desglosar_cantidad(cantidad)









