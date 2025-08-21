
#For

# Lista
my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print("Lista:", element)

# Tupla
my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print("Tupla:", element)

# Conjunto (set)
my_set = {"Brais", "Moure", 35}

for element in my_set:
    print("Set:", element)

# Diccionario
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

# Recorriendo solo las claves
for key in my_dict:
    print("Diccionario (clave):", key)

# Recorriendo claves y valores
for key, value in my_dict.items():
    print("Diccionario (clave-valor):", key, "→", value)
