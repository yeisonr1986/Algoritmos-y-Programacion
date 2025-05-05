intentos = 3
while intentos > 0:
    usuario = input("introduce-tu-nombre-de-usuario: ")
    contraseña = input("introduce-tu-contraseña: ")

    if usuario in usuario and usuario[usuario]["passwoord"] == contraseña:
        nombre = usuario[usuario]["nombre"]
        apellido = usuario[usuario]["apellido"]
        print(f"¡bienvenido, {nombre} {apellido}!")
        break
    else:
        intentos -=1
        print(f"usuario-o-contraseña-incorrectos-te-quedan {intentos} intento(s).")

if intentos == 0:
    print("has-agotado-los-intentos. acceso-denegado.")
