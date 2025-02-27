def verificar_expresion(P, Q):
    # Calculamos la expresión P^3 + Q^4 - 2*P^2
    resultado = P**3 + Q**4 - 2*(P**2)
    
    # Verificamos si la expresión es mayor que 680
    if resultado > 680:
        print("P y Q satisfacen la expresión: P = " + str(P) + ", Q = " + str(Q))
    else:
        print("P y Q no satisfacen la expresión: P = " + str(P) + ", Q = " + str(Q))

# Ejemplo de uso
P = int(input("Ingrese el valor de P: "))
Q = int(input("Ingrese el valor de Q: "))

verificar_expresion(P, Q)






