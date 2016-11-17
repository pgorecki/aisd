# -*- encoding: utf8 -*-

import unittest

from my_queue import Queue

import unittest

class TestQueue(unittest.TestCase):

    def test_nowa_kolejka_jest_pusta(self):
        q = Queue()
        self.assertTrue(q.is_empty())

    def test_po_dodaniu_elementu_kolejka_nie_jest_pusta(self):
        q = Queue()
        q.enqueue(123)
        self.assertFalse(q.is_empty())

    def test_po_dodaniu_i_usunieciu_elementu_kolejka_jest_pusta(self):
        q = Queue()
        q.enqueue(123)
        q.dequeue()
        self.assertTrue(q.is_empty())

    def test_po_dodaniu2_i_usunieciu1_elementu_kolejka_nie_jest_pusta(self):
        q = Queue()
        q.enqueue(123)
        q.enqueue(456)
        q.dequeue()
        self.assertFalse(q.is_empty())

    def test_pierwszy_wchodzi_pierwszy_wychodzi(self):
        q = Queue()
        q.enqueue(123)
        q.enqueue(456)
        self.assertEqual(q.dequeue(), 123)

    def test_drugi_wchodzi_drugi_wychodzi(self):
        q = Queue()
        q.enqueue(123)
        q.enqueue(456)
        q.dequeue()
        self.assertEqual(q.dequeue(), 456)


if __name__ == '__main__':
    unittest.main()

