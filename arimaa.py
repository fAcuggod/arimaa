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

#### Espacio para Funciones Auxiliares y Constantes propias.

#### Ejercicio 1

def tablero_bien_formado(t : Tablero) -> bool:
    """
        Indica si el tablero *t* esta bien formado.

        PRE: True

        Args:
            t (Tablero): El tablero de juego para el cual se
                         indica si esta bien formado.
        
        Returns:
            True si la longitud de t (Su cantidad de filas) coincide con la altura ALTO,
            y despues revisa si la longitud de estas filas coincide con el largo ANCHO.
    """
    res: bool = False
    if (len(t) == ALTO):
        for fila in t:
            if (len(fila) != ANCHO):
                return res
            res = True
    return res

def posicion_en_tablero(pos : Posicion) -> bool:
    """
        Indica si la posicion "pos" esta dentro del tablero.

        PRE: True

        Args:
            pos (Posicion): La posicion que determinaremos
                            si esta dentro del tablero o no.        
        Returns:
            True si el valor de fila esta entre 0 (inclusive) y el ALTO,
               y si el valor de columna esta entre 0 (inclusive) y el ANCHO.
    """
    return ((0 <= pos.fila) and (pos.fila < ALTO)) and ((0 <= pos.columna) and (pos.columna < ANCHO))


def movimiento_bien_formado(m : Movimiento) -> bool:
    """
        Indica si el movimiento "m" esta bien formado.

        PRE: True

        Args:
            m (Movimiento): El movimiento que se validara segun sus valores de origen, accion y pasos.

        Returns:
            True si la posicion de origen esta en el tablero
               y si su accion es mover a secas y contiene un elemento de paso
               y si su accion es arrastrar O empujar y contiene dos elementos de pasos.
    """
    res: bool = False
    if (posicion_en_tablero(m.origen)):
        if(m.accion == MOVER_A_SECAS and len(m.pasos) == 1):
            res = True
        elif((m.accion == ARRASTRAR or m.accion == EMPUJAR) and len(m.pasos) == 2):
            res = True
    return res


def juego_bien_formado(j : Juego) -> bool:
    """
        Indica si el juego "j" esta bien formado.

        PRE: True

        Args:
            j (Juego): El juego que se validara segun su tablero y pasos consumidos.

        Returns:
            True si el tablero esta bien formado
               y si los pasos consumidos estan entre 0 (inclusive) y Max_Pasos
    """
    res: bool = False
    if(tablero_bien_formado(j.tablero)):
        if((0 <= j.pasos_consumidos) and (j.pasos_consumidos < MAX_PASOS)):
            res = True
    return res

#### Ejercicio 2
def posicion_vecina_hacia(pos : Posicion, d : Direccion) -> Posicion:
    """
        Para la posicion "pos", nos da una posicion vecina en la direccion "d".

        PRE: True

        Args:
            pos (Posicion): La posicion de origen
            d  (Direccion): La direccion donde se buscara posicion vecina.

        Returns:
            Si d es NORTE, nos dara una posicion en la misma columna de origen pero fila + 1,
          y si d es   SUR, nos dara una posicion en la misma columna de origen pero fila - 1, 
          y si d es OESTE, nos dara una posicion en la misma fila de origen, pero columna - 1,
          y si d es  ESTE, nos dara una posicion en la misma fila de origen, pero columna + 1
    """
    if (d == NORTE):
        return Posicion(pos.fila + 1, pos.columna)
    elif (d == SUR):
        return Posicion(pos.fila - 1, pos.columna)
    elif (d == OESTE):
        return Posicion(pos.fila, pos.columna - 1)
    else:
        return Posicion(pos.fila, pos.columna + 1)

def casilla_en_posicion(t : Tablero, p : Posicion) -> Casilla:
    """
        Dado un tablero 't', nos da la Casilla en la posicion 'p'

        PRE: que tableroBienFormado(t) y posicionEnTablero(p) den True.

        Args:
            t (Tablero): El tablero de juego que se analizara
            p (Posicion): La posicion cuya casilla necesitamos.

        Returns:
            Casilla de 't' con valores correspondientes a la fila y columna de 'p'
    """
    assert(tablero_bien_formado(t) and posicion_en_tablero(p))
    return t[p.fila][p.columna]

def hay_casilla_vacia(t : Tablero, pos : Posicion) -> bool:
    """
        Dado un tablero 't' y una posicion 'pos', nos dira si
        esta casilla esta vacia.

        PRE: que tableroBienFormado(t) y posicionEnTablero(p) den True.

        Args:
            t (Tablero): El tablero de juego que se analizara
            pos (Posicion): La posicion cuya casilla observaremos.

        Returns:
            True si la casilla es Vacia.
    """
    assert(tablero_bien_formado(t) and posicion_en_tablero(pos))
    return casilla_en_posicion(t, pos) == VACIA


def hay_pieza_de_color(t : Tablero, pos : Posicion, col : Color) -> bool:
    """
        Dado un Tablero 't', una Posicion 'pos' y un color 'col',
        nos dira si en el casillo correspondiente hay una pieza del color dado.

        PRE: que tableroBienFormado(t) y posicionEnTablero(p) den True.

        Args:
            t (Tablero): El tablero de juego que se analizara
            pos (Posicion): La posicion cuya casilla observaremos.
            col (Color): El color con el que compararemos.

        Returns:
            True si la casilla contiene una Pieza cuyo color = col
    """
    assert(tablero_bien_formado(t) and posicion_en_tablero(pos))
    return casilla_en_posicion(t, pos).color == col

#### Ejercicio 3

def hay_casilla_vacia_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    """
        Dado un Tablero 't', una Posicion 'pos' y una Direccion 'd',
        nos dira si en la direccion dada tenemos una casilla vacia.

        PRE: que tableroBienFormado(t) y posicionEnTablero(p) den True.

        Args:
            t (Tablero): El tablero de juego que se analizara
            pos (Posicion): La posicion cuya vecina analizaremos.
            d (Direccion): La direccion donde buscaremos una casilla vecina vacia.

        Returns:
            True si la casilla vecina a pos en la direccion 'd' esta vacia.
    """
    assert(tablero_bien_formado(t) and posicion_en_tablero(pos))
    return hay_casilla_vacia(t, posicion_vecina_hacia(pos, d))

"""
def hay_pieza_amiga_vecina(t : Tablero, pos : Posicion) -> bool:
    raise Exception("No implementado")

def hay_pieza_enemiga_mas_debil_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    raise Exception("No implementado")

def hay_pieza_enemiga_mas_fuerte_vecina(t : Tablero, pos : Posicion) -> bool:
    raise Exception("No implementado")

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
"""