# 🌍 Gestión de Datos de Países en Python

> Trabajo Práctico Integrador (TPI) — Programación 1  
> Tecnicatura Universitaria en Programación a Distancia (TUPAD)  
> Universidad Tecnológica Nacional — UTN  
> 2° Cuatrimestre 2025

---

## 📋 Descripción del programa

Sistema de gestión de datos de países desarrollado en **Python 3**, que permite administrar un dataset almacenado en un archivo CSV. El programa corre completamente en consola y aplica los conceptos fundamentales de la materia: listas, diccionarios, funciones, estructuras condicionales y repetitivas, ordenamientos y estadísticas.

Cada país se representa con cuatro atributos: nombre, población, superficie (en km²) y continente. Al iniciar, el sistema carga los datos desde `paises.csv` en una lista de diccionarios en memoria. Todos los cambios (agregar o actualizar países) se guardan automáticamente en el archivo CSV.

### Funcionalidades

| Opción | Función |
|--------|---------|
| 1 | Mostrar todos los países |
| 2 | Agregar un nuevo país |
| 3 | Actualizar población y superficie de un país |
| 4 | Buscar país por nombre (coincidencia parcial) |
| 5 | Filtrar por continente |
| 6 | Filtrar por rango de población |
| 7 | Filtrar por rango de superficie |
| 8 | Ordenar por nombre, población o superficie |
| 9 | Mostrar estadísticas del dataset |
| 0 | Salir |

---

## ⚙️ Requisitos

- Python 3.x (sin dependencias externas)
- El archivo `paises.csv` debe estar en la misma carpeta que `main.py`

---

## 🚀 Instrucciones de uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/tpi-paises-python.git
cd tpi-paises-python
```

### 2. Ejecutar el programa

```bash
python main.py
```

### 3. Navegar el menú

Al iniciar, el programa carga los datos del CSV y muestra el menú principal. Ingresá el número de la opción deseada y presioná Enter.

```
---------- MENÚ PRINCIPAL ----------
1. Mostrar todos los países
2. Agregar un país
3. Actualizar población y superficie de un país
4. Buscar país por nombre
5. Filtrar países por continente
6. Filtrar países por rango de población
7. Filtrar países por rango de superficie
8. Ordenar países
9. Mostrar estadísticas
0. Salir
Ingrese una opción:
```

---

## 📂 Estructura del proyecto

```
tpi-paises-python/
├── main.py       # Código fuente completo
├── paises.csv    # Dataset base de países
└── README.md     # Este archivo
└── modulos       # Módulo de funciones
└── capturas      # Capturas del código de Python
```

---

## 💡 Ejemplos de entradas y salidas

### Agregar un país

```
Ingrese una opción: 2

---------- AGREGAR PAÍS ----------
Ingrese el nombre del país: Paraguay
Ingrese la población: 7353038
Ingrese la superficie en km²: 406752
Ingrese el continente: América
País agregado correctamente.
Datos guardados correctamente en el archivo CSV.
```

> Si el país ya existe, el sistema lo informa y no lo agrega:
```
Error: el país ya existe en el sistema.
```

> Si se deja un campo vacío, el sistema lo vuelve a pedir:
```
Ingrese el nombre del país:
Error: el campo no puede estar vacío.
Ingrese el nombre del país:
```

> Si se escribe el país solo con letras, el sistema lo vuelve a pedir:
---
Error: el nombre del país no puede ser solo números.


### Buscar por nombre (coincidencia parcial)

```
Ingrese una opción: 4

---------- BUSCAR PAÍS ----------
Ingrese el nombre o parte del nombre del país: ar

Resultados encontrados:
---------- LISTADO DE PAÍSES ----------
Nombre: Argentina
Población: 45376763
Superficie: 2780400 km²
Continente: América
-----------------------------------
Nombre: Arabia Saudita
Población: 34813871
Superficie: 2149690 km²
Continente: Asia
-----------------------------------
```

> La búsqueda no distingue mayúsculas de minúsculas: "ar", "AR" y "Ar" devuelven el mismo resultado.

> Si no hay coincidencias:
```
No se encontraron países con ese criterio de búsqueda.
```

---

### Filtrar por continente

```
Ingrese una opción: 5

---------- FILTRAR POR CONTINENTE ----------
Continentes disponibles:
America
Europa
Asia
Africa
Oceania
Ingrese el continente: Oceanía

---------- LISTADO DE PAÍSES ----------
Nombre: Australia
Población: 25690000
Superficie: 7692024 km²
Continente: Oceanía
-----------------------------------
Nombre: Nueva Zelanda
Población: 5122600
Superficie: 268021 km²
Continente: Oceanía
-----------------------------------
```

---

### Filtrar por rango de población

```
Ingrese una opción: 6

---------- FILTRAR POR RANGO DE POBLACIÓN ----------
Ingrese la población mínima: 50000000
Ingrese la población máxima: 150000000

---------- LISTADO DE PAÍSES ----------
Nombre: Francia
Población: 67750000
Superficie: 643801 km²
Continente: Europa
-----------------------------------
Nombre: Japón
Población: 125800000
Superficie: 377975 km²
Continente: Asia
-----------------------------------
```

> Si el mínimo es mayor que el máximo, el sistema lo detecta y vuelve a pedir los valores:
```
Error: el valor mínimo no puede ser mayor que el valor máximo.
```

---

### Ordenar países

```
Ingrese una opción: 8

---------- ORDENAR PAÍSES ----------
1. Ordenar por nombre
2. Ordenar por población
3. Ordenar por superficie
Seleccione una opción: 2

Tipo de orden:
1. Ascendente
2. Descendente
Seleccione una opción: 2

---------- LISTADO DE PAÍSES ----------
Nombre: China
Población: 1412000000
Superficie: 9596961 km²
Continente: Asia
-----------------------------------
Nombre: India
Población: 1408000000
Superficie: 3287263 km²
Continente: Asia
-----------------------------------
...
```

---

### Estadísticas

```
Ingrese una opción: 9

---------- ESTADÍSTICAS ----------

País con mayor población:
Nombre: China
Población: 1412000000
Superficie: 9596961 km²
Continente: Asia
-----------------------------------

País con menor población:
Nombre: Uruguay
Población: 3426260
Superficie: 176215 km²
Continente: América
-----------------------------------

Promedio de población: 101876438.14
Promedio de superficie: 2394270.38 km²

Cantidad de países por continente:
América: 7
Europa: 5
Asia: 5
Oceanía: 2
África: 2
```

---

### Actualizar un país

```
Ingrese una opción: 3

---------- ACTUALIZAR PAÍS ----------
Ingrese el nombre exacto del país a actualizar: Argentina

País encontrado:
Nombre: Argentina
Población: 45376763
Superficie: 2780400 km²
Continente: América
-----------------------------------
Ingrese la nueva población: 46000000
Ingrese la nueva superficie en km²: 2780400
Datos actualizados correctamente.
```

---

## 👥 Integrantes del equipo

**| Nombre completo | Legajo | Comisión | Módulos desarrollados |**
|----------------|--------|----------------------|
| Mariano Ezequiel Maidana | [Legajo 1] |  Comisión M26 C1-08  | Agregar/actualizar países, validaciones, ordenamientos |

| Mariano Gallo | Matrícula 103050 |  Comisión M26 C1-10 | Carga CSV, modularización, filtros, estadísticas |

---

## 🎥 Video demostrativo

[Insertar link al video aquí]

> El video muestra el funcionamiento completo del sistema en consola, la estructura del código y la explicación de las decisiones técnicas tomadas.

---

## 📄 Documentación

[Insertar link al informe PDF aquí]

---

## 📚 Bibliografía utilizada

- Downey, A. (2015). *Think Python* — https://greenteapress.com/wp/think-python-2e/
- Sweigart, A. (2020). *Automate the Boring Stuff with Python* — https://automatetheboringstuff.com
- Videos y materiales del aula virtual — Campus UTN TUPAD
