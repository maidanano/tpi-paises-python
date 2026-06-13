# ---------------- FUNCIONES PRINCIPALES DEL SISTEMA ----------------


from datos import guardar_paises_csv
from validacion import pedir_texto_no_vacio, pedir_entero_positivo, pedir_rango, pedir_continente
from visualizacion import mostrar_pais, mostrar_paises

#Funciones para agregar un país, actualizar datos de un país, buscar por nombre, y filtrar por continente, población o superficie.


#Función agregar país, que pide los datos del nuevo país, valida que no exista otro con el mismo nombre, y lo agrega a la lista de países.
def agregar_pais(paises, archivo_csv):

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
    guardar_paises_csv(archivo_csv, paises)

    print("País agregado correctamente.")


#Funcion actualizar país, que busca un país por nombre exacto, y permite actualizar su población y superficie. 
#Si el país no existe, muestra un mensaje de error.
def actualizar_pais(paises, archivo_csv):

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

            guardar_paises_csv(archivo_csv, paises)

            print("Datos actualizados correctamente.")
            return

    print("No se encontró un país con ese nombre.")


#Función buscar país por nombre, que permite buscar países por coincidencia parcial o exacta en el nombre, y muestra los resultados encontrados.
def buscar_pais_por_nombre(paises):

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


#Función filtrar por continente, que permite filtrar países por continente seleccionado, y muestra los resultados encontrados.
def filtrar_por_continente(paises):

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


#Función filtrar por población, que permite filtrar países por un rango de población ingresado por el usuario, y muestra los resultados encontrados.
def filtrar_por_poblacion(paises):

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


#Función filtrar por superficie, que permite filtrar países por un rango de superficie ingresado por el usuario, y muestra los resultados encontrados.
def filtrar_por_superficie(paises):

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

