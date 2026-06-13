# ---------------- FUNCIONES DE ARCHIVO CSV ----------------

import csv
#Función cargar países
def cargar_paises_csv(nombre_archivo):
    
    #Lee el archivo CSV y carga los países en una lista de diccionarios.
    #Cada país se representa con las claves nombre, población, superficie y continente.
    
    paises = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                try:
                    nombre = fila["nombre"].strip()
                    poblacion = int(fila["poblacion"])
                    superficie = int(fila["superficie"])
                    continente = fila["continente"].strip()

                    if nombre != "" and continente != "" and poblacion > 0 and superficie > 0:
                        pais = {
                            "nombre": nombre.title(),
                            "poblacion": poblacion,
                            "superficie": superficie,
                            "continente": continente.title()
                        }

                        paises.append(pais)


                    else:
                        print("Se encontró una fila con datos vacíos o inválidos. No fue cargada.")


                except ValueError:
                    print("Error de formato en una fila del CSV. No fue cargada.")
                except KeyError:
                    print("Error: el archivo CSV no tiene las columnas requeridas.")
                    return []

    except FileNotFoundError:
        print("Error: no se encontró el archivo CSV.")
    except Exception as e_excp:
        print(f"Ocurrió un error al leer el archivo: {e_excp}")

    return paises

#Función guardar paises
def guardar_paises_csv(nombre_archivo, paises):
    #Guarda la lista de países en un archivo CSV.

    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("nombre,poblacion,superficie,continente\n")

            for pais in paises:
                linea = f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n"
                archivo.write(linea)

        print("Datos guardados correctamente en el archivo CSV.")

    except Exception as error:
        print(f"Error al guardar el archivo CSV: {error}")

