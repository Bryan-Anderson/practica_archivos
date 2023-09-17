def calcular_promedio(notas):
    return sum(notas) // len(notas)

def procesar_datos(input_data):
    estudiantes = input_data.split('|')
    promedios = []
    for estudiante in estudiantes:
        datos = estudiante.split(',')
        nombre = datos[0]
        notas = list(map(int, datos[1:]))
        promedio = calcular_promedio(notas)
        promedios.append(f"{nombre}={promedio}")
    return promedios

def guardar_en_archivo(promedios):
    with open("promedios.txt", "w") as archivo:
        archivo.write("\n".join(promedios))

if __name__ == "__main__":
    input_data = input("Ingresa los datos de los estudiantes: ")
    promedios = procesar_datos(input_data)
    guardar_en_archivo(promedios)
    print("Se ha creado el archivo 'promedios.txt' con los promedios guardados.")
