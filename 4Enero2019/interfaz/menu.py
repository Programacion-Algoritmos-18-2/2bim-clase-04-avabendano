#!/usr/bin/python
# -*- coding: utf-8 -*-
# Victoria

class Menu(object):

    # Metodo que imprime un menu y retorna una opcion en texto
    def menuPrincipal(self):
        print('\t=== MENU ===')
        print('Metodo de ordenacion:')
        print('1 - Ordenamiento por nombre')
        print('2 - Ordenamiento por ciudad')
        print('3 - Ordenamiento por campeonatos')
        print('4 - Ordenamiento por numero de jugadores')
        op = int(input('\tOpcion: '))

        if op == 1:
            return 'nombre'
        elif op == 2:
            return 'ciudad'
        elif op == 3:
            return 'campeonato'
        elif op == 4:
            return 'numJugador'
