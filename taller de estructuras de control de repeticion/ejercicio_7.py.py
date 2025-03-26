# buscar > altura
num_estudiantes = int(input("Ingrese el número de estudiantes: "))
if num_estudiantes <= 0:
    print("El número de estudiantes debe ser mayor que 0.")
else:
    max_altura = 0  
    for i in range(1, num_estudiantes + 1):
        altura = int(input(f"Ingrese la altura del estudiante {i} (en cm): "))
        if altura > max_altura:  
            max_altura = altura
    print(f"La mayor altura es: {max_altura} cm")



   

