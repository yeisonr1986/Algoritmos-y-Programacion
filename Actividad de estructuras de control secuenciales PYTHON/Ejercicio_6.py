# Solicitar los 4 dígitos
A = int(input("Ingresa el primer dígito (A): "))
B = int(input("Ingresa el segundo dígito (B): "))
C = int(input("Ingresa el tercer dígito (C): "))
D = int(input("Ingresa el cuarto dígito (D): "))

# Formar el número N
N = 1000 * A + 100 * B + 10 * C + D

# Redondear N a la centena más próxima
# Extraemos las dos últimas cifras
decenas_y_unidades = N % 100

# Si las decenas y unidades son 50 o más, redondeamos hacia arriba
if decenas_y_unidades >= 50:
    N_redondeado = (N // 100) * 100 + 100
else:
    N_redondeado = (N // 100) * 100

# Imprimir el resultado
print(f"El número N es: {N}")
print(f"El número redondeado a la centena más próxima es: {N_redondeado}")




