import math

def resolver_ecuacion_cuadratica(A, B, C):
    # Calcular el discriminante
    D = B**2 - 4*A*C
    
    if D > 0:
        # Si D > 0, hay dos soluciones reales
        X1 = (-B + math.sqrt(D)) / (2 * A)
        X2 = (-B - math.sqrt(D)) / (2 * A)
        return f"Las soluciones son: X1 = {X1} y X2 = {X2}"
    elif D == 0:
        # Si D = 0, hay una única solución
        X1 = X2 = -B / (2 * A)
        return f"La solución doble es: X1 = X2 = {X1}"
    else:
        # Si D < 0, no hay soluciones reales
        return "No tiene solución en los Reales."

# Ejemplo de uso
A = int(input("Introduce el valor de A: "))
B = int(input("Introduce el valor de B: "))
C = int(input("Introduce el valor de C: "))

resultado = resolver_ecuacion_cuadratica(A, B, C)
print(resultado)





