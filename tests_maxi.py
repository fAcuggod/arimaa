import unittest
from arimaa_maxi import *

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

def tablero_3x2():
    return leer_tablero([
        'hc',
        'cc',
        'dc'
    ])

def tablero_8x2():
    return leer_tablero([
        'hc',
        'cc',
        'dc',
        'cc',
        'dc',
        'cc',
        'dc',
        'cc'        
    ])
#### Ejercicio 1

class test_tablero_bien_formado(unittest.TestCase):

    def test_8x8_lleno(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(tablero_bien_formado(t))

    def test_3x2(self):
        t = tablero_3x2()
        self.assertFalse(tablero_bien_formado(t))

    def test_8x2(self):
        t = tablero_8x2()
        self.assertFalse(tablero_bien_formado(t))

class test_juego_bien_formado(unittest.TestCase):

    def test_juego_ok(self):
        j = Juego(tablero_8x8_vacio(), DORADO, 0)
        self.assertTrue(juego_bien_formado(j))

    def test_juego_mal(self):
        j = Juego(tablero_3x2(), DORADO, 0)
        self.assertFalse(juego_bien_formado(j))

    def test_juego_horrendo(self):
        j = Juego(tablero_3x2(), DORADO, 5)
        self.assertFalse(juego_bien_formado(j))

    def test_juego_ok_plateado(self):
        j = Juego(tablero_8x8_vacio(), PLATEADO, 0)
        self.assertTrue(juego_bien_formado(j))

    def test_juego_mal_plateado(self):
        j = Juego(tablero_8x8_vacio(), PLATEADO, 4)
        self.assertFalse(juego_bien_formado(j))

    def test_juego_empezado(self):
        j = Juego(tablero_8x8_vacio(), DORADO, 3)
        self.assertTrue(juego_bien_formado(j))

if __name__ == '__main__':
    unittest.main(verbosity=2)