# CARGA DE PAISES
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

# AGREGAR PAIS (1)

def agregar_pais(paises):

    # Validar nombre
    while True:
        nombre = input("Ingrese el nombre del país: ").strip().capitalize()
        if nombre != "":
            break
        print("El nombre no puede estar vacío.")

    # Verificar si ya existe
    for pais in paises:
        if pais["nombre"] == nombre:
            print("Ese país ya existe.")
            return

    # Validar población
    while True:
        try:
            poblacion = int(input("Ingrese la población: "))
            if poblacion > 0:
                break
            print("La población debe ser mayor que 0.")
        except ValueError:
            print("Debe ingresar un número.")

    # Validar superficie
    while True:
        try:
            superficie = int(input("Ingrese la superficie: "))
            if superficie > 0:
                break
            print("La superficie debe ser mayor que 0.")
        except ValueError:
            print("Debe ingresar un número.")

    # Validar continente
    while True:
        continente = input("Ingrese el continente: ").strip().capitalize()
        if continente != "":
            break
        print("El continente no puede estar vacío.")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)

    print("País agregado correctamente.")

# BUSCAR PAIS (3)

def buscar_pais(paises):
    while True:
        nombre_buscado = input("Ingrese el nombre del país: ").strip()
        if nombre_buscado != "":
            break
        print("Debe ingresar un nombre.")
    encontrado = False
    for pais in paises:
        if nombre_buscado.lower() in pais["nombre"].lower():
            print("\nPaís encontrado:")
            print(pais)
            encontrado = True
    if not encontrado:
        print("No se encontraron países.")

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
        buscar_pais(paises)

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