#!/usr/bin/python
# -*- coding: utf-8 -*-
# Victoria

from modelado.mimodelo import *
from paquete_archivos.miarchivo import *

# Objeto para leer el archivo de informacion.csv
archivo = MiArchivo()
# Objeto para escribir el nuevo archivo informacion2.csv
archivoNuevo = MiArchivoEscribir()

# recuperamos todas las lineas del archivo
informacion = archivo.obtener_informacion()
# cerramos el archivo, ya que la informacion esta guardada en la variable informacion
archivo.cerrar_archivo()
# Separamos los datos de cada linea
informacion = [l.split("|") for l in informacion]

# Creamos una lista vacia
lista_equipos = []

# Por cada linea de inforamcion se crea un objeto Equipo
for dato in informacion:
    equipo = Equipo(dato[0], dato[1], int(dato[2]), int(dato[3]))
    # Agregamos el equipo a la lista
    lista_equipos.append(equipo)

# Creamos un objeto operacion
operacion = Operaciones(lista_equipos)
# Sobreescribimos la lista_equipos con su version ordenada
# usando el metodo de ordenar de la clase Operaciones
lista_equipos = operacion.ordenar()

# Bloque para imprimir en consola el resultado
print("\nEquipos ordenados por nombre:")
for equipo in lista_equipos:
    print(equipo)
print()
# Fin bloque

# Por cada Equipo en la lista se escribe una linea en el nuevo archivo
for equipo in lista_equipos:
    archivoNuevo.agregar_informacion(equipo)

# Cerramos el archivo informacion2.csv
archivoNuevo.cerrar_archivo()
