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
    "nombre": nombre.title(),
    "poblacion": poblacion,
    "superficie": superficie,
    "continente": continente.title()
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
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']} km²")

            # Nueva población
            while True:
                nueva_poblacion = input("Ingrese la nueva población: ")
                if nueva_poblacion.isdigit():
                    nueva_poblacion = int(nueva_poblacion)
                    if nueva_poblacion > 0:
                        break
                print("Debe ingresar un número mayor que 0.")

            # Nueva superficie
            while True:
                nueva_superficie = input("Ingrese la nueva superficie: ")
                if nueva_superficie.isdigit():
                    nueva_superficie = int(nueva_superficie)
                    if nueva_superficie > 0:
                        break
                print("Debe ingresar un número mayor que 0.")

            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie

            print("\nPaís actualizado correctamente.")
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']} km²")
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
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']} km²")
            encontrado = True

    if not encontrado:
        print("No se encontraron países.")