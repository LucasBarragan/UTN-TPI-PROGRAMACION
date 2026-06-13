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