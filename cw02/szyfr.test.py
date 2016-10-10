# -*- encoding: utf8 -*-

from szyfr import gaderypoluki

import unittest

class TestGaderypoluki(unittest.TestCase):

    def test_pusty(self):
        # pusta wiadomość nie jest kodowana
        self.assertEqual(gaderypoluki(''), '')

    def test_ga(self):
        # sprawdzamy czy g zostaje zamienione na a
        # oraz czy a zostaje zamienione na g
        self.assertEqual(gaderypoluki('ga'), 'ag')

    def test_de(self):
        # sprawdzamy czy g zostaje zamienione na a
        # oraz czy a zostaje zamienione na g
        self.assertEqual(gaderypoluki('de'), 'ed')

    def test_ry(self):
        # sprawdzamy czy r zostaje zamienione na y
        # oraz czy y zostaje zamienione na r
        self.assertEqual(gaderypoluki('ry'), 'yr')

    def test_po(self):
        # sprawdzamy czy p zostaje zamienione na o
        # oraz czy o zostaje zamienione na p
        self.assertEqual(gaderypoluki('po'), 'op')

    def test_lu(self):
        # sprawdzamy czy l zostaje zamienione na u
        # oraz czy u zostaje zamienione na l
        self.assertEqual(gaderypoluki('lu'), 'ul')

    def test_ki(self):
        # sprawdzamy czy k zostaje zamienione na i
        # oraz czy i zostaje zamienione na k
        self.assertEqual(gaderypoluki('ki'), 'ik')

    def test_szyfr1(self):
        # sprawdzamy wiadomość składającą się z wyłącznie z podstawień
        self.assertEqual(gaderypoluki('galop'), 'agupo')

if __name__ == '__main__':
    unittest.main()