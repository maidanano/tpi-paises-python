# ---------------- FUNCIONES DE ORDENAMIENTO ----------------

from modulos.visualizacion import mostrar_paises


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

    if opcion != "1" and opcion != "2" and opcion != "3":
            print("Opción inválida.")
            return

    print("\nTipo de orden:")
    print("1. Ascendente")
    print("2. Descendente")

    tipo_orden = input("Seleccione una opción: ")

    if tipo_orden == "1":
        descendente = False
    elif tipo_orden == "2":
        descendente = True
    else:
        print("Opción de orden inválida.")
        return

    if opcion == "1":
        paises_ordenados = sorted(paises, key=obtener_nombre, reverse=descendente)
    elif opcion == "2":
        paises_ordenados = sorted(paises, key=obtener_poblacion, reverse=descendente)
    else:
        paises_ordenados = sorted(paises, key=obtener_superficie, reverse=descendente)

    mostrar_paises(paises_ordenados)
