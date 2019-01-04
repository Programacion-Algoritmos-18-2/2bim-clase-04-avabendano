#!/usr/bin/python
# -*- coding: utf-8 -*-
# Victoria

import codecs
import sys


class MiArchivo:

    # Constructor de clase
    def __init__(self):
        self.archivo = codecs.open("data/informacion.csv", "r")

    # Metodo que devuelve todas las lineas del archivo
    def obtener_informacion(self):
        return self.archivo.readlines()

    # Metodo que cierra la lectura del archivo
    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir:

    # Constructor de clase
    def __init__(self):
        self.archivo = codecs.open("data/informacion2.csv", "a")

    # Metodo encargado de escrbir el objeto Equipo en el nuevo archivo
    def agregar_informacion(self, equipo):
        # Usamos | para mantener relacion con el archivo original
        self.archivo.write("%s|%s|%d|%d\n" % (
            equipo.nombres, equipo.ciudad, equipo.campeonatos, equipo.numJugadores))

    # Metodo que escribe un texto en el archivo
    def agregar_linea(self, texto):
        self.archivo.write(texto)

    # Metodo que cierra la escritura del archivo
    def cerrar_archivo(self):
        self.archivo.close()
