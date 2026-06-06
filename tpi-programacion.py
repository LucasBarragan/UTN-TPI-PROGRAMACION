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
        nombre = input("Ingrese el nombre del país: ").strip().lower()
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
        continente = input("Ingrese el continente: ").strip().lower()
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

# ACTUALIZAR PAISES (2)

def actualizar_pais(paises):

    while True:
        nombre_buscado = input("Ingrese el nombre del país a actualizar: ").strip()
        if nombre_buscado != "":
            break
        print("Debe ingresar un nombre.")
    encontrado = False

    for pais in paises:
        if nombre_buscado.lower() == pais["nombre"].lower():
            print("\nPaís encontrado:")
            print(pais)
            # Nueva población
            while True:
                try:
                    nueva_poblacion = int(input("Ingrese la nueva población: "))
                    if nueva_poblacion > 0:
                        break
                    print("La población debe ser mayor que 0.")
                except ValueError:
                    print("Debe ingresar un número.")
            # Nueva superficie
            while True:
                try:
                    nueva_superficie = int(input("Ingrese la nueva superficie: "))
                    if nueva_superficie > 0:
                        break
                    print("La superficie debe ser mayor que 0.")
                except ValueError:
                    print("Debe ingresar un número.")
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            print("\nPaís actualizado correctamente.")
            print(pais)
            encontrado = True
            break

    if not encontrado:
        print("No se encontró el país.")

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

# FILTRAR PAISES (4)

# Filtro para los nombres de los paises
def filtrar_paises(paises):

    print("\n=== FILTROS ===")
    print("1. Filtrar por continente")
    print("2. Filtrar por población")
    print("3. Filtrar por superficie")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        filtrar_continente(paises)

    elif opcion == "2":
        filtrar_poblacion(paises)

    elif opcion == "3":
        filtrar_superficie(paises)

    else:
        print("Opción inválida.")

# Filtro para los continentes
def filtrar_continente(paises):

    while True:
        continente = input("Ingrese el continente: ").strip()
        if continente != "":
            break
        print("Debe ingresar un continente.")

    encontrado = False

    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            print(pais)
            encontrado = True

    if not encontrado:
        print("No se encontraron países.")

# Filtro para la población
def filtrar_poblacion(paises):

    while True:
        try:
            minimo = int(input("Ingrese la población mínima: "))
            if minimo >= 0:
                break
            print("Debe ser un número positivo.")
        except ValueError:
            print("Debe ingresar un número.")
    while True:
        try:
            maximo = int(input("Ingrese la población máxima: "))
            if maximo >= minimo:
                break
            print("Debe ser mayor o igual al mínimo.")
        except ValueError:
            print("Debe ingresar un número.")
    encontrado = False
    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            print(pais)
            encontrado = True

    if not encontrado:
        print("No se encontraron países.")

# Filtro para la superficie
def filtrar_superficie(paises):

    while True:
        try:
            minimo = int(input("Ingrese la superficie mínima: "))
            if minimo >= 0:
                break
            print("Debe ser un número positivo.")
        except ValueError:
            print("Debe ingresar un número.")

    while True:
        try:
            maximo = int(input("Ingrese la superficie máxima: "))
            if maximo >= minimo:
                break
            print("Debe ser mayor o igual al mínimo.")
        except ValueError:
            print("Debe ingresar un número.")

    encontrado = False

    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            print(pais)
            encontrado = True

    if not encontrado:
        print("No se encontraron países.")

#ORDENAR PAISES (5)
def ordenar_paises(paises):
    #muestra el menu de opciones de ordenamiento
    print("ORDENAR PAÍSES\n")
    print("1. Ordenar por nombre")
    print("2. Ordenar por población.")
    print("3. Ordenar por superficie")

    opcion = input(" Seleccione una opcín: ")

    if opcion == "1":
        ordenar_por_nombre(paises)
    elif opcion == "2":
        ordenar_por_poblacion(paises)
    elif opcion == "3":
        ordenar_por_superficie(paises)
    else:
        print("Opción inválida.")

def pedir_orden():
    # Le pregunta al usuario si quiere orden ascendente o descendente
    # Devuelve False si es ascendente, True si es descendente
    print("\n1. Ascendente")
    print("2. Descendente")
    while True:
        opcion = input("Seleccione el orden: ")
        if opcion == "1":
            return False
        elif opcion == "2":
            return True
        else:
            print("Opción inválida. Ingrese 1 o 2.")

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
        actualizar_pais(paises)

    elif opcion == "3":
        buscar_pais(paises)

    elif opcion == "4":
        filtrar_paises(paises)

    elif opcion == "5":
        print("Ordenar países")

    elif opcion == "6":
        print("Mostrar estadísticas")

    elif opcion == "0":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")