#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    try:
        raise Exception('bacon', 'oeufs')
    except Exception as inst:
        print(type(inst))   # L'instance de l'exception
        print(inst.args)    # arguments stockés dans .args
        print(inst)         # __str__ permet d'afficher les arguments
        x, y = inst.args    # unpack des arguments
        print('x =', x)
        print('y =', y)


if __name__ == '__main__':
    main()
