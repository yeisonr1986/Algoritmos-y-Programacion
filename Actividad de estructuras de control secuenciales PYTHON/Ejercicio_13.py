

from datetime import datetime

def obtener_signo_y_edad(fecha_nacimiento):
    # Definir los signos zodiacales con sus fechas
    signos = [
        ("Sagitario", (11, 22), (12, 21)),
        ("Capricornio", (12, 22), (1, 20)),
        ("Acuario", (1, 21), (2, 19)),
        ("Piscis", (2, 20), (3, 19)),
        ("Aries", (3, 21), (4, 20)),
        ("Tauro", (4, 21), (5, 21)),
        ("Géminis", (5, 22), (6, 21)),
        ("Cáncer", (6, 22), (7, 22)),
        ("Leo", (7, 23), (8, 23)),
        ("Virgo", (8, 24), (9, 22)),
        ("Libra", (9, 23), (10, 22)),
        ("Escorpión", (10, 23), (11, 21))
    ]
    
    # Extraer la fecha de nacimiento
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
    dia = fecha_nacimiento.day
    mes = fecha_nacimiento.month
    
    # Calcular el signo
    for signo, (mes_inicio, dia_inicio), (mes_fin, dia_fin) in signos:
        if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fin and dia <= dia_fin) or (mes > mes_inicio and mes < mes_fin):
            signo_zodiacal = signo
            break
    
    # Calcular la edad
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year
    if fecha_actual.month < fecha_nacimiento.month or (fecha_actual.month == fecha_nacimiento.month and fecha_actual.day < fecha_nacimiento.day):
        edad -= 1
    
    # Mostrar el resultado
    print(f"Tu signo zodiacal es: {signo_zodiacal}")
    print(f"Tu edad es: {edad} años")

# Ejemplo de uso
fecha_nacimiento = input("Ingresa tu fecha de nacimiento (dd/mm/aaaa): ")
obtener_signo_y_edad(fecha_nacimiento)








