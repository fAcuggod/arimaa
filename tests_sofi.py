import unittest
from arimaa import *

def tablero_8x8_vacio():
    return leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])

def tablero_8x8_inicial_ejemplo():
    return leer_tablero([
              'hcdmedch', #7
              'rrrrrrrr', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              'RRRRRRRR', #1
              'HCDMEDCH', #0
              #01234567
            ])


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

class test_posicion_vecina_hacia(unittest.TestCase):

    def test_vecina_al_norte(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(0, 0), NORTE), Posicion(1, 0))
    def test_vecina_al_sur(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(1,0), SUR), Posicion(0,0))
    def test_vecina_al_este(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(0, 0), ESTE), Posicion(0, 1))
    def test_vecina_al_oeste(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(0,1), OESTE), Posicion(0,0))

class test_hay_casilla_vacia(unittest.TestCase):

    def test_casilla_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_casilla_vacia(t, Posicion(2, 1)))
    def test_casilla_figura(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_casilla_vacia(t, Posicion(0, 4)))
    def test_todo_vacio(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_casilla_vacia(t, Posicion(7,4)))

class test_hay_pieza_de_color(unittest.TestCase):

    def test_hay_pieza_de_color_ok(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_pieza_de_color(t, Posicion(1, 4), DORADO))

if __name__ == '__main__':
    unittest.main(verbosity=2)
