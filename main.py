from modulos.datos import cargar_paises_csv
from visualizacion import mostrar_menu, mostrar_paises
from operaciones import (
    agregar_pais,
    actualizar_pais,
    buscar_pais_por_nombre,
    filtrar_por_continente,
    filtrar_por_poblacion,
    filtrar_por_superficie,
    ordenar_paises
)
from estadisticas import mostrar_estadisticas


ARCHIVO_CSV = "paises.csv"


def main():
    paises = cargar_paises_csv(ARCHIVO_CSV)

    opcion = ""

    while opcion != "10":
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_paises(paises)

        elif opcion == "2":
            agregar_pais(paises, ARCHIVO_CSV)

        elif opcion == "3":
            actualizar_pais(paises, ARCHIVO_CSV)

        elif opcion == "4":
            buscar_pais_por_nombre(paises)

        elif opcion == "5":
            filtrar_por_continente(paises)

        elif opcion == "6":
            filtrar_por_poblacion(paises)

        elif opcion == "7":
            filtrar_por_superficie(paises)

        elif opcion == "8":
            ordenar_paises(paises)

        elif opcion == "9":
            mostrar_estadisticas(paises)

        elif opcion == "10":
            print("Saliendo del programa...")

        else:
            print("Opción inválida. Intente nuevamente.")


main()