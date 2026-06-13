# ---------------- FUNCIONES DE VISUALIZACIÓN ----------------

#Funciones para mostrar el menú, un país o una lista de países.


#Función que muestra el menú principal del sistema.
def mostrar_menu():

    print("\n---------- MENÚ PRINCIPAL ----------")
    print("1. Mostrar todos los países")
    print("2. Agregar un país")
    print("3. Actualizar población y superficie de un país")
    print("4. Buscar país por nombre")
    print("5. Filtrar países por continente")
    print("6. Filtrar países por rango de población")
    print("7. Filtrar países por rango de superficie")
    print("8. Ordenar países")
    print("9. Mostrar estadísticas")
    print("0. Salir")


#Muestra los datos de un país.
def mostrar_pais(pais):

    
    print(f"Nombre: {pais['nombre']}")
    print(f"Población: {pais['poblacion']}")
    print(f"Superficie: {pais['superficie']} km²")
    print(f"Continente: {pais['continente']}")
    print("-----------------------------------")


#Muestra una lista de países.
def mostrar_paises(paises):

    
    if len(paises) == 0:
        print("No hay países para mostrar.")
    else:
        print("\n---------- LISTADO DE PAÍSES ----------")
        for pais in paises:
            mostrar_pais(pais)
