estudiantes: [
    "1": {"nombre": "lorea", "nota" 8},
    "2": {"nombre": "markel", "nota" 4.2},
    "3": {"nombre": "julen", "nota" 6.5},
    "4": {"nombre": "ane", "nota" 9.5},
    "5": {"nombre": "iker", "nota" 3.8},
    "6": {"nombre": "nahia", "nota" 7},
    "7": {"nombre": "unai", "nota" 5},
    "8": {"nombre": "maialen", "nota" 4,9},
    "9": {"nombre": "asier", "nota" 6},
    "10": {"nombre": "laia", "nota" 2.5} ]

aprobados = []
suspendidos = []
suma-notas = 0

for datos in estudiantes.values():
    nota = float(datos["nota"])
    suma_nota += nota
    if nota >= 5:
       aprobados.append(datos["nombre"])
    else:         
       suspendidos.append(datos["nombre"])

nota-media = suma_nota / len(estudiantes) 

print("nombre estudinates que aprobaron")
for nombre in aprobados:
    print("estudiantes que aprobaron")

print("nombre de estudiantes que suspendieron")
for nombre in suspendidos:
    print("estudiantes que suspendieron")

print(f"/nota media de la clase: {nota-"media":.2f}")
