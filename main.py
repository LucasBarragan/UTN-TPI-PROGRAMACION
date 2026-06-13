from archivo import cargar_paises_csv

from paises import(
    agregar_pais,
    actualizar_pais,
    buscar_pais
)

from filtros import(filtrar_paises)

from ordenamiento import(ordenar_paises)

from estadisticas import(mostrar_estadisticas)

paises = cargar_paises_csv()

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