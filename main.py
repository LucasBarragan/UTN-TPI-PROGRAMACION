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


def bubble_sort(paises, campo, descendente):
    # Ordena la lista usando el Bubble Sort
    # Recibe la lista, el campo por el que ordenar y si es descendente trabaja sobre una copia para no modificar la lista original
    lista_ordenada = paises[:]
    n = len(lista_ordenada)

    for i in range(n - 1):
        for j in range(n - 1 - i):

            # Obtiene los valores a comparar de los dos países 
            valor_actual = lista_ordenada[j][campo]
            valor_siguiente = lista_ordenada[j + 1][campo]

            # Si se comparan nombres, ignora mayúsculas/minúsculas
            if campo == "nombre":
                valor_actual = valor_actual.lower()
                valor_siguiente = valor_siguiente.lower()

            # Decide si hay que intercambiar según el orden elegido
            if not descendente:
                intercambiar = valor_actual > valor_siguiente
            else:
                intercambiar = valor_actual < valor_siguiente

            # Si corresponde, intercambia los dos elementos
            if intercambiar:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]

    return lista_ordenada

def mostrar_lista_ordenada(lista, campo, descendente):
    # Muestra el resultado del ordenamiento con un encabezado descriptivo
    orden_texto = "descendente" if descendente else "ascendente"
    print(f"\n=== Países ordenados por {campo} ({orden_texto}) ===")
    for pais in lista:
        print(pais)


def ordenar_por_nombre(paises):
    # Pide el orden, ordena por nombre y muestra el resultado
    descendente = pedir_orden()
    lista_ordenada = bubble_sort(paises, "nombre", descendente)
    mostrar_lista_ordenada(lista_ordenada, "nombre", descendente)


def ordenar_por_poblacion(paises):
    # Pide el orden, ordena por población y muestra el resultado
    descendente = pedir_orden()
    lista_ordenada = bubble_sort(paises, "poblacion", descendente)
    mostrar_lista_ordenada(lista_ordenada, "población", descendente)

def ordenar_por_superficie(paises):
    # Pide el orden, ordena por superficie y muestra el resultado
    descendente = pedir_orden()
    lista_ordenada = bubble_sort(paises, "superficie", descendente)
    mostrar_lista_ordenada(lista_ordenada, "superficie", descendente)

def mostrar_estadisticas(paises):
    # Verifica que haya países cargados antes de calcular
    if len(paises) == 0:
        print("No hay países cargados.")
        return

    print("\n=== ESTADÍSTICAS ===")

 # Busca el país con mayor y menor población recorriendo toda la lista
    pais_mayor_pob = paises[0]
    pais_menor_pob = paises[0]
    for pais in paises:
        if pais["poblacion"] > pais_mayor_pob["poblacion"]:
            pais_mayor_pob = pais
        if pais["poblacion"] < pais_menor_pob["poblacion"]:
            pais_menor_pob = pais

    print(f"\nPaís con MAYOR población: {pais_mayor_pob}")
    print(f"País con MENOR población: {pais_menor_pob}")
    
    # Calcula el promedio de población sumando y dividiendo por la cantidad
    total_poblacion = 0
    for pais in paises:
        total_poblacion += pais["poblacion"]
    print(f"\nPromedio de población: {total_poblacion // len(paises):,}")

    # Calcula el promedio de superficie de la misma forma
    total_superficie = 0
    for pais in paises:
        total_superficie += pais["superficie"]
    print(f"Promedio de superficie: {total_superficie // len(paises):,} km²")

    # Cuenta cuántos países hay por continente usando un diccionario
    # La clave es el nombre del continente y el valor es la cantidad
    continentes = {}
    for pais in paises:
        continente = pais["continente"]
        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\nCantidad de países por continente:")
    for continente, cantidad in continentes.items():
        print(f"   {continente}: {cantidad} país/es")

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
        ordenar_paises(paises)

    elif opcion == "6":
        mostrar_estadisticas(paises)

    elif opcion == "0":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")