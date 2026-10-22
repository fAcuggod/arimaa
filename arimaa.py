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
    return (tablero_bien_formado(j.tablero) and (0 <= j.pasos_consumidos) and (j.pasos_consumidos < MAX_PASOS))

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
        return pos2.fila == (pos.fila - 1) and pos2.columna == pos.columna
    elif d == SUR:
        return pos2.fila == (pos.fila + 1) and pos2.columna == pos.columna
    elif d == ESTE:
        return pos2.fila == pos.fila and pos2.columna == (pos.columna + 1)
    else:
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
    assert(not(hay_casilla_vacia(t, pos)))
    es_figura:bool = False
    es_color:bool = False
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

def hay_pieza_amiga_vecina(t : Tablero, pos : Posicion) -> bool:
    raise Exception("No implementado")

def hay_pieza(t : Tablero, pos : Posicion) -> bool:
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
    assert(hay_pieza(t, pos))
    color_propio:Color = t[pos.fila][pos.columna].color
#    if hay_pieza_de_color(t, pos, color_propio):
    raise Exception("No implementado")
    # True <-> hayPiezaEnemigaMásDébilHacia (t, pos, d)

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
    raise Exception("No implementado")

#### Ejercicio 4

def puede_realizar_movimiento(j : Juego, m : Movimiento) -> bool:
    raise Exception("No implementado")

#### Ejercicio 5

def activar_trampas(t : Tablero) -> Tablero:
    raise Exception("No implementado")

#### Ejercicio 6

def realizar_movimiento(j : Juego, m : Movimiento) -> Juego:
    raise Exception("No implementado")

#### Ejercicio 7

def hay_ganador_determinado(j : Juego) -> bool:
    raise Exception("No implementado")

def ganador_del_juego(j : Juego) -> Color:
    raise Exception("No implementado")
