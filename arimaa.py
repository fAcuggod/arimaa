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

#### Funciones Auxiliares y Constantes propias.

def hay_pieza(t: Tablero, pos: Posicion) -> bool:
    """
        Dado un tablero 't' y una posicion 'pos',
        nos dira si hay una pieza en la posicion dada.

        PRE: True

        Args:
            t (Tablero): el tablero donde esta la posicion
            pos (Posicion): la posicion que estamos analizando.

        Returns:
            True si la casilla correspondiente a la posicion 'pos'
                 tiene un valor diferente de VACIA.
    """
    return t[pos.fila][pos.columna] != VACIA

def es_enemigo(t: Tablero, pos: Posicion, posEnemiga: Posicion) -> bool:
    """
        Dado un tablero 't' y posiciones 'pos' y 'posEnemiga'
        nos dira si son de colores opuestos.

        PRE: Que haya una pieza en la posicion 'pos'
               y haya una pieza en la posicion 'posEnemiga'

        Args:
            t           (Tablero): el tablero donde estaran ambas posiciones
            pos        (Posicion): la primer posicion a comparar
            posEnemiga (Posicion): la segunda posicion a comparar

        Returns:
            True si la Figura en la posicion 'pos' es de color Dorado y la de 'posEnemiga' es Plateado
               o si la Figura en la posicion 'pos' es de color plateado y la de 'posEnemiga' es Dorado
    """
    assert(hay_pieza(t, pos))
    assert(hay_pieza(t, posEnemiga))
    if(casilla_en_posicion(t, pos).color == DORADO):
        res = casilla_en_posicion(t, posEnemiga).color == PLATEADO
    else:
        res = casilla_en_posicion(t, posEnemiga).color == DORADO
    return res

def direccion_de_movimiento_habilitada(t: Tablero, pos: Posicion, d: Direccion) -> bool:
    """
        Dado un tablero 't', posicion 'pos' y direccion 'd'
        nos dira si podremos movernos en direccion 'd'.

        PRE: Que haya una pieza en la posicion especificada.

        Args:
            t           (Tablero): el tablero donde estaran ambas posiciones
            pos        (Posicion): la posicion actual
            d (Direccion): la direccion en la cual nos queremos mover

        Returns:
            True al menos que haya una figura Conejo de color Dorado y la direccion sea Sur,
               o al menos que haya una figura COnejo de color Plateado y la direccion sea Norte
    """
    assert(hay_pieza(t, pos))
    res: bool = True
    if (casilla_en_posicion(t, pos).figura == CONEJO and casilla_en_posicion(t, pos).color == DORADO):
        res = not (d == SUR)
    elif (casilla_en_posicion(t, pos).figura == CONEJO and casilla_en_posicion(t,pos).color == PLATEADO):
        res = not (d == NORTE)
    return res

def puede_mover_a_secas(t: Tablero, pos: Posicion, d: Direccion):
    """
        Dado un tablero 't', una posicion 'pos' y una direccion 'd',
        determinara si podemos movernos en esa direccion 'd'.

        PRE: True

        Args:
            t    (Tablero) : el tablero donde estaran ambas posiciones
            pos (Posicion) : la posicion desde donde partiremos
            d  (Direccion) : la direccion en la que deseamos movernos.

        Returns:
            True si hay_casilla_vacia_Hacia(t,pos,d) nos devuelve true.
    """
    return hay_casilla_vacia_hacia(t, pos, d)

def puede_arrastrar(t: Tablero, pos: Posicion, d: Direccion, dArrastre: Direccion):
    """
        Dado un tablero 't', una posicion 'pos' y una direccion 'dArrastre',
        determinara si podemos movernos a 'd' arrastrando la ficha enemiga hacia esa direccion 'dArrastre'.

        PRE: True

        Args:
            t    (Tablero) : el tablero donde estaran ambas posiciones
            pos (Posicion) : la posicion desde donde partiremos
            d (DIreccion): la direccion en la que queremos movernos
            dArrastre  (Direccion) : la direccion en la que deseamos arrastrar a la ficha enemiga.

        Returns:
            True si hay_casilla_vacia_Hacia(t,pos,d) y hay_pieza_enemiga_mas_debil_hacia(t, pos, opuesta(dArrastre)) nos devuelven true
    """
    return hay_casilla_vacia_hacia(t, pos, d) and hay_pieza_enemiga_mas_debil_hacia(t, pos, opuesta(dArrastre))

def puede_empujar(t: Tablero, pos: Posicion, d: Direccion, dEmpuje: Direccion):
    """
        Dado un tablero 't', una posicion 'pos', una direccion 'd' y una direccion 'dEmpuje',
        determinara si podemos movernos a 'd' empujando la ficha enemiga hacia esa direccion 'dEmpuje'.

        PRE: True

        Args:
            t    (Tablero) : el tablero donde estaran ambas posiciones
            pos (Posicion) : la posicion desde donde partiremos
            d (DIreccion): la direccion en la que queremos movernos
            dEmpuje  (Direccion) : la direccion en la que deseamos empujar a la ficha enemiga.

        Returns:
            True si hay_pieza_enemiga_mas_debil_hacia(t, pos, d) da true, y al definir posEnemiga como posicion_vecina_hacia(pos, d), 
                    hayCasillaVaciaHacia(t, posEnemiga, dEmpuje) nos dan true.
    """
    res: bool = False
    if(hay_pieza_enemiga_mas_debil_hacia(t, pos, d)):
        posEnemiga : Posicion = posicion_vecina_hacia(pos, d)
        res = hay_casilla_vacia_hacia(t, posEnemiga, dEmpuje)
    return res

def puede_realizar_accion(t: Tablero, m: Movimiento) -> bool:
    """
        Dado un tablero 't' y un movimiento 'm',
        determinara si la accion de dicho movimiento es valida.

        PRE: True

        Args:
            t    (Tablero) : el tablero donde estaran ambas posiciones
            m (Movimiento) : el movimiento que deseamos realizar

        Returns:
            True si la accion del movimiento es Mover a Secas y puedeMOverASecas(t, m.origen, m.pasos[0]) devuelve true,
                ,si la accion del movimiento es Empujar y puedeEmpujar(t, m.origen, m.pasos[0], m.pasos[1]) devuelve true,
               o si la accion del movimiento es Arrastrar y puedeArrastrar(t, m.origen, m.pasos[0], m.pasos[1]) devuelve true.
    """
    res: bool = False
    if(m.accion == MOVER_A_SECAS):
        res = puede_mover_a_secas(t, m.origen, m.pasos[0])
    elif(m.accion == ARRASTRAR):
        res = puede_arrastrar(t, m.origen, m.pasos[0], m.pasos[1])
    else:
        res = puede_empujar(t, m.origen, m.pasos[0], m.pasos[1])
    return res


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

def hay_pieza_amiga_vecina(t : Tablero, pos : Posicion) -> bool:
    """
        Dado un Tablero 't' y una Posicion 'pos',
        nos dira si en la direccion dada tenemos una casilla vacia.

        PRE: que tableroBienFormado(t) y posicionEnTablero(p) den True.
             y que haya una pieza en dicha posicion en el tablero dado.

        Args:
            t (Tablero): El tablero de juego que se analizara
            pos (Posicion): La posicion cuya vecina analizaremos.

        Returns:
            True si en alguna casilla vecina a pos hay una pieza de su mismo color.
    """
    assert(tablero_bien_formado(t) and posicion_en_tablero(pos) and hay_pieza(t, pos))
    res: bool = False
    for d in Direccion:
        if(hay_pieza(t, posicion_vecina_hacia(pos, d)) and casilla_en_posicion(t, posicion_vecina_hacia(pos, d)).color == casilla_en_posicion(t, pos).color):
            res = True
    return res
    

def hay_pieza_enemiga_mas_debil_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    """
        Dado un Tablero 't', una Posicion 'pos' y una Direccion 'd',
        nos dira si en la direccion dada tenemos una ficha del color opuesto
        cuyo valor de fuerza es menor al de la figura en 'pos'

        PRE: que tableroBienFormado(t) y posicionEnTablero(p) den True.
             y que haya una pieza en dicha posicion en el tablero dado.

        Args:
            t    (Tablero): El tablero de juego que se analizara
            pos (Posicion): La posicion cuya posible enemiga analizaremos.
            d  (Direccion): La direccion en la cual buscaremos enemigos.

        Returns:
            True si la casilla vecina en la direccion 'd' contiene una figura
            del color opuesto a la de 'pos', y su valor de fuerza es menor a la misma.

    """
    assert(tablero_bien_formado(t) and posicion_en_tablero(pos) and hay_pieza(t, pos))
    res: bool = False
    posicionVecina : Posicion = posicion_vecina_hacia(pos, d)
    piezaNuestra : Casilla = casilla_en_posicion(t, pos)
    casillaEnemiga : Casilla = casilla_en_posicion(t, posicionVecina)
    if(hay_pieza(t, posicionVecina) and es_enemigo(t, pos, posicionVecina)):
        res = fuerza(piezaNuestra.figura) > fuerza(casillaEnemiga.figura)
    return res

def hay_pieza_enemiga_mas_fuerte_vecina(t : Tablero, pos : Posicion) -> bool:
    """
        Dado un Tablero 't' y una Posicion 'pos',
        nos dira si en alguna direccion tenemos una ficha del color opuesto
        cuyo valor de fuerza es mayor al de la figura en 'pos'

        PRE: que tableroBienFormado(t) y posicionEnTablero(p) den True.
             y que haya una pieza en dicha posicion en el tablero dado.

        Args:
            t    (Tablero): El tablero de juego que se analizara
            pos (Posicion): La posicion cuya posible enemiga analizaremos.

        Returns:
            True si en alguna casilla vecina hay una figura del color opuesto
            a la de 'pos', y su valor de fuerza es mayor a la misma.
    """
    assert(tablero_bien_formado(t) and posicion_en_tablero(pos) and hay_pieza(t, pos))
    res: bool = False
    piezaNuestra : Casilla = casilla_en_posicion(t, pos)
    for d in Direccion:
        posicionVecina : Posicion = posicion_vecina_hacia(pos, d)
        casillaEnemiga : Casilla = casilla_en_posicion(t, posicionVecina)
        if(hay_pieza(t, posicionVecina) and es_enemigo(t, pos, posicionVecina)):
            res = fuerza(piezaNuestra.figura) < fuerza(casillaEnemiga.figura)
    return res

def hay_pieza_congelada(t : Tablero, pos : Posicion) -> bool:
    """
        Dado un Tablero 't' y una Posicion 'pos',
        nos dira si en alguna direccion tenemos una ficha del color opuesto
        cuyo valor de fuerza es mayor al de la figura en 'pos'

        PRE: que tableroBienFormado(t) y posicionEnTablero(p) den True.

        Args:
            t    (Tablero): El tablero de juego que se analizara
            pos (Posicion): La posicion de la pieza.

        Returns:
            True si hay una pieza en la posicion dada del tablero, 
                    cerca suyo hay una pieza enemiga mas fuerte
                    y no hay una pieza aliada cerca.
    """
    assert(tablero_bien_formado(t) and posicion_en_tablero(pos))
    return (hay_pieza(t,pos) and hay_pieza_enemiga_mas_fuerte_vecina(t, pos) and not hay_pieza_amiga_vecina(t, pos))

#### Ejercicio 4
def puede_realizar_movimiento(j : Juego, m : Movimiento) -> bool:
    """
        Dado un juego "j" y un movimiento "m",
        determinaremos si se podra realizar dicho movimiento.

        PRE: que juegoBIenFOrmado(j) y movimientoBIenFormado(m) den True.

        Args:
            j (Juego): El estado actual de la partida.
            m (Movimiento): El movimiento que se esta intentando realizar.

        Returns:
            True si hay_pieza_de_color(j.tablero, m.origen, j.turno) da true,
                    hay_pieza_congelada(j.tablero, m.origen) devuelve false,
                    direccion_de_movimiento_habilitada(j.tablero, m.origen, m.pasos[0]) da true,
                    y (j.pasos_consumidos + len(m.pasos) <= MAX_PASOS) and puede_realizar_accion(j.tablero, m) devuelve true.

    """
    assert(juego_bien_formado(j) and movimiento_bien_formado(m))
    return (hay_pieza_de_color(j.tablero, m.origen, j.turno) and not hay_pieza_congelada(j.tablero, m.origen) and direccion_de_movimiento_habilitada(j.tablero, m.origen, m.pasos[0]) and (j.pasos_consumidos + len(m.pasos) <= MAX_PASOS) and puede_realizar_accion(j.tablero, m))

"""
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