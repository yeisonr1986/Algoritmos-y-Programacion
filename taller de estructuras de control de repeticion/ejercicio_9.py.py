# analisis puntajes
nombres = []
puntajes = []
while True:
    nombre = input("Ingrese el nombre del estudiante: ")
    puntaje = int(input(f"Ingrese el puntaje de {nombre}: "))
     nombres.(nombres)
    puntajes.(puntajes)
    continuar = input("¿Desea ingresar otro estudiante? (Sí/No): ").strip().lower()
    if continuar != "sí" and continuar != "si":
        break
max_puntaje = max(puntajes)
min_puntaje = min(puntajes)
estudiante_max = nombres[puntajes.index(max_puntaje)]
estudiante_min = nombres[puntajes.index(min_puntaje)]
promedio = sum(puntajes) / len(puntajes)
porcentaje_inferior = (len([p for p in puntajes if p < promedio]) / len(puntajes)) * 100
porcentaje_superior = (len([p for p in puntajes if p > promedio]) / len(puntajes)) * 100
print("\n--- Resultados del análisis ---")
print(f"Estudiante con puntaje más alto: {estudiante_max} con {max_puntaje}")
print(f"Estudiante con puntaje más bajo: {estudiante_min} con {min_puntaje}")
print(f"Puntaje máximo obtenido: {max_puntaje}")
print(f"Puntaje mínimo obtenido: {min_puntaje}")
print(f"Promedio de puntajes: {promedio:.2f}")
print(f"Porcentaje de estudiantes con puntajes inferiores al promedio: {porcentaje_inferior:.2f}%")
print(f"Porcentaje de estudiantes con puntajes superiores al promedio: {porcentaje_superior:.2f}%")


   

