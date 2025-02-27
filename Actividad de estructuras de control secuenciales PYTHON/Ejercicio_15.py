def determinar_anemia(edad, sexo, hemoglobina):
    # Condiciones para la edad y el rango de hemoglobina
    if edad <= 1:
        if 13 <= hemoglobina <= 26:
            return "Negativo"
        else:
            return "Positivo"
    elif edad <= 6:
        if 10 <= hemoglobina <= 18:
            return "Negativo"
        else:
            return "Positivo"
    elif edad <= 12:
        if 11 <= hemoglobina <= 15:
            return "Negativo"
        else:
            return "Positivo"
    elif edad <= 5:
        if 11.5 <= hemoglobina <= 15:
            return "Negativo"
        else:
            return "Positivo"
    elif edad <= 10:
        if 12.6 <= hemoglobina <= 15.5:
            return "Negativo"
        else:
            return "Positivo"
    elif edad <= 15:
        if 13 <= hemoglobina <= 15.5:
            return "Negativo"
        else:
            return "Positivo"
    elif sexo == "F" and edad > 15:  # Mujer mayor de 15 años
        if 12 <= hemoglobina <= 16:
            return "Negativo"
        else:
            return "Positivo"
    elif sexo == "M" and edad > 15:  # Hombre mayor de 15 años
        if 14 <= hemoglobina <= 18:
            return "Negativo"
        else:
            return "Positivo"
    else:
        return "Datos no válidos"  # En caso de que los datos no sean válidos

# Ejemplo de uso
edad = int(input("Introduce la edad de la persona: "))
sexo = input("Introduce el sexo de la persona (M para hombre, F para mujer): ").upper()
hemoglobina = float(input("Introduce el nivel de hemoglobina (g%): "))

resultado = determinar_anemia(edad, sexo, hemoglobina)
print(f"Resultado: {resultado}")










