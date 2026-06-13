# ---------------- FUNCIONES PRINCIPALES DEL SISTEMA ----------------

def agregar_pais(paises):
    """
    Agrega un nuevo país a la lista.
    No permite campos vacíos ni países repetidos por nombre exacto.
    """
    print("\n---------- AGREGAR PAÍS ----------")

    nombre = pedir_texto_no_vacio("Ingrese el nombre del país: ")

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Error: el país ya existe en el sistema.")
            return

    poblacion = pedir_entero_positivo("Ingrese la población: ")
    superficie = pedir_entero_positivo("Ingrese la superficie en km²: ")
    continente = pedir_continente("Ingrese el continente: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    guardar_paises_csv(ARCHIVO_CSV, paises)

    print("País agregado correctamente.")


def actualizar_pais(paises):
    """
    Actualiza población y superficie de un país buscado por nombre exacto.
    """
    print("\n---------- ACTUALIZAR PAÍS ----------")

    nombre = pedir_texto_no_vacio("Ingrese el nombre exacto del país a actualizar: ")

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("\nPaís encontrado:")
            mostrar_pais(pais)

            nueva_poblacion = pedir_entero_positivo("Ingrese la nueva población: ")
            nueva_superficie = pedir_entero_positivo("Ingrese la nueva superficie en km²: ")

            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie

            guardar_paises_csv(ARCHIVO_CSV, paises)

            print("Datos actualizados correctamente.")
            return

    print("No se encontró un país con ese nombre.")


def buscar_pais_por_nombre(paises):
    """
    Busca países por coincidencia parcial o exacta en el nombre.
    """
    print("\n---------- BUSCAR PAÍS ----------")

    busqueda = pedir_texto_no_vacio("Ingrese el nombre o parte del nombre del país: ")

    resultados = []

    for pais in paises:
        if busqueda.lower() in pais["nombre"].lower():      #Clave el comando 'in, ya que sobre strings devuelve True si el texto
            resultados.append(pais)                         #buscado aparece en cualquier parte del nombre, no solo al principio

    if len(resultados) == 0:
        print("No se encontraron países con ese criterio de búsqueda.")
    else:
        print("\nResultados encontrados:")
        mostrar_paises(resultados)


def filtrar_por_continente(paises):
    """
    Filtra países por continente.
    """
    print("\n---------- FILTRAR POR CONTINENTE ----------")

    continente = pedir_continente("Ingrese el continente: ")

    resultados = []

    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron países para ese continente.")
    else:
        mostrar_paises(resultados)


def filtrar_por_poblacion(paises):
    """
    Filtra países según un rango de población.
    """
    print("\n---------- FILTRAR POR RANGO DE POBLACIÓN ----------")

    minimo, maximo = pedir_rango(
        "Ingrese la población mínima: ",
        "Ingrese la población máxima: "
    )

    resultados = []

    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron países dentro de ese rango de población.")
    else:
        mostrar_paises(resultados)


def filtrar_por_superficie(paises):
    """
    Filtra países según un rango de superficie.
    """
    print("\n---------- FILTRAR POR RANGO DE SUPERFICIE ----------")

    minimo, maximo = pedir_rango(
        "Ingrese la superficie mínima en km²: ",
        "Ingrese la superficie máxima en km²: "
    )

    resultados = []

    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron países dentro de ese rango de superficie.")
    else:
        mostrar_paises(resultados)

