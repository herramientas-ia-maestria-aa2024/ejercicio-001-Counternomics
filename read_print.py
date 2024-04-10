# Leer el archivo de texo
with open('informacion.txt', 'r') as file:
    # Correr un bucle por cada linea
    for line in file:
        # Imprimir linea
        print(line.rstrip())
