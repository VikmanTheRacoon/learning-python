#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
import random

tickets_disponibles = 10


class VendeurTickets(threading.Thread):
    tickets_vendus = 0

    def __init__(self, semaphore):
        super().__init__()
        self.sem = semaphore
        print('Le vendeur {} de ticket à commencé son travail'.format(self.getName()))

    def run(self):
        global tickets_disponibles
        running = True
        while running:
            self.random_delay()
            self.sem.acquire()
            if tickets_disponibles <= 0:
                running = False
            else:
                self.tickets_vendus += 1
                tickets_disponibles -= 1
                print('Le vendeur {} a vendu un ticket ({} restants)'.format(self.getName(), tickets_disponibles))
            self.sem.release()
        print('Le vendeur {} a vendu {} ticket(s) '.format(self.getName(), self.tickets_vendus))

    def random_delay(self):
        time.sleep(random.randint(0, 1))


def main():
    semaphore = threading.Semaphore()
    vendeurs = []
    for i in range(4):
        vendeur = VendeurTickets(semaphore)
        vendeur.start()
        vendeurs.append(vendeur)
    for vendeur in vendeurs:
        vendeur.join()


if __name__ == '__main__':
    main()
