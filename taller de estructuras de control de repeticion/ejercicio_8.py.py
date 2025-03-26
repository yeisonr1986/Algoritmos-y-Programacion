# analisis encuesta
total_encuestados = 0
consumen_licor = 0
mujeres_menores = 0
hombres_no_aguardiente = 0
suma_edades_cerveza = 0
consumidores_cerveza = 0
consumidores_whisky = 0
while True:
    total_encuestados += 1  
    consume = int(input("¿Consume licor? (Sí/No): "))
    if consume == "sí" or consume == "si":
        consumen_licor += 1 
        print("Licor preferido:\n1-Aguardiente\n2-Ron\n3-Cerveza\n4-Tequila\n5-Whisky\n6-Otro")
        licor = int(input("Ingrese el número del licor preferido: "))
        edad = int(input("Ingrese su edad: "))
        sexo = int(input("Ingrese su sexo (M/F): "))
        if sexo == "F" and edad < 18:
            mujeres_menores = 1
        if sexo == "M" and 20 <= edad <= 25 and licor != 1:
            hombres_no_aguardiente += 1
        if licor == 3: 
            suma_edades_cerveza += edad
            consumidores_cerveza += 1
        if licor == 5:  
            consumidores_whisky += 1
    continuar = int(input("¿Desea continuar con la encuesta? (Sí/No): ").strip().lower()
     if continuar != "sí" and continuar != "si":
        break
print("\n--- Resultados de la encuesta ---")
print(f"Total de personas encuestadas que consumen licor: {consumen_licor}")
print(f"Total de mujeres menores de edad: {mujeres_menores}")
print(f"Total de hombres entre 20 y 25 años que no consumen aguardiente: {hombres_no_aguardiente}")
if consumidores_cerveza > 0:
    promedio_cerveza = suma_edades_cerveza / consumidores_cerveza
    print(f"Promedio de edad de quienes consumen cerveza: {promedio_cerveza:.2f} años")
else:
    print("No hay consumidores de cerveza registrados.")
porcentaje_whisky = (consumidores_whisky / total_encuestados) * 100
print(f"Porcentaje de personas que consumen whisky: {porcentaje_whisky:.2f}%")



   

