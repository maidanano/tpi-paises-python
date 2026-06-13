# ---------------- FUNCIONES DE VALIDACIÓN ----------------

def pedir_texto_no_vacio(mensaje):
    
    #Se solicita un texto y valida que no esté vacío.
    
    texto = input(mensaje).strip()

    while texto == "":
        print("Error: el campo no puede estar vacío.")
        texto = input(mensaje).strip()

    return texto


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


def pedir_rango(mensaje_minimo, mensaje_maximo):
    
    #Se solicita un rango mínimo y máximo, validando que el mínimo no sea mayor al máximo.
    
    minimo = pedir_entero_positivo(mensaje_minimo)
    maximo = pedir_entero_positivo(mensaje_maximo)

    while minimo > maximo:
        print("Error: el valor mínimo no puede ser mayor que el valor máximo.")
        minimo = pedir_entero_positivo(mensaje_minimo)
        maximo = pedir_entero_positivo(mensaje_maximo)

    return minimo, maximo

def pedir_continente(mensaje):
    print("Continentes disponibles:")
    for i, c in enumerate(CONTINENTES_VALIDOS, 1):
        print(f" {i}. {c}")

    while True:
        texto = input(mensaje).strip()
        for continente in CONTINENTES_VALIDOS:
            if continente.lower() == texto.lower():
                return continente
        print(f"Error: continente inválido. Ingrese uno de la lista")

