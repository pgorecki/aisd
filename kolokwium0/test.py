# -*- encoding: utf8 -*-

import unittest
import hashlib
from zadania import *

#
# UWAGA!!!!
# Nie modyfikuj tego pliku. Modyfikacja pliku skutkować będzie otrzymaniem 0 punktów z kolokwium
#

# jest 5 testów, więc można uzyskać max. 5 punktów 

class Kolokwium0(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(hashlib.md5(open('test.py', 'rb').read()).hexdigest())

    def test_zad1a(self):
        self.assertTrue(czy_pierwsza(3))
        self.assertTrue(czy_pierwsza(5))
        self.assertTrue(czy_pierwsza(997))
        self.assertFalse(czy_pierwsza(4))
        self.assertFalse(czy_pierwsza(15))
        self.assertFalse(czy_pierwsza(447))

    def test_zad1b(self):
        self.assertFalse(czy_pierwsza(1))
        self.assertTrue(czy_pierwsza(2))

    def test_zad2(self):
        self.assertEqual(1, suma_od_do([1],0,0))
        self.assertEqual(1, suma_od_do([1,2,3],0,0))
        self.assertEqual(2, suma_od_do([1,2,3],1,1))
        self.assertEqual(3, suma_od_do([1,2,3],2,2))
        self.assertEqual(5, suma_od_do([1,2,3],1,2))
        self.assertEqual(3, suma_od_do([1,2,4],0,1))
        self.assertEqual(7, suma_od_do([1,2,4],0,2))

    def test_zad3a(self):
        self.assertEqual([3,4,5,6], kopiuj_z_pominieciem([1,2,3,4,5,6],[1,2]))
        self.assertEqual([4,5,6,7,8], kopiuj_z_pominieciem([1,2,3,4,5,6,7,8],[1,2,3]))
        self.assertEqual([1,2,3,4,5,6,7,8], kopiuj_z_pominieciem([1,2,3,4,5,6,7,8],[9,10,11]))

    def test_zad3b(self):
        self.assertEqual([], kopiuj_z_pominieciem([1,2,3],[1,2,3]))
        self.assertEqual([4], kopiuj_z_pominieciem([1,2,3,3,4],[1,2,3]))
        self.assertEqual([], kopiuj_z_pominieciem([1,1,1,1,1],[1,1,1]))

if __name__ == '__main__':
    unittest.main()
