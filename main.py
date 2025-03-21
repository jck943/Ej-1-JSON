import json

datos = json.load(open("datos.json"))

# Quien es el fundador de Audi y cuando lo fundo. Ejemplo: Flautin el flautas creó Audi en el año 1679
print(f"{datos["fundacion"]["fundador"]} creó Audi en el año {datos["fundacion"]["año"]}")

# Cual es el eslogan de Audi. Ejemplo: Eslogan: Las mariposas vuelan
print(f"Eslogan: {datos["eslogan"]}")

# Mostrar el nombre de cada tecnología seguido de su descripción, con un salto de línea entre cada una"
for tecnologia in datos["tecnologia_destacada"]:
    print(tecnologia["nombre"])
    print(tecnologia["descripcion"])
    print()

# Modelos populares de Audi en forma de lista
print("Modelos populares de Audi: ")
for modelo in datos["modelos_populares"]:
    print(f"- {modelo}")
print()

# Las principales competencias de Audi dadas la vuelta
print("Principales competencias de Audi: ")
for i in range(len(datos["competencia"]) - 1, -1, -1):
    print(f"- {datos["competencia"][i]}")
print()

# Mostrar el modelo popular número 3 seguido de la descripción del elemento 5 de tecnologia_destacada
print(f"{datos["modelos_populares"][2]}: {datos["tecnologia_destacada"][4]["descripcion"]}")