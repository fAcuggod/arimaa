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
    
def tablero_8x8_trampas():
    return leer_tablero([
              '--------', #7
              '--------', #6
              '--X--X--', #5
              '--------', #4
              '--------', #3
              '--X--X--', #2
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

class test_es_posicion_vecina_hacia(unittest.TestCase): # (test func. aux)

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

class test_hay_pieza_amiga_hacia(unittest.TestCase): # (test func. aux)

    def test_hay_pieza_amiga_hacia_ok(self):
        t = leer_tablero([
              'R-hRD-Rr', #7
              'M----d--', #6
              '-h-rrCR-', #5
              'R-rcE---', #4
              '--drRR--', #3
              '-HD-H--m', #2
              '--r-RCc-', #1
              're---r--', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_amiga_hacia(t, Posicion(3, 3), NORTE))
    def test_no_hay_pieza_amiga_hacia(self):
        t = leer_tablero([
              'R-hRD-Rr', #7
              'M----d--', #6
              '-h-rrCR-', #5
              'R-rcE---', #4
              '--drRR--', #3
              '-HD-H--m', #2
              '--r-RCc-', #1
              're---r--', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_amiga_hacia(t, Posicion(7, 2), ESTE))

class test_hay_pieza_amiga_vecina(unittest.TestCase):

    def test_hay_pieza_amiga_vecina(self):
        t = leer_tablero([
              'R-hRD-Rr', #7
              'M----d--', #6
              '-h-rrCR-', #5
              'R-rcE---', #4
              '--drRR--', #3
              '-HD-H--m', #2
              '--r-RCc-', #1
              're---r--', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_amiga_vecina(t, Posicion(4, 3)))
    def test_no_hay_pieza_amiga_vecina(self):
        t = leer_tablero([
              '--------', #7
              '--------', #6
              '---E----', #5
              '--MhR---', #4
              '---R----', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_amiga_vecina(t, Posicion(4, 3)))

class test_hay_pieza_enemiga_mas_debil_hacia(unittest.TestCase):

    def test_hay_pieza_enemiga_mas_debil_hacia(self):
        t = leer_tablero([
              '--Hdm---', #7
              'r--HhC--', #6
              'e---R-C-', #5
              'ME--d---', #4
              'h--RDcRr', #3
              'R-R-r--r', #2
              '-RRcrRD-', #1
              '--r---rr', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(1, 3), OESTE))
    def test_no_hay_pieza(self):
        t = leer_tablero([
              '--Hdm---', #7
              'r--HhC--', #6
              'e---R-C-', #5
              'ME--d---', #4
              'h--RDcRr', #3
              'R-R-r--r', #2
              '-RMcrRD-', #1
              '--r---rr', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(1, 3), NORTE))
    def test_pieza_vecina_es_amiga(self):
        t = leer_tablero([
              '--Hdm---', #7
              'r--HhC--', #6
              'e---R-C-', #5
              'ME--d---', #4
              'h--RDcRr', #3
              'R-R-r--r', #2
              '-RMcrRD-', #1
              '--r---rr', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(1, 3), ESTE))

class test_hay_pieza_enemiga_mas_fuerte_hacia(unittest.TestCase): # (test func. aux)

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
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_hacia(t, Posicion(6, 5), NORTE))

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
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(6, 5)))

class test_hay_pieza_congelada(unittest.TestCase):

    def test_hay_pieza_congelada(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_congelada(t, Posicion(6, 1)))
    def test_no_pieza_congelada(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_congelada(t, Posicion(2, 3)))

# EJERCICIO 4

class test_direccion_de_movimiento_habilitada(unittest.TestCase): # (test func. aux)
    
    def test_direccion_de_mov_conejo_dorado_ok(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-Ce-----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(direccion_de_movimiento_habilitada(t, Posicion(2, 3), NORTE))
    def test_direccion_de_mov_conejo_dorado_mal(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertFalse(direccion_de_movimiento_habilitada(t, Posicion(2, 3), SUR))
    def test_direccion_de_mov_conejo_plateado_ok(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(direccion_de_movimiento_habilitada(t, Posicion(5, 2), SUR))
    def test_direccion_de_mov_conejo_plateado_mal(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-h-c--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertFalse(direccion_de_movimiento_habilitada(t, Posicion(5, 2), NORTE))
    def test_direccion_de_mov_fig_distinta_a_conejo(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(direccion_de_movimiento_habilitada(t, Posicion(3, 3), NORTE))

class test_puede_mover_a_secas(unittest.TestCase): # (test func. aux)
    
    def test_puede_mover_a_secas_ok(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(puede_mover_a_secas(t, Posicion(2, 3), ESTE))
    def test_no_puede_mover_a_secas(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertFalse(puede_mover_a_secas(t, Posicion(2, 3), NORTE))

class test_puede_arrastrar(unittest.TestCase): # (test func. aux)

    def test_puede_arrastrar_ok(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc-rr-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertFalse(puede_arrastrar(t, Posicion(5, 6), OESTE, SUR))
    def test_puede_arrastral_mal(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertFalse(puede_arrastrar(t, Posicion(5, 2), OESTE, SUR))

class test_puede_empujar(unittest.TestCase): # (test func. aux)

    def test_puede_empujar_ok(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(puede_empujar(t, Posicion(6, 2), NORTE, ESTE))
    def test_no_puede_empujar(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hM---r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertFalse(puede_empujar(t, Posicion(5, 2), NORTE, ESTE))

class test_puede_realizar_accion(unittest.TestCase): # (test func. aux)
    
    def test_puede_realizar_accion_mover_a_secas_ok(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(puede_realizar_accion(t, Movimiento(MOVER_A_SECAS, Posicion(3, 3), [NORTE])))
    def test_no_puede_realizar_accion_mover_a_secas(self):
        t = leer_tablero([
                  '--d--H-D', #7
                  '-hMc--r-', #6
                  '--r--C-H', #5
                  '---r----', #4
                  '-CeD----', #3
                  '---R----', #2
                  '--------', #1
                  '--------', #0
                  #01234567
                ])
        self.assertFalse(puede_realizar_accion(t, Movimiento(MOVER_A_SECAS, Posicion(3, 3), [NORTE, SUR])))
    def test_puede_realizar_accion_arrastrar(self):
        t = leer_tablero([
                  '--d--H-D', #7
                  '-hMc--r-', #6
                  '--r--C-H', #5
                  '---r----', #4
                  '-CeD----', #3
                  '---R----', #2
                  '--------', #1
                  '--------', #0
                  #01234567
                ])
        self.assertTrue(puede_realizar_accion(t, Movimiento(ARRASTRAR, Posicion(3, 3), [ESTE, SUR])))
    def test_no_puede_realizar_accion_arrastrar(self):
        t = leer_tablero([
                  '--d--H-D', #7
                  '-hMc--r-', #6
                  '--r--C-H', #5
                  '---r----', #4
                  '-CeD----', #3
                  '---R----', #2
                  '--------', #1
                  '--------', #0
                  #01234567
                ])
        self.assertFalse(puede_realizar_accion(t, Movimiento(ARRASTRAR, Posicion(3, 3), [OESTE, SUR])))
    def test_puede_realizar_accion_empujar(self):
        t = leer_tablero([
                  '--d--H-D', #7
                  '-hMc--r-', #6
                  '--r--C-H', #5
                  '---r----', #4
                  '-CeD----', #3
                  '---R----', #2
                  '--------', #1
                  '--------', #0
                  #01234567
                ])
        self.assertTrue(puede_realizar_accion(t, Movimiento(EMPUJAR, Posicion(3, 3), [NORTE, NORTE])))
    def test_no_puede_realizar_accion_empujar(self):
        t = leer_tablero([
                  '--d--H-D', #7
                  '-hMc--r-', #6
                  '--r--C-H', #5
                  '---rR---', #4
                  '-CeD----', #3
                  '---R----', #2
                  '--------', #1
                  '--------', #0
                  #01234567
                ])
        self.assertFalse(puede_realizar_accion(t, Movimiento(EMPUJAR, Posicion(3, 3), [NORTE, ESTE])))

class test_puede_realizar_movimiento(unittest.TestCase):

    def test_puede_realizar_movimiento_ok(self):
        t = leer_tablero([
                  '--d--H-D', #7
                  '-hMc--r-', #6
                  '--r--C-H', #5
                  '--------', #4
                  '-CrD----', #3
                  '---R----', #2
                  '--------', #1
                  '--------', #0
                  #01234567
                ])
        self.assertTrue(puede_realizar_movimiento(Juego(t, DORADO, 1), Movimiento(MOVER_A_SECAS, Posicion(3, 3), [NORTE])))
    def test_no_puede_realizar_movimiento(self):
        t = leer_tablero([
                  '--d--H-D', #7
                  '-hMc--r-', #6
                  '--r--C-H', #5
                  '---d----', #4
                  '-CeR----', #3
                  '---m----', #2
                  '--------', #1
                  '--------', #0
                  #01234567
                ])
        self.assertFalse(puede_realizar_movimiento(Juego(t, DORADO, 3), Movimiento(MOVER_A_SECAS, Posicion(3, 3), [NORTE])))

# EJERCICIO 5

class tes_tableros_coinciden_en_la_posicion(unittest.TestCase): # (test func. aux)

    def test_tableros_coinciden_en_la_posicion_ok(self):
        t1 = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '---h----', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        t2 = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '---h----', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(tableros_coinciden_en_la_posicion(t1, t2, Posicion(4, 3)))
    def test_tableros_no_coinciden_en_la_posicion(self):
        t1 = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '---h----', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        t2 = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '---r----', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertFalse(tableros_coinciden_en_la_posicion(t1, t2, Posicion(4, 3)))

class test_tableros_coinciden_salvo_en_la_posicion(unittest.TestCase): # (test func. aux)
    
    def test_tableros_coinciden_salvo_en_la_posicion_ok(self):
        t1 = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '---rH---', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        t2 = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '---rC---', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(tableros_coinciden_salvo_en_la_posicion(t1, t2, Posicion(4, 4)))
    def test_tableros_coinciden(self):
        t1 = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '---rC---', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        t2 = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '---rC---', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(tableros_coinciden_salvo_en_la_posicion(t1, t2, Posicion(4, 4)))
    def test_tableros_no_coinciden_salvo_en_la_posicion(self):
        t1 = leer_tablero([
              '--------', #7
              '-----c--', #6
              '--------', #5
              '---r----', #4
              '------H-', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        t2 = leer_tablero([
              '--------', #7
              '-r---d--', #6
              '--------', #5
              '---C----', #4
              '--------', #3
              '--------', #2
              '---M----', #1
              '------c-', #0
              #01234567
            ])
        self.assertFalse(tableros_coinciden_salvo_en_la_posicion(t1, t2, Posicion(4, 3)))

class test_es_tablero_sacando_pieza(unittest.TestCase): # (test func. aux)

    def test_es_tablero_sacando_pieza_ok(self):
        t1 = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '---H----', #4
              '---C----', #3
              '--r-----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        t2 = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '---H----', #4
              '---C----', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(es_tablero_sacando_pieza(t1, t2, Posicion(2, 2)))
    def test_no_es_tablero_sacando_pieza(self):
        t1 = leer_tablero([
              '--------', #7
              '--r-----', #6
              '--------', #5
              '--------', #4
              '---H----', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        t2 = leer_tablero([
              '--------', #7
              '--r-----', #6
              '--------', #5
              '--------', #4
              '---H----', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertFalse(es_tablero_sacando_pieza(t1, t2, Posicion(6, 2)))
        
class test_es_tablero_despues_de_activar_trampa(unittest.TestCase): # (test func. aux)

    def test_es_tablero_despues_de_activar_trampa_ok(self):
        t1 = leer_tablero([
              '--------', #7
              '--r-----', #6
              '--------', #5
              '--------', #4
              '---H----', #3
              '--r-----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        t2 = leer_tablero([
              '--------', #7
              '--r-----', #6
              '--------', #5
              '--------', #4
              '---H----', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(es_tablero_despues_de_activar_trampa(t1, t2, Posicion(2, 2)))
    def test_no_es_tablero_despues_de_activar_trampa(self):
        t1 = leer_tablero([
              '--------', #7
              '--M-----', #6
              '--c-----', #5
              '--------', #4
              '---H----', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        t2 = leer_tablero([
              '--------', #7
              '--M-----', #6
              '--c-----', #5
              '--------', #4
              '---H----', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertFalse(es_tablero_despues_de_activar_trampa(t1, t2, Posicion(5, 2)))
    def test_es_tablero_despues_de_activar_trampa_pieza_liberada(self):
        t1 = leer_tablero([
              '--------', #7
              '--d-----', #6
              '--r-----', #5
              '--------', #4
              '---H----', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        t2 = leer_tablero([
              '--------', #7
              '--d-----', #6
              '---r----', #5
              '--------', #4
              '---H----', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertFalse(es_tablero_despues_de_activar_trampa(t1, t2, Posicion(5, 2)))
    def test_es_tablero_despues_de_activar_trampa_tableros_iguales(self):
        t1 = leer_tablero([
              '--------', #7
              '--d-----', #6
              '--r-----', #5
              '--------', #4
              '---H----', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        t2 = leer_tablero([
              '--------', #7
              '--d-----', #6
              '--r-----', #5
              '--------', #4
              '---H----', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(es_tablero_despues_de_activar_trampa(t1, t2, Posicion(5, 2)))

class test_tablero_post_activar_trampa(unittest.TestCase): # (test func. aux)

    def test_tablero_post_activar_trampa_ok(self):
        t1 = leer_tablero([
              '--------', #7
              '--d-----', #6
              '--r-----', #5
              '--------', #4
              '--------', #3
              '--rC----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        t2 = leer_tablero([
              '--------', #7
              '--d-----', #6
              '--r-----', #5
              '--------', #4
              '--------', #3
              '---C----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertEqual(tablero_post_activar_trampa(t1, Posicion(2, 2)), t2)
    def test_tablero_post_activar_trampa_amigo_vecino(self):
        t1 = leer_tablero([
              '--------', #7
              '--E-----', #6
              '-----ch-', #5
              '--------', #4
              '--------', #3
              '---C----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        t2 = leer_tablero([
              '--------', #7
              '--E-----', #6
              '-----ch-', #5
              '--------', #4
              '--------', #3
              '---C----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertEqual(tablero_post_activar_trampa(t1, Posicion(5, 5)), t2)

class test_es_tablero_despues_de_activar_todas_las_trampas(unittest.TestCase): # (test func. aux)

    def test_es_tablero_despues_de_activar_todas_las_trampas_ok(self):
        t1 = leer_tablero([
              '--------', #7
              '--E-----', #6
              '--r--ch-', #5
              '--------', #4
              '--------', #3
              '--Re-r--', #2
              '-----H--', #1
              '--------', #0
              #01234567
            ])
        t2 = leer_tablero([
              '--------', #7
              '--E-----', #6
              '-----ch-', #5
              '--------', #4
              '--------', #3
              '---e----', #2
              '-----H--', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(es_tablero_despues_de_activar_todas_las_trampas(t1, t2))

class test_activar_trampas(unittest.TestCase):

    def test_activar_trampas_ok(self):
        t0 = leer_tablero([
                   '-eRD--rd', #7
                   '--------', #6
                   'H-r--E--', #5
                   '-H--r-Cr', #4
                   'R-------', #3
                   'R-H--m--', #2
                   'R-------', #1
                   'c-D---R-', #0
                   #01234567
                 ])
        t1 = leer_tablero([
                   '-eRD--rd', #7
                   '--------', #6
                   'H-------', #5
                   '-H--r-Cr', #4
                   'R-------', #3
                   'R-------', #2
                   'R-------', #1
                   'c-D---R-', #0
                   #01234567
                 ])
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0, t1)
        self.assertEqual(t2, t1)
    def test_activar_trampas_ok2(self):
        t = leer_tablero([
              '--------', #7
              '--------', #6
              '-Cr--ch-', #5
              '--------', #4
              '--------', #3
              '--Ce-d--', #2
              '-----H--', #1
              '--------', #0
              #01234567
            ])
        t1 = leer_tablero([
              '--------', #7
              '--------', #6
              '-C---ch-', #5
              '--------', #4
              '--------', #3
              '---e----', #2
              '-----H--', #1
              '--------', #0
              #01234567
            ])
        self.assertEqual(activar_trampas(t), t1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
