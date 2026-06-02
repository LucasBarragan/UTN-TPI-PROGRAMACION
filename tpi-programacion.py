def cargar_paises_csv():
    paises = []

    archivo = open("paises.csv", "r")

    # Saltar encabezado
    archivo.readline()

    for linea in archivo:
        linea = linea.strip()
        datos = linea.split(",")

        pais = {
            "nombre": datos[0],
            "poblacion": int(datos[1]),
            "superficie": int(datos[2]),
            "continente": datos[3]
        }

        paises.append(pais)

    archivo.close()

    return paises


# Prueba

paises = cargar_paises_csv()

print(f"Se cargaron {len(paises)} países.")

for pais in paises:
    print(pais)