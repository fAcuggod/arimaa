import unittest
from arimaa import *

# Las piezas se representan con las siguientes letras:
#   E : elefante
#   M : camello
#   H : caballo
#   D : perro
#   C : gato
#   R : ratón
# donde
#   mayúscula : dorado
#   minúscula : plateado

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

# EJERCICIO 1
class test_movimiento_bien_formado(unittest.TestCase):

    def test_movimiento_ok(self):
        self.assertTrue(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])))
    def test_arrastrar_mal(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(ARRASTRAR, Posicion(0, 1), [SUR])))
    def test_empujar_ok(self):
        self.assertTrue(movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(0, 1), [NORTE, SUR])))
    def test_arrastrar_ok(self):
        self.assertTrue(movimiento_bien_formado(Movimiento(ARRASTRAR, Posicion(0, 1), [NORTE, SUR])))
    def test_empujar_mal(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(0, 1), [OESTE])))
    def test_no_es_pos_origen(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(10, 0), [SUR])))

# EJERCICIO 2

class test_es_posicion_vecina_hacia(unittest.TestCase):

    def test_es_pos_vecina_norte(self):
        self.assertTrue(es_posicion_vecina_hacia(Posicion(1, 0), NORTE, Posicion(0, 0)))
    def test_no_es_pos_vecina_norte(self):
        self.assertFalse(es_posicion_vecina_hacia(Posicion(1, 0), NORTE, Posicion(1, 1)))
    def test_es_pos_vecina_sur(self):
        self.assertTrue(es_posicion_vecina_hacia(Posicion(1, 0), SUR, Posicion(2, 0)))
    def test_no_es_pos_vecina_sur(self):
        self.assertFalse(es_posicion_vecina_hacia(Posicion(1, 0), SUR, Posicion(0, 0)))
    def test_es_pos_vecina_este(self):
        self.assertTrue(es_posicion_vecina_hacia(Posicion(1, 1), ESTE, Posicion(1, 2)))
    def test_no_es_pos_vecina_este(self):
        self.assertFalse(es_posicion_vecina_hacia(Posicion(1, 1), ESTE, Posicion(0, 1)))
    def test_es_pos_vecina_oeste(self):
        self.assertTrue(es_posicion_vecina_hacia(Posicion(1, 1), OESTE, Posicion(1, 0)))
    def test_no_es_pos_vecina_oeste(self):
        self.assertFalse(es_posicion_vecina_hacia(Posicion(1, 1), OESTE, Posicion(1, 2)))

# EJERCICIO 3

class test_hay_pieza_enemiga_mas_fuerte_hacia(unittest.TestCase):

    def test_hay_pieza_enemiga_mas_fuerte_norte(self):
        t = leer_tablero([
              '-H------', #7
              '-r------', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_hacia(t, Posicion(6, 1), NORTE))
    def test_no_hay_pieza_enemiga_mas_fuerte_norte(self):
        t = leer_tablero([
              '-H------', #7
              '-r---r--', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_hacia(t, Posicion(6, 5), NORTE))
    def test_pieza_vecina_es_amiga(self):
        t = leer_tablero([
              '-H---m--', #7
              '-r---r--', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_hacia(t, Posicion(6, 5), NORTE))

class test_hay_pieza_enemiga_mas_fuerte_vecina(unittest.TestCase):

    def test_hay_pieza_enemiga_mas_fuerte_vecina(self):
        t = leer_tablero([
              'R-e--mRr', #7
              '------dE', #6
              'h--Rr-RR', #5
              'c--R-C--', #4
              '-rCHDrr-', #3
              '----rc--', #2
              'h-R-M-R-', #1
              'rr-D-dH-', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(3, 1)))
    def test_no_hay_pieza_enemiga_mas_fuerte_vecina(self):
        t = leer_tablero([
              '-H------', #7
              '-r---r--', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(6, 5)))

if __name__ == '__main__':
    unittest.main(verbosity=2)
