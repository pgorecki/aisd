# -*- encoding: utf8 -*-

import unittest

from my_list import LinkedList, Node

import unittest

class TestList(unittest.TestCase):

    def test_nowa_lista_nie_ma_glowy(self):
        l = LinkedList()
        self.assertEqual(l.head, None)


    def test_wstawienie_pierwszego_elementu(self):
        l = LinkedList()
        l.insert(Node(10))
        self.assertEqual(l.head.data, 10)

    def test_wstawienie_2_elementow(self):
        l = LinkedList()
        l.insert(Node(10))
        l.insert(Node(20))
        self.assertEqual(l.head.data, 20)
        self.assertEqual(l.head.next.data, 10)

    def test_wstawienie_3_elementow(self):
        l = LinkedList()
        l.insert(Node(10))
        l.insert(Node(20))
        l.insert(Node(30))
        self.assertEqual(l.head.data, 30)
        self.assertEqual(l.head.next.data, 20)
        self.assertEqual(l.head.next.next.data, 10)

    def test_wyszukiwanie_z_porazka(self):
        l = LinkedList()
        l.insert(Node(10))
        l.insert(Node(20))
        l.insert(Node(30))
        self.assertEqual(l.search(40), None)

    def test_wyszukiwanie_sukces_ostatni(self):
        l = LinkedList()
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        l.insert(n1)
        l.insert(n2)
        l.insert(n3)
        self.assertEqual(l.search(10), n1)

    def test_wyszukiwanie_sukces_pierwszy(self):
        l = LinkedList()
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        l.insert(n1)
        l.insert(n2)
        l.insert(n3)
        self.assertEqual(l.search(30), n3)


if __name__ == '__main__':
    unittest.main()

