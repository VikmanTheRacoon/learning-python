#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    """The entry point of the script

    This function will act as an entry point for the script.

    Args:
        None

    Returns:
        None

    Raises:
        None

    """
    fruits = [
        'orange',
        'pomme',
        'poire',
        'banane',
        'kiwi',
        'pomme',
        'banane']

    # Affiche le nombre de pommes
    print(fruits.count('pomme'))

    # Affiche le nombre de coing
    print(fruits.count('coing'))

    # Affiche la postion de la première occurence de banane
    fruits.index('banane')

    # Affiche la postion de la première occurence de banane à partie de l'index 4
    fruits.index('banane', 4)

    # Renverse la liste et l'affiche
    fruits.reverse()
    print(fruits)

    # Ajoute une élément à la fin
    fruits.append('raisin')
    print(fruits)

    # Trie la liste et l'affiche
    fruits.sort()
    print(fruits)

    # Récupère le dernier élément et l'enlève de la liste
    fruits.pop()
    print(fruits)


if __name__ == '__main__':
    #
    # Call the main() function
    #
    main()
