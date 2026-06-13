# ---------------- FUNCIONES DE VALIDACIÓN ----------------

CONTINENTES_VALIDOS = ["America", "Europa", "Asia", "Africa", "Oceania"]


#Función que pide texto no vacío
def pedir_texto_no_vacio(mensaje):
    
    #Se solicita un texto y valida que no esté vacío.
    
    texto = input(mensaje).strip()

    while texto == "":
        print("Error: el campo no puede estar vacío.")
        texto = input(mensaje).strip()

    return texto


#Función que pide entero positivo
def pedir_entero_positivo(mensaje):
    
    #Se solicita un número entero positivo.
    
    while True:
        try:
            numero = int(input(mensaje))

            if numero > 0:
                return numero
            else:
                print("Error: debe ingresar un número mayor a cero.")

        except ValueError:
            print("Error: debe ingresar un número entero válido.")


#Función que pide un rango mínimo y máximo
def pedir_rango(rango_minimo, rango_maximo):
    
    #Se solicita un rango mínimo y máximo, validando que el mínimo no sea mayor al máximo.
    
    minimo = pedir_entero_positivo(rango_minimo)
    maximo = pedir_entero_positivo(rango_maximo)

    while minimo > maximo:
        print("Error: el valor mínimo no puede ser mayor que el valor máximo.")
        minimo = pedir_entero_positivo(rango_minimo)
        maximo = pedir_entero_positivo(rango_maximo)

    return minimo, maximo


#Función que pide un continente válido
def pedir_continente(mensaje):
    print("Continentes disponibles:")
    
    for i, c in enumerate(CONTINENTES_VALIDOS, 1):
        print(f"{c}")

    while True:
        texto = input(mensaje).strip()
        for continente in CONTINENTES_VALIDOS:
            if continente.lower() == texto.lower():
                return continente
        print(f"Error: continente inválido. Ingrese uno de la lista")


#Funcion que pide el nombre de un país, validando que no esté vacío ni contenga solo números,
# y devuelve el nombre con la primera letra en mayúscula.
def pedir_nombre_pais(mensaje):

    nombre = input(mensaje).strip()

    while nombre == "" or nombre.isdigit():
        if nombre == "":
            print("Error: el nombre del país no puede estar vacío.")
        else:
            print("Error: el nombre del país no puede ser solo números.")

        nombre = input(mensaje).strip()

    return nombre.title()


