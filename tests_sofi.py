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

#### Ejercicio 2

class test_posicion_vecina_hacia(unittest.TestCase):

    def test_vecina_al_norte(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(0, 0), NORTE), Posicion(1, 0))
    def test_vecina_al_sur(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(1,0), SUR), Posicion(0,0))
    def test_vecina_al_este(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(0, 0), ESTE), Posicion(0, 1))
    def test_vecina_al_oeste(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(0,1), OESTE), Posicion(0,0))

class test_son_posiciones_vecinas(unittest.TestCase):

    def test_vecinas(self):
        self.assertTrue(son_posiciones_vecinas(Posicion(0, 0), Posicion(1, 0)))

class test_casilla_en_posicion(unittest.TestCase):

    def test_casilla_en_posicion(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(casilla_en_posicion(t, Posicion(0, 0)), Pieza(CABALLO, DORADO))

    def test_casilla_fuerapos(self):
        t = tablero_8x8_vacio()
        self.assertNotEqual(casilla_en_posicion(t, Posicion(0, 0)), Pieza(CABALLO, DORADO))

    def test_casilla_mal(self):
        t = tablero_3x2()
        with self.assertRaises(AssertionError):
            casilla_en_posicion(t, Posicion(0, 0)), Pieza(CABALLO, DORADO)

    def test_casilla_color(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertNotEqual(casilla_en_posicion(t, Posicion(0,0)), Pieza(CABALLO, PLATEADO))


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
