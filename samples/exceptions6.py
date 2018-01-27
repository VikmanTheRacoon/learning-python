#!/usr/bin/env python
# -*- coding: utf-8 -*-


def diviser(x, y):
    try:
        resultat = x / y
    except ZeroDivisionError:
        print('Division par zéro')
    else:
        print('Résultat = ', resultat)
    finally:
        print('Clause finally éxecutée')


def main():
    pass


if __name__ == '__main__':
    main()
