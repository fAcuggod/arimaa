from definiciones import *

#### Algunas funciones ya dadas

def son_posiciones_vecinas(pos1 : Posicion, pos2 : Posicion) -> bool: # pragma: no cover
    return (pos1.fila == pos2.fila and abs(pos1.columna - pos2.columna) == 1) \
        or (pos1.columna == pos2.columna and abs(pos1.fila - pos2.fila) == 1)

def direccion_desde_hasta(pos1 : Posicion, pos2 : Posicion) -> Direccion: # pragma: no cover
    assert son_posiciones_vecinas(pos1, pos2)
    if pos1.fila < pos2.fila:
       return NORTE
    elif pos1.fila > pos2.fila:
       return SUR
    elif pos1.columna < pos2.columna:
       return ESTE
    else:
       return OESTE

def pasar_turno(j : Juego) -> Juego: # pragma: no cover
    return Juego(j.tablero, oponente(j.turno), 0)

#### Ejercicio 1

def tablero_bien_formado(t : Tablero) -> bool:
    if (len(t) == ALTO):
        for fila in t:
            if (len(fila) != ANCHO):
                return False
        return True
    else: 
        return False

def posicion_en_tablero(pos : Posicion) -> bool:
    res:bool = False
    if 0 <= pos[0] <= ALTO and 0 <= pos[1] <= ANCHO:
        res = True
    return res

def movimiento_bien_formado(m : Movimiento) -> bool:
    # raise Exception("No implementado")
    res: bool = False
    if posicion_en_tablero(m.origen):
        if m.accion == MOVER_A_SECAS and len(m.pasos) == 1:
            res = True
        elif m.accion == ARRASTRAR and len(m.pasos) == 2:
            res = True
        elif m.accion == EMPUJAR and len(m.pasos) == 2:
            res = True
    return res

def juego_bien_formado(j : Juego) -> bool:
    c1:bool = (tablero_bien_formado(j.tablero))
    c2:bool = (0 <= j.pasos_consumidos)
    c3:bool = (j.pasos_consumidos < MAX_PASOS)
    return c1 and c2 and c3

#### Ejercicio 2

def posicion_vecina_hacia(pos : Posicion, d : Direccion) -> Posicion:
    if d == NORTE:
        res:Posicion = Posicion(pos.fila + 1,pos.columna)
    elif d == SUR:
        res:Posicion = Posicion(pos.fila - 1, pos.columna)
    elif d == ESTE:
        res:Posicion = Posicion(pos.fila, pos.columna + 1)
    else:
        res:Posicion = Posicion(pos.fila, pos.columna - 1)
    return res

def es_posicion_vecina_hacia(pos: Posicion, d: Direccion, pos2: Posicion) -> bool:
    # (func. aux) decide si dos posiciones pos y pos2 son vecinas en dirección d
    if d == NORTE:
        return pos2.fila == (pos.fila + 1) and pos2.columna == pos.columna
    elif d == SUR:
        return pos2.fila == (pos.fila - 1) and pos2.columna == pos.columna
    elif d == ESTE:
        return pos2.fila == pos.fila and pos2.columna == (pos.columna + 1)
    else: #d == OESTE:
        return pos2.fila == pos.fila and pos2.columna == (pos.columna - 1)

def casilla_en_posicion(t : Tablero, p : Posicion) -> Casilla:
    assert(tablero_bien_formado(t) and posicion_en_tablero(p))
    return t[p.fila][p.columna]

def hay_casilla_vacia(t : Tablero, pos : Posicion) -> bool:
    assert(tablero_bien_formado(t) and posicion_en_tablero(pos))
    return t[pos.fila][pos.columna] == VACIA

LISTA_DE_TODAS_LAS_FIGURAS = [ELEFANTE, CAMELLO, CABALLO, PERRO, GATO, CONEJO]
LISTA_DE_LOS_COLORES = [DORADO, PLATEADO]

def hay_pieza_de_color(t : Tablero, pos : Posicion, col : Color) -> bool:
    assert(tablero_bien_formado(t) and posicion_en_tablero(pos))
    es_figura:bool = False
    es_color:bool = False
    if hay_casilla_vacia(t, pos):
        return False
    for f in LISTA_DE_TODAS_LAS_FIGURAS:
#        print(t[pos.fila][pos.columna]) # Pieza(figura=CONEJO, color=DORADO)
        if t[pos.fila][pos.columna].figura == f:
            es_figura = True
    if t[pos.fila][pos.columna].color == col:
        es_color = True
    return es_color and es_figura

def hay_figura_de_color(t:Tablero, pos: Posicion, f: Figura, col: Color): 
    #funcion auxiliar que se fija si está una figura especifica
    res:bool = False
    if hay_pieza_de_color(t, pos, col):
        res = t[pos.fila][pos.columna].figura == f
    return res

#### Ejercicio 3

def hay_casilla_vacia_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    assert(tablero_bien_formado(t) and posicion_en_tablero(pos))
    res:bool = False
    pos_vecina:Posicion = posicion_vecina_hacia(pos, d)
    if hay_casilla_vacia(t,pos_vecina):
        res = True
    return res

def hay_pieza_amiga_hacia(t: Tablero, pos: Posicion, d: Direccion) -> bool:
    # (func. aux) decide si la pieza en dirección d respecto a la posición pos es amiga
    res:bool = False #si no hay pieza en t[pos.fila][pos.columna] devuelve falso
    if hay_pieza(t, pos): #si hay pieza, busca la amiga en funcion de su color y la direccion donde la piden
        col_pieza: Color = t[pos.fila][pos.columna].color
        pos_amiga: Posicion = posicion_vecina_hacia(pos, d)
        res = hay_pieza_de_color(t, pos_amiga, col_pieza)
    return res

def hay_pieza_amiga_vecina(t : Tablero, pos : Posicion) -> bool:
    assert(tablero_bien_formado(t) and posicion_en_tablero(pos))
    for d in Direccion:
        if hay_pieza_amiga_hacia(t, pos, d):
            return True
    return False

def hay_pieza(t : Tablero, pos : Posicion) -> bool:
    # (func. aux) decide si existe una pieza en el tablero t posición pos
    hay_color:bool = False
    hay_figura:bool = False   
    if hay_casilla_vacia(t, pos):
        return hay_color and hay_figura
    for f in LISTA_DE_TODAS_LAS_FIGURAS:
        if t[pos.fila][pos.columna].figura == f:
            hay_figura = True
    for col in LISTA_DE_LOS_COLORES:
        if t[pos.fila][pos.columna].color == col:
            hay_color = True
    return hay_color and hay_figura

def hay_pieza_enemiga_mas_debil_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    assert(tablero_bien_formado(t) and posicion_en_tablero(pos))
    assert hay_pieza(t, pos)
    col_propio: Color = t[pos.fila][pos.columna].color
    fig_propia: Figura = t[pos.fila][pos.columna].figura
    pos_vecina = posicion_vecina_hacia(pos, d)
    if posicion_en_tablero(pos_vecina) and hay_pieza(t, pos_vecina):
        if col_propio == t[pos_vecina.fila][pos_vecina.columna].color:
            return False
        return fuerza(fig_propia) > fuerza(t[pos_vecina.fila][pos_vecina.columna].figura)
    return False

def hay_pieza_enemiga_mas_fuerte_hacia(t: Tablero, pos: Posicion, d: Direccion) -> bool:
    # (func. aux) decide si existe una fig_enemiga más fuerte en la dirección d de la posición pos
    assert(tablero_bien_formado(t) and posicion_en_tablero(pos))
    assert hay_pieza(t, pos)
    col_propio: Color = t[pos.fila][pos.columna].color
    fig_propia: Figura = t[pos.fila][pos.columna].figura
    pos_vecina = posicion_vecina_hacia(pos, d)
    if posicion_en_tablero(pos_vecina) and hay_pieza(t, pos_vecina):
        if col_propio == t[pos_vecina.fila][pos_vecina.columna].color:
            return False
        return fuerza(fig_propia) < fuerza(t[pos_vecina.fila][pos_vecina.columna].figura)
    return False

def hay_pieza_enemiga_mas_fuerte_vecina(t : Tablero, pos : Posicion) -> bool:
    assert(tablero_bien_formado(t) and posicion_en_tablero(pos))
    assert hay_pieza(t, pos)
    for d in Direccion:
        if hay_pieza_enemiga_mas_fuerte_hacia(t, pos, d):
            return True
    return False

def hay_pieza_congelada(t : Tablero, pos : Posicion) -> bool:
    assert(tablero_bien_formado(t) and posicion_en_tablero(pos))
    return hay_pieza(t, pos) and hay_pieza_enemiga_mas_fuerte_vecina(t, pos) and not hay_pieza_amiga_vecina(t, pos)

#### Ejercicio 4

def direccion_de_movimiento_habilitada(t: Tablero, pos: Posicion, d: Direccion) -> bool:
    # (func. aux) decide si de haber pieza en la posición pos del tablero t, la figura de la pieza tiene habilitado moverse en la dirección d
    assert hay_pieza(t, pos)
    fig_pieza: Figura = t[pos.fila][pos.columna].figura
    col_pieza: Color  = t[pos.fila][pos.columna].color
    if fig_pieza == CONEJO and col_pieza == DORADO:
        return d != SUR
    elif fig_pieza == CONEJO and col_pieza == PLATEADO:
        return d != NORTE
    else:
        return True

def puede_mover_a_secas(t: Tablero, pos: Posicion, d: Direccion) -> bool:
    # (func. aux) decide si dada la posición pos del tablero t existe casilla vacía en la dirección d
    return hay_casilla_vacia_hacia(t, pos, d)

def puede_arrastrar(t: Tablero, pos: Posicion, d: Direccion, d_arrastre: Direccion) -> bool:
    # (func. aux) decide si se puede arrastrar la pieza ubicada en la dirección opuesta(d_arrastre) hacia la posición pos
    return hay_casilla_vacia_hacia(t, pos, d) and hay_pieza_enemiga_mas_debil_hacia(t, pos, opuesta(d_arrastre))

def puede_empujar(t: Tablero, pos: Posicion, d: Direccion, d_empuje: Direccion) -> bool:
    # (func. aux) decide si se puede empujar la pieza ubicada en pos_enemiga hacia la dirección d_empuje
    if not hay_pieza_enemiga_mas_debil_hacia(t, pos, d):
        return False
    pos_enemiga: Posicion = posicion_vecina_hacia(pos, d)
    return hay_casilla_vacia_hacia(t, pos_enemiga, d_empuje)

def puede_realizar_accion(t: Tablero, m: Movimiento) -> bool:
    # (func. aux) decide si se puede realizar el movimiento m en el tablero t
    if m.accion == MOVER_A_SECAS:
        return puede_mover_a_secas(t, m.origen, m.pasos[0])
    elif m.accion == ARRASTRAR:
        return puede_arrastrar(t, m.origen, m.pasos[0], m.pasos[1])
    else:
        # única acción restante es PULL
        return puede_empujar(t, m.origen, m.pasos[0], m.pasos[1])

def puede_realizar_movimiento(j : Juego, m : Movimiento) -> bool:
    assert(juego_bien_formado(j) and movimiento_bien_formado(m))
    c1:bool = hay_pieza_de_color(j.tablero, m.origen, j.turno)
    c2:bool = not hay_pieza_congelada(j.tablero, m.origen)
    c3:bool = direccion_de_movimiento_habilitada(j.tablero, m.origen, m.pasos[0])
    c4:bool = (j.pasos_consumidos + len(m.pasos) <= MAX_PASOS)
    c5:bool = puede_realizar_accion(j.tablero, m)
    return c1 and c2 and c3 and c4 and c5

#### Ejercicio 5

def tableros_coinciden_en_la_posicion(t1: Tablero, t2: Tablero, pos: Posicion) -> bool:
    # (func. aux) decide si la posición pos es la misma para t1 y t2
    return t1[pos.fila][pos.columna] == t2[pos.fila][pos.columna]

def tableros_coinciden_salvo_en_la_posicion(t1: Tablero, t2: Tablero, pos: Posicion) -> bool:
    # (func. aux) decide si dos tableros coinciden salvo en la posición pos
    for pos_fila in range(ALTO):
        for pos_columna in range(ANCHO):
            pos_prima: Posicion = Posicion(pos_fila, pos_columna)
            if pos_prima != pos and not tableros_coinciden_en_la_posicion(t1, t2, pos_prima):
                return False
    return True

def es_tablero_sacando_pieza(t0: Tablero, t1: Tablero, pos: Posicion) -> bool:
    # (func. aux) decide si t1 es tablero luego de sacar la pieza en la posición pos del tablero t0
    return tableros_coinciden_salvo_en_la_posicion(t0, t1, pos) and hay_casilla_vacia(t1, pos)

def es_tablero_despues_de_activar_trampa(t0: Tablero, t1: Tablero, postrampa: Posicion) -> bool:
    # (func. aux) decide si el tablero t1 es tablero luego de activar trampa en la posición postrampa del tablero t0
    if hay_pieza_amiga_vecina(t0, postrampa) and t1 != t0:
        return False
    elif hay_pieza_amiga_vecina(t0, postrampa):
        return True
    else:
        pass
    return es_tablero_sacando_pieza(t0, t1, postrampa)

def tablero_post_activar_trampa(t: Tablero, postrampa: Posicion) -> Tablero:
    # (func. aux) dado un tablero t, devuelve el tablero luego de activar la trampa en la posicion postrampa
    assert tablero_bien_formado(t)
    res: Tablero = leer_tablero([
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
    for pos_fila in range(ALTO):
        for pos_columna in range(ANCHO):
            pos_prima: Posicion = Posicion(pos_fila, pos_columna)
            if pos_prima == postrampa and hay_pieza(t, pos_prima) and not hay_pieza_amiga_vecina(t, pos_prima):
                res[pos_prima.fila][pos_prima.columna] = VACIA
            else:
                res[pos_prima.fila][pos_prima.columna] = t[pos_prima.fila][pos_prima.columna]
    return res

def es_tablero_despues_de_activar_todas_las_trampas(t0: Tablero, t1: Tablero) -> bool:
    # (func. aux) decide si t1 es tablero luego de que se activen las trampas en el tablero t0
    t_int_1: Tablero = tablero_post_activar_trampa(t0, POSICIONES_TRAMPA[0])
    t_int_2: Tablero = tablero_post_activar_trampa(t_int_1, POSICIONES_TRAMPA[1])
    t_int_3: Tablero = tablero_post_activar_trampa(t_int_2, POSICIONES_TRAMPA[2])
    c1:bool = es_tablero_despues_de_activar_trampa(t0, t_int_1, POSICIONES_TRAMPA[0])
    c2:bool = es_tablero_despues_de_activar_trampa(t_int_1, t_int_2, POSICIONES_TRAMPA[1])
    c3:bool = es_tablero_despues_de_activar_trampa(t_int_2, t_int_3, POSICIONES_TRAMPA[2])
    c4:bool = es_tablero_despues_de_activar_trampa(t_int_3, t1, POSICIONES_TRAMPA[3])
    return c1 and c2 and c3 and c4

def activar_trampas(t : Tablero) -> Tablero:
    assert tablero_bien_formado(t)
    res: Tablero = t
    for trampa in POSICIONES_TRAMPA:
        res = tablero_post_activar_trampa(res, trampa)
    return res

#### Ejercicio 6

def sacar_pieza(t: Tablero, pos : Posicion) -> Tablero:
    # (func. aux) elimina la pieza que esté en posición pos del tablero t
    res: Tablero = leer_tablero([
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
    for fila in range (ALTO):
        for columna in range (ANCHO):
            res[fila][columna] = t[fila][columna]
    res[pos.fila][pos.columna] = VACIA
    return res

def es_tablero_poniendo_pieza(t0: Tablero, t1:Tablero, pos:Posicion, f:Figura, col:Color) -> bool:
    # (func. aux) decide si poniendo la pieza de figura f y color col en t0 se obtiene un tablero igual a t1
    c1:bool = tableros_coinciden_salvo_en_la_posicion(t0, t1, pos)
    c2:bool = hay_figura_de_color(t1, pos, f, col)
    return c1 and c2

def es_tablero_trasladando_pieza(t0 : Tablero, t1: Tablero, pos_origen : Posicion, pos_destino: Posicion) -> bool:
    # (func. aux) decide t1 es el resultado de trasladar la pieza de t0.pos_origen a t1.pos_destino
    f:Figura = t0[pos_origen.fila][pos_origen.columna].figura
    col:Color = t0[pos_origen.fila][pos_origen.columna].color
    hay_figura:bool = hay_figura_de_color(t0, pos_origen, f, col)
    t_intermedio: Tablero = sacar_pieza(t0, pos_origen)
    c1:bool = es_tablero_sacando_pieza(t0, t_intermedio, pos_origen)
    c2:bool = es_tablero_poniendo_pieza(t_intermedio, t1, pos_destino, f, col)
    return hay_figura and c1 and c2

def tablero_post_mover_a_secas(t0 : Tablero, t1: Tablero, pos: Posicion, d : Direccion) -> bool:
    # (func. aux) que decide si t1 es el tablero despues de mover a secas una pieza en posición pos de tablero t0 a dirección d
    pos_destino:Posicion = posicion_vecina_hacia(pos, d)
    t_intermedio:Tablero = tablero_trasladando_pieza(t0, pos, pos_destino)
    c1:bool = es_posicion_vecina_hacia(pos, d, pos_destino)
    c2:bool = es_tablero_trasladando_pieza(t0, t_intermedio, pos, pos_destino)
    c3:bool = es_tablero_despues_de_activar_todas_las_trampas(t_intermedio, t1)
    return c1 and c2 and c3

def tablero_trasladando_pieza(t:Tablero, pos_origen:Posicion, pos_destino:Posicion) -> Tablero:
    # (func. aux) que mueve la pieza que estaba en pos_origen de t y la mueve a pos_destino
    assert tablero_bien_formado(t)
    res:Tablero = leer_tablero([
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
    for pos_fila in range (ALTO):
        for pos_columna in range (ANCHO):
            pos_prima: Posicion = Posicion(pos_fila, pos_columna)
            res[pos_prima.fila][pos_prima.columna] = t[pos_prima.fila][pos_prima.columna]
    res = sacar_pieza(res, pos_origen)
    pieza_a_mover:Pieza = t[pos_origen.fila][pos_origen.columna]
    res[pos_destino.fila][pos_destino.columna] = pieza_a_mover
    assert es_tablero_trasladando_pieza(t, res, pos_origen, pos_destino)
    return res
    
def tablero_post_arrastrar(t0:Tablero, t1:Tablero, pos:Posicion, d:Direccion, d_arrastre:Direccion) -> bool:
    # (func. aux)
    pos_hueco:Posicion = posicion_vecina_hacia(pos, d)
    pos_enemiga:Posicion = posicion_vecina_hacia(pos, opuesta(d_arrastre))
    t_intermedio1:Tablero = tablero_trasladando_pieza(t0, pos, pos_hueco)
    t_intermedio2:Tablero = tablero_trasladando_pieza(t_intermedio1, pos_enemiga, pos)
    c1:bool = es_posicion_vecina_hacia(pos, d, pos_hueco)
    c2:bool = es_posicion_vecina_hacia(pos, opuesta(d_arrastre), pos_enemiga)
    c3:bool = es_tablero_trasladando_pieza(t0, t_intermedio1, pos, pos_hueco)
    c4:bool = es_tablero_trasladando_pieza(t_intermedio1, t_intermedio2, pos_enemiga, pos)
    c5:bool = es_tablero_despues_de_activar_todas_las_trampas(t_intermedio2, t1)
    return  c1 and c2 and c3 and c4 and c5

def tablero_post_empujar(t0:Tablero, t1:Tablero, pos:Posicion, d:Direccion, d_empuje:Direccion) -> bool:
    pos_enemiga:Posicion = posicion_vecina_hacia(pos, d)
    pos_hueco:Posicion = posicion_vecina_hacia(pos_enemiga, d_empuje)
    t_intermedio1:Tablero = tablero_trasladando_pieza(t0, pos_enemiga, pos_hueco)
    t_intermedio2:Tablero = tablero_trasladando_pieza(t_intermedio1, pos, pos_enemiga)
    c1:bool = es_posicion_vecina_hacia(pos, d, pos_enemiga)
    c2:bool= es_posicion_vecina_hacia(pos_enemiga, d_empuje, pos_hueco)
    c3:bool = es_tablero_trasladando_pieza(t0, t_intermedio1, pos_enemiga, pos_hueco)
    c4:bool = es_tablero_trasladando_pieza(t_intermedio1, t_intermedio2, pos, pos_enemiga)
    c5:bool = es_tablero_despues_de_activar_todas_las_trampas(t_intermedio2, t1)
    return c1 and c2 and c3 and c4 and c5

def hay_que_cambiar_de_turno(j:Juego, m:Movimiento) -> bool:
    res:bool = False
    if j.pasos_consumidos + len(m.pasos) < MAX_PASOS:
        res = False
    else:
        res = True
    return res

def juego_con_turno_posiblemente_avanzado (j0 :Juego, j1:Juego, m:Movimiento) -> bool:
    res : bool = False
    if hay_que_cambiar_de_turno(j0, m):
        res = j1.turno == oponente(j0.turno) and j1.pasos_consumidos == 0
    else:
        res = j1.turno == j0.turno and j1.pasos_consumidos == (j0.pasos_consumidos + len(m.pasos))    
    return res

def juego_post_movimiento(j0:Juego, j1:Juego, m:Movimiento) -> bool:
    # (func. aux) meto tablero post movimiento acá adentro en vez de hacerla aparte
    c1:bool = False
    if m.accion == MOVER_A_SECAS:
        c1 = tablero_post_mover_a_secas(j0.tablero, j1.tablero, m.origen, m.pasos[0])
    elif m.accion == ARRASTRAR:
        c1 = tablero_post_arrastrar(j0.tablero, j1.tablero, m.origen, m.pasos[0], m.pasos[1])
    else: #m.accion == EMPUJAR
        c1 = tablero_post_empujar(j0.tablero, j1.tablero, m.origen, m.pasos[0], m.pasos[1])
    c2:bool = juego_con_turno_posiblemente_avanzado(j0, j1, m)
    return c1 and c2


def realizar_movimiento(j : Juego, m : Movimiento) -> Juego:
    assert juego_bien_formado(j) and movimiento_bien_formado(m)
    assert puede_realizar_movimiento(j, m)
    t1:Tablero = leer_tablero([
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
    pos_destino:Posicion = posicion_vecina_hacia(m.origen, m.pasos[0]) #posición a la cual se mueve la pieza del jugador actual
    pieza_propia:Pieza = j.tablero[m.origen.fila][m.origen.columna] #pieza propia que el jugador actual mueve en este movimiento
    pasos_antes:int = j.pasos_consumidos
    pasos_despues:int = 0
    if m.accion == MOVER_A_SECAS:
        t1 = sacar_pieza(j.tablero, m.origen)
        t1[pos_destino.fila][pos_destino.columna] = pieza_propia
        assert tablero_post_mover_a_secas(j.tablero, t1, m.origen, m.pasos[0])
        pasos_despues = pasos_antes + 1

    if m.accion == ARRASTRAR:
        t1 = sacar_pieza(j.tablero, m.origen)
        pos_enemiga:Posicion = posicion_vecina_hacia(m.origen, opuesta(m.pasos[1])) #la pos_enemiga está en la dirección opuesta del mov que hago para arrastrarla desde pos_propia
        t1[pos_destino.fila][pos_destino.columna] = pieza_propia
        t1 = sacar_pieza(t1, pos_enemiga)
        t1[m.origen.fila][m.origen.columna] = j.tablero[pos_enemiga.fila][pos_enemiga.columna] #pieza enemiga
        assert tablero_post_arrastrar(j.tablero, t1, m.origen, m.pasos[0], m.pasos[1])
        pasos_despues = pasos_antes + 2

    if m.accion == EMPUJAR:
        pos_enemiga:Posicion = posicion_vecina_hacia(m.origen, m.pasos[0])
        t1 = sacar_pieza(j.tablero, pos_enemiga)
        pos_hueco:Posicion = posicion_vecina_hacia(pos_enemiga, m.pasos[1]) #posicion a la cual empuja a la enemiga
        t1[pos_hueco.fila][pos_hueco.columna] = j.tablero[pos_enemiga.fila][pos_enemiga.columna] #pieza enemiga
        t1 = sacar_pieza(t1, m.origen)
        t1[pos_enemiga.fila][pos_enemiga.columna] = pieza_propia
        assert tablero_post_empujar(j.tablero, t1, m.origen, m.pasos[0], m.pasos[1])
        pasos_despues = pasos_antes + 2
        
    turno_nuevo:Color = j.turno
    if not (pasos_despues < MAX_PASOS):
        turno_nuevo = oponente(j.turno)
        pasos_despues = 0
    res:Juego = Juego(t1, turno_nuevo, pasos_despues)
    assert juego_bien_formado(res)
    assert juego_post_movimiento(j, res, m)
    return res

#### Ejercicio 7

def hay_ganador_determinado(j : Juego) -> bool:
    raise Exception("No implementado")

def ganador_del_juego(j : Juego) -> Color:
    raise Exception("No implementado")
