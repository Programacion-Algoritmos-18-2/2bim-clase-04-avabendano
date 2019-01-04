#!/usr/bin/python
# -*- coding: utf-8 -*-
# Victoria


class Equipo(object):

    # Constructor de clase
    def __init__(self, nombres, ciudad, campeonatos, numJugadores):
        self.nombres = nombres
        self.ciudad = ciudad
        self.campeonatos = campeonatos
        self.numJugadores = numJugadores

    def __str__(self):
        return "%s %s %d %d" % (self.nombres, self.ciudad, self.campeonatos, self.numJugadores)

    def __repr__(self):
        return "%s %s %d %d" % (self.nombres, self.ciudad, self.campeonatos, self.numJugadores)


class Operaciones(object):

    # Constructor de clase
    def __init__(self, listado):
        self.listado_equipos = listado

    # Metodo ordenar
    def ordenar(self):
        """
            https://docs.python.org/3/howto/sorting.html
            >>> sorted(student_objects, key=lambda student: student.age)   # sort by age
        """
        return sorted(self.listado_equipos, key=lambda equipo: equipo.nombres)
