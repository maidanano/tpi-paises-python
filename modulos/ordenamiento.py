# ---------------- FUNCIONES DE ORDENAMIENTO ----------------

from visualizacion import mostrar_paises


#Función que obtiene el nombre de un país, en minúsculas, para usar como clave de ordenamiento.
def obtener_nombre(pais):
    return pais["nombre"].lower()


#Función que obtiene la población de un país, para usar como clave de ordenamiento.
def obtener_poblacion(pais):
    return pais["poblacion"]


#Función que obtiene la superficie de un país, para usar como clave de ordenamiento.
def obtener_superficie(pais):
    return pais["superficie"]


#Función que ordena los países por nombre, población o superficie, según la elección del usuario, y muestra los resultados ordenados.
def ordenar_paises(paises):

    print("\n---------- ORDENAR PAÍSES ----------")
    print("1. Ordenar por nombre")
    print("2. Ordenar por población")
    print("3. Ordenar por superficie")

    opcion = input("Seleccione una opción: ")

    print("\nTipo de orden:")
    print("1. Ascendente")
    print("2. Descendente")

    tipo_orden = input("Seleccione una opción: ")

    descendente = False

    if tipo_orden == "2":
        descendente = True
    elif tipo_orden != "1":
        print("Opción de orden inválida.")
        return

    if opcion == "1":
        paises_ordenados = sorted(paises, key=obtener_nombre, reverse=descendente)
    elif opcion == "2":
        paises_ordenados = sorted(paises, key=obtener_poblacion, reverse=descendente)
    elif opcion == "3":
        paises_ordenados = sorted(paises, key=obtener_superficie, reverse=descendente)
    else:
        print("Opción inválida.")
        return

    mostrar_paises(paises_ordenados)
