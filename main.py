from archivo import cargar_paises_csv

from paises import(
    agregar_pais,
    actualizar_pais,
    buscar_pais
)

from filtros import(filtrar_paises)

from ordenamiento import(ordenar_paises)

paises = cargar_paises_csv()





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