import unittest
from arimaa import *

class test_posicion_en_tablero(unittest.TestCase):

    def test_posicion_ok(self):
        self.assertTrue(posicion_en_tablero(Posicion(5, 3)))
    def test_borde_0_0(self):
        self.assertTrue(posicion_en_tablero(Posicion(0,0)))
    def test_borde_8_8(self):
        self.assertTrue(posicion_en_tablero(Posicion(8,8)))
    def test_afuera_fila(self):
        self.assertFalse(posicion_en_tablero(Posicion(-2,3)))
    def test_afuera_columna(self):
        self.assertFalse(posicion_en_tablero(Posicion(4,11)))
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
