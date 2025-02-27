def deporte_apropiado(temperatura):
    # Determinar el deporte según la temperatura
    if temperatura > 85:
        deporte = "Natación"
    elif 70 < temperatura <= 85:
        deporte = "Tenis"
    elif 32 < temperatura <= 70:
        deporte = "Golf"
    elif 10 < temperatura <= 32:
        deporte = "Esquí"
    else:
        deporte = "Marcha"
    
    # Mostrar el resultado
    print(f"A una temperatura de {temperatura}°F, el deporte apropiado es: {deporte}")

# Ejemplo de uso
temperatura = int(input("Ingrese la temperatura en grados Fahrenheit: "))
deporte_apropiado(temperatura)










