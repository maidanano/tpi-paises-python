# ---------------- FUNCIONES DE ESTADÍSTICAS ----------------

#Funciones para mostrar estadísticas generales del dataset, como el país con mayor población, menor población, promedio de población y superficie, y cantidad de países por continente.


from .visualizacion import mostrar_pais

#Función que muestra el país con mayor población
def mostrar_pais_mayor_poblacion(paises):
    mayor = paises[0]

    for pais in paises:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais

    print("\nPaís con mayor población:")
    mostrar_pais(mayor)


#Función que muestra el país con menor población
def mostrar_pais_menor_poblacion(paises):
    menor = paises[0]

    for pais in paises:
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

    print("\nPaís con menor población:")
    mostrar_pais(menor)


#Función que calcula el promedio de población de paises en el dataset
def calcular_promedio_poblacion(paises):
    suma = 0

    for pais in paises:
        suma += pais["poblacion"]

    return suma / len(paises)


#Función que calcula el promedio de superficie de paises en el dataset y devuelve el resultado.
def calcular_promedio_superficie(paises):
    suma = 0

    for pais in paises:
        suma += pais["superficie"]

    return suma / len(paises)


#Función que cuenta cuántos países hay por continente y devuelve un diccionario con continente como clave y cantidad como valor.
def contar_paises_por_continente(paises):
    """
    Cuenta cuántos países hay por continente.
    Devuelve un diccionario con continente como clave y cantidad como valor.
    """
    conteo = {}

    for pais in paises:
        continente = pais["continente"]

        if continente in conteo:
            conteo[continente] += 1
        else:
            conteo[continente] = 1

    return conteo


#Función que muestra todas las estadísticas calculadas. Recibe la lista de países como parámetro.
#Muestra el país con mayor población, menor población, promedio de población y superficie, y cantidad de países por continente.
def mostrar_estadisticas(paises):
    
    print("\n---------- ESTADÍSTICAS ----------")

    if len(paises) == 0:
        print("No hay datos disponibles para calcular estadísticas.")
        return

    mostrar_pais_mayor_poblacion(paises)
    mostrar_pais_menor_poblacion(paises)

    promedio_poblacion = calcular_promedio_poblacion(paises)
    promedio_superficie = calcular_promedio_superficie(paises)

    print(f"\nPromedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f} km²")

    conteo = contar_paises_por_continente(paises)

    print("\nCantidad de países por continente:")

    for continente in conteo:
        print(f"{continente}: {conteo[continente]}")
