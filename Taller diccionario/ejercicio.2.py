datos = {"mike": 3, "ane": 8, "amaia": 12, "unai": 5, "jon": 8, "ainhoa": 7, "maite": 5}
valores_unicos = []
for valor in datos.values():
    if valor not in valores_unicos:
        valores_unicos.append(valor)
print(valores_unicos)        