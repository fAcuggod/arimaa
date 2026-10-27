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

#### Auxiliares

class test_hay_pieza(unittest.TestCase):

    def test_hay_pieza(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_pieza(t, Posicion(0, 0)))
    
    def test_no_hay_pieza(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_pieza(t, Posicion(4,4)))

class test_es_enemigo(unittest.TestCase):

    def test_es_enemigo(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(es_enemigo(t, Posicion(0,0), Posicion(7,7)))

    def test_es_aliado(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(es_enemigo(t, Posicion(0,0), Posicion(0,1)))

    def test_es_enemigo_reves(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(es_enemigo(t, Posicion(7,7), Posicion(0,0)))

    def test_es_aliado_reves(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(es_enemigo(t, Posicion(7,7), Posicion(7,6)))

    def test_es_mismo(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(es_enemigo(t, Posicion(0,0), Posicion(0,0)))

class test_direccion_de_movimiento_habilitada(unittest.TestCase): 
    
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
   
class test_puede_mover_a_secas(unittest.TestCase): 
    
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

class test_puede_arrastrar(unittest.TestCase): 

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

class test_puede_empujar(unittest.TestCase): 

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

class test_puede_realizar_accion(unittest.TestCase): 

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

class test_tableros_coinciden_en_la_posicion(unittest.TestCase):

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

class test_tableros_coinciden_salvo_en_la_posicion(unittest.TestCase):

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

class test_crear_tablero_vacio(unittest.TestCase):

    def test_es_tablero_bien_hecho(self):
        t1 = crear_tablero_vacio()
        self.assertTrue(len(t1) == ALTO and len(t1[0]) == ANCHO)

class test_es_tablero_sacando_pieza(unittest.TestCase): 

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

class test_es_tablero_despues_de_activar_trampa(unittest.TestCase):

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

class test_es_tablero_despues_de_activar_todas_las_trampas(unittest.TestCase):

    def test_es_tablero_despues_de_activar_todas_las_trampas_ok(self):
        t1 = leer_tablero([
              '--------', #7
              '--E-----', #6
              '--r--cH-', #5
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
              '------h-', #5
              '--------', #4
              '--------', #3
              '---e----', #2
              '-----H--', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(es_tablero_despues_de_activar_todas_las_trampas(t1, t2))

class test_tablero_post_activar_trampa(unittest.TestCase): 

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

class test_copiar_tableros(unittest.TestCase):

    def test_copiar_tablero(self):
        t1: Tablero = tablero_8x8_inicial_ejemplo()
        t2: Tablero = copiar_tablero(t1)
        self.assertEqual(t1, t2)

class test_copiar_pieza(unittest.TestCase):
    def test_copiar_pieza(self):
        t: Tablero = tablero_8x8_inicial_ejemplo()
        p: Pieza = copiar_pieza(t, Posicion(1,1))
        self.assertEqual(p, t[1][1])

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
    
    def test_posicion_miti(self):
        self.assertFalse(posicion_en_tablero(Posicion(5,9)))
    
    def test_posicion_mal(self):
        self.assertFalse(posicion_en_tablero(Posicion(10,20)))

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

    def test_hay_pieza_de_color_no(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_pieza_de_color(t, Posicion(1, 4), PLATEADO))

#### Ejercicio 3

class test_hay_casilla_vacia_hacia(unittest.TestCase):

    def test_hay_casilla_vacia_hacia(self):
        t = leer_tablero([
              '-r----rr', #7
              '-mrh----', #6
              '-r---r--', #5
              'd-EH---c', #4
              '-M--hD-d', #3
              '-R-e----', #2
              '---H-R-C', #1
              'R-R---RR', #0
              #01234567
            ])
        self.assertTrue(hay_casilla_vacia_hacia(t, Posicion(0, 0), NORTE))

    def test_no_hay_casilla_vacia_hacia(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(0,0), ESTE))

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
    
    def test_hay_pieza_aliada(self):
        t = leer_tablero([
              '-H------', #7
              '-r---r--', #6
              '-----c--', #5
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

#### Ejercicio 4

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

#### Ejercicio 5

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

#### Ejercicio 6
class test_realizar_movimiento(unittest.TestCase):

    def test_no_puede_realizar_movimiento(self):
        t0 = tablero_8x8_inicial_ejemplo()
        j0 = Juego(t0, PLATEADO, 0)
        mInvalido = Movimiento(MOVER_A_SECAS, Posicion(1,0), [NORTE])
        self.assertFalse(puede_realizar_movimiento(j0, mInvalido))
        self.assertEqual(realizar_movimiento(j0, mInvalido), j0)

    def test_mover_a_secas(self):
        t0 = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '--------', #5
               '---m----', #4
               '--------', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        tN = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '---m----', #5
               '--------', #4
               '--------', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        j0 = Juego(t0, PLATEADO, 0) 
        jN = Juego(tN, PLATEADO, 1) 
        mN = Movimiento(MOVER_A_SECAS, Posicion(4, 3), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)

    def test_arrastrar(self):
        t0 = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '--------', #5
               '---mR---', #4
               '--------', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        tN = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '---m----', #5
               '---R----', #4
               '--------', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        j0 = Juego(t0, PLATEADO, 0) 
        jN = Juego(tN, PLATEADO, 2) 
        mN = Movimiento(ARRASTRAR, Posicion(4, 3), [NORTE, OESTE])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)

    def test_empujar(self):
        t0 = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '--------', #5
               '---mE---', #4
               '--------', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        tN = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '--------', #5
               '---E----', #4
               '---m----', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        j0 = Juego(t0, DORADO, 0) 
        jN = Juego(tN, DORADO, 2) 
        mN = Movimiento(EMPUJAR, Posicion(4, 4), [OESTE, SUR])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)

    def test_empujar_cambio_de_turno(self):
        t0 = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '--------', #5
               '--Em----', #4
               '--------', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        tN = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '--------', #5
               '---E----', #4
               '---m----', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        j0 = Juego(t0, DORADO, 2) 
        jN = Juego(tN, PLATEADO, 0) 
        mN = Movimiento(EMPUJAR, Posicion(4, 2), [ESTE, SUR])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)


#### Ejercicio 7

"""
class test_ganador_del_juego(unittest.TestCase):

    def test_promueve_conejo_dorado_turno_del_oponente(self):
        t = leer_tablero([
              'rr----Rr', #7
              'c-----me', #6
              '---Ed-R-', #5
              '-M---R--', #4
              '---R----', #3
              '-rrrr---', #2
              '-H---DCC', #1
              'R-----RR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        self.assertTrue(hay_ganador_determinado(j))
        self.assertEqual(ganador_del_juego(j), DORADO)

"""

if __name__ == '__main__':
    unittest.main(verbosity=2)