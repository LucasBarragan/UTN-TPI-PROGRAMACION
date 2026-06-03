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

paises = cargar_paises_csv()

# AGREGAR PAIS

def agregar_pais(paises):

    nombre = input("Ingrese el nombre del país: ").capitalize()
    poblacion = int(input("Ingrese la población: "))
    superficie = int(input("Ingrese la superficie: "))
    continente = input("Ingrese el continente: ").capitalize()

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)

    print("País agregado correctamente.")
    #print(paises[-1]) probamos si funciona

# MENU

def mostrar_menu():
    print("\n=== GESTIÓN DE PAÍSES ===")
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    return opcion



while True:
    opcion = mostrar_menu()

    if opcion == "1":
        agregar_pais(paises)

    elif opcion == "2":
        print("Actualizar país")

    elif opcion == "3":
        print("Buscar país")

    elif opcion == "4":
        print("Filtrar países")

    elif opcion == "5":
        print("Ordenar países")

    elif opcion == "6":
        print("Mostrar estadísticas")

    elif opcion == "0":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")