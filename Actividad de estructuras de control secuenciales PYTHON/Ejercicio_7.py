def calcular_pago(distancia_recorrida):
    if distancia_recorrida <= 300:
        # Si la distancia es 300 km o menos, se cobra 50000 COP
        return 50000
    elif distancia_recorrida > 300 and distancia_recorrida <= 1000:
        # Si la distancia es mayor a 300 km pero menor o igual a 1000 km
        # Se cobran 70000 COP más 30000 COP por cada km adicional
        km_extra = distancia_recorrida - 300
        return 70000 + (30000 * km_extra)
    else:
        # Si la distancia es mayor a 1000 km
        # Se cobran 150000 COP más 9000 COP por cada km adicional
        km_extra = distancia_recorrida - 1000
        return 150000 + (9000 * km_extra)

# Ejemplo de uso
distancia = int(input("Ingrese la distancia recorrida en km: "))
pago = calcular_pago(distancia)
print(f"El monto a pagar es: {pago} COP")





