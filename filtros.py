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
