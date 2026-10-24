# **Arimaa**
    - Juegos de dos jugadores (Dorado vs Plateado)
    - Tablero 8x8
        - Filas 1 a 8
        - Columnas A a H
    - Casillas Trampa: C3, C6, F3, F6
    - 16 piezas por jugador, tipos/figuras de mayor a menor fuerza:
        - Elefante x1
        - Camello x1
        - Caballos x2
        - Perros x2
        - Gatos x2
        - Conejos x8
    - Las piezas mas fuertes pueden empujar y arrastrar a las mas debiles del oponente, y congelan a las enemigas adyacentes.
    - Objetivo final: Ubicar un Conejo en la fila extrema opuesta.
- **Etapa 1: Ubicacion de piezas**
    - El tablero empieza vacio
    - El dorado inicia
    - Van poniendo sus piezas en casillas vacias por turnos.
    - No se pueden mover las piezas
    - Dorados solo en filas 1-2
    - Plateados solo en filas 7-8
- **Etapa 2: El juego**
    - Ahora se jugara por turnos.
    - El dorado inicia
    - Cada jugada consta de varios movimientos
        - Cada movimiento consta de uno o dos pasos:
            - Unico paso: Movimiento que solo mueve una pieza propia
            - Dos pasos: Mueve una pieza propia y ademas una pieza enemiga (arrastre o empuje).
        - Cada jugada requerira al menos un movimiento, pero un maximo de 4 pasos.
        - En cada movimiento, el jugador mueve una pieza propia una casilla de distancia en alguna direccino ortogonal (norte, sur, este u oeste)
        - Todas las piezas se mueven igual, excepto los peones, quienes no pueden retroceder.
        - En una jugada se podran hacer varios movimientos con la misma pieza o cuatro piezas diferentes. 
        - En un movimiento la pieza puede cambiar de direccion.
        - CUuando una pieza se mueve, puede arrastrar a una adyacente del oponente siempre que esta sea mas debil. Mientras que la pieza nuestra se mueve, la del oponente ahora ocupara nuestra posicion original.
        - Una pieza tambien puede empujar a una adyacente enemiga siempre que esta sea mas debil, ocupando el lugar donde estaba la enemiga y moviendo al enemigo a otra.
        - Una pieza congela las enemigas adyacentes siempre que sean mas debiles. Una pieza congelada no puede hacer ningun movimiento propio hasta tener una vecina del color propio.
        - Si al final de un movimiento hay una pieza propia o del oponente ubicada en una casilla trampa, y no tiene vecinas de su propio color, esta pieza sera retirada del juego, sea la pieza del jugador o del oponente, o inclusive una que se encontraba ya en la casilla trampa pero perdio a su vecino aliado.
    - El juego finalizara si al final de una jugada hay un conejo en la fila inicial del oponente o si un jugador se queda sin conejos.
    - Si el jugador a quien le toca mover no puede hace rningun movimiento (todas sus piezas estan congeladas o bloqueadas), el juego se traba y no hay ganador.


---
# El proyecto

## archivos
- definiciones: no se modifca, es guia
- arimaa: logica del juego, procedimientos y funcioens estan ya declarados, completarlas pero no cambiar nombres ni tipos. Se puede agregar auxiliares.
- tests: hay qu eagregar casos de test, al menos 90% en cubrimiento de linea y rama.
- cubrimento: obtiene el cubrimiento de forma simple, no se toca
- interfaz: implementacion de la UI, usara nustra logica, ya esta todo hecha esta parte.
- readme: readme del repo + comandos utiles
- piezas: imagenes para la ui
- ejemplo_tab lero: ejemplo de un tablero de juego.

## pautas
- grupo de a 3 o 4
- se debe implementar caso de test para cada ejercicio, y el programa debe pasarlos.
    - adicionalmente tenemos Validar Tests TP en el campus para validar.
- la logica debe estar en arimaa.py
- se deben tipar variables, funciones y parametros
- solo tecnicas vistas en clase, el listado esta disponible en .pdf
- solo se califica con aprueba/desaprueba
- todos los integrantes deben poder responder preguntas sobre el trabajo practico.

## a evaluar
- correccion: todos los ejercicios deben estar bien.
- declaratividad: nombres de variables, parametros, preocedimientos y funciones deben ser apropiados al problema. la estructura del codigo tambien debe comunciar la intencion. evitar breaks o multiples returns asi tambien evitar miedo al booleano.
- modularizacion: evitar repetir codigo innecesariamente, usar adecuadamente los procedimientos y funciones definidos previamente. se pueden agregar mas procedimientos y funciones para separar el codigo. evitar niveles profundos de identacion, si requiere mas de 3 niveles de anidamiento, probablemente pueda usar una subtarea.
- documentacion: deben usar docstrings. # no es documentacion, el codigo debe cumplir un setandar basico de calidad, la documentacion describiendo que hace cada funcion, no como lo hace. sus precondiciones si las hay. los tests no requieren docstrings pero si un estandar de legibilidad co buenos nombres de funcioens y variables. si es necesaria, agregar aclaraciones para el equipo de programacion que lea su codigo.

Ejemplo:

```
def esBisiesto(año: int) -> bool:
    """
    Indica si el año *año* es bisiesto.

    PRE: True

    Args:
        año (int): El numero de año para el cual se indica si es bisiesto.
    
    Returns:
        True si el año *año* es bisiesto y False si no.
    """
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
```

- Testing: todos lso ejercicios (solo los procedimientos y func. pedidas) deben tener sus propios csos que pasen correctamente. Se necesita una cobertura de al menos 90% de lineas y de ramas para todo el archivo.

# Entrega
Se espera uso de Git. Para la entrega se usara gitlab. Repo privado, todos los integrantes y un rold e developer para el usuario de docentes.
Solo un integrante realizara la entrega: quien anoto al grupo en el link para registrarlo.
La entrega consisitra de la URL del repo y un commit particular. Les docentes descargaran el codigo de ese commit de entrega. EN caso de que el link o el commit no se puedan descargar, el trabajo estara desaprobado, pero se podra reentregar en fecha de recuperatorio.

Antes de enviar el trabajo recomendamos que clonen el repo con el link y commit proporcionados, chequear que ambos son validos.

Ejecutar los casos de test de la materia y sus propios casos de test, sobre el repo recien clonado.

Incluir todo archivo/carpeta necesario apra ejecutar los casos de test, los cuales todos deben pasar satifsactoriamente.

# Enunciado

## Tipos de datos
Constantes:
- ALTO = 8
- ANCHO = 8
- Max_Pasos = 4

Tipos de datos a usar:
- **Figura**: Elefante, Camello, Caballo, Perro, Gato o Conejo.
    - Representa cada una de las seis posibles figuras (tipo de pieza) del juego.
- **Color**: Dorado o Plateado
    - Representa los colores de los dos jugadores y sus piezas.
- **Casilla**: Vacia o **Pieza**
    - Representa el contenido de una casilla, puede estar Vacia o contener una pieza (valor del tipo **Pieza**)
- **Pieza**: **Figura** x **Color**
    - Reperesenta una pieza de una cierta figura y cierto color, dada como tupla Figura x Color.
- **Tablero**: Seq(seq(Casilla))
    - Representa el contenido del tablero, una matriz de **Alto** x **Ancho** casillas, representada como una secuencia de filas, cada una de las cuales a su vez es una secuencia de casillas.
- **Accion**: Mover a Secas, Arrastrar o Empujar
    - Representa la accion de una pieza al moverse, puede ser movimiento a secas, movimiento que arrastre una pieza del oponente o movimiento que empuje una pieza del oponente.
- **Posicion**: Z x Z
    - Representa una posicion, normalmente una utpla Fila x Columna, ambos valores estando entre 0 (inclusive) y el Alto u Ancho respectivamente.
- **Direccion**: Norte, Sur, Este u Oeste.
    - Representa cada una de las cuatro direcciones ortogonales
- **Movimiento**: **Accion** x **Posicion** x seq(**Direccion**)
    - Representa un movimiento de pieza unica, casilla unica en direccion ortogonal. Tripla accion-origen-pasos (**Accion** x **Posicion** x seq(**Direccion**)), siendo pasos una lista de direccioens donde:
        - Si la accion es mover a secas, la tripla es un movimiento a secas, la posicion origen corresponde a la casilla de origen de la pieza y pasos es una lista de direcciones de **solo un elemento** donde dicho paso indica la direccion de movimiento.
        - Si la accion es arrastrar o empujar, la tripla representa un movimiento que arrastra una pieza del oponente. Origen corresponde a la casilla de origen de la pieza que se mueve, y pasos es una lista de direccioens de **dos elementos**. El primer paso indica la direccion de movimiento de la pieza que se mueve, el segundo paso indica a direccion de movimiento de la pieza oponente que se arrastra u empuja segun la accion.
- **Juego**: **Tablero** x **Color** x Z
    - Reperesenta el estado actual del juego. Tabero representa el estado actual del tablero, turno es el color del jugador al que le toca jugar actualmente y pasosConsumidos es el numero de pasos ya efectuados por el jugador en el turno actual.

## Tipos de datos y funciones
Nombres de variables que usaremos normalmente:
- i, n para denotar numeros enteros
- f para denotar figuras
- col para denotar colores
- c para denotar casillas
- t para denotar tableros
- pos para denotar posiciones
- d para denotar direcciones
- m para denotar movimientos
- j para denotar juegos
- Sufijo -s para denotar secuencias, por ejemplo ds es una lista de direcciones.
### Convenciones de notacion y funciones primitivas
- Si t es una n-upla, notamos t a su i-esima componente, para cada 1 <= i <= n
- Si s es una secuencia, notamos |s| a su longitud y s[i] a su i-esimo elemento para cada 0 <= i < |s|
- Suponemos definida la funcion fuerza(f: Figura):Z del siguiente modo:
    fuerza(Conejo) = 1
    fuerza(Gato) = 2
    fuerza(Perro) = 3
    fuerza(Caballo) = 4
    fuerza(Camello) = 5
    fuerza(Elefante) = 6
- Suponemos definida la funcion oponente(col: Color):Color tal que:
    oponente(Dorado) = Plateado
    oponente(Plateado) = Dorado
- Suponemos definida la funcion opuesta(d: Direccion): Direccion tal que:
    opuesta(Norte) = Sur
    opuesta(Sur) = Norte
    opuesta(Este) = Oeste
    opuesta(Oeste) = Este
- Suponemos definida la constante Posiciones_Trampa:seq(Posicion) del siguiente modo: Posiciones_Trampa = [(2,2),(2,5),(5,2),(5,5)], representando las casillas trampa C3, F3, C6 y F6
- Si c es una Casilla no vacia, entonces c es una Pieza, en tal caso tiene c.figura y c.color respectivamente.
- Si p es una Posicion, tendra p.fila y p.columna respectivamente.
- Si m es un Movimiento, tendremos m.accion, m.origen y m.pasos respectivamente.
- Si j es un Juego, tendremos j.tablero, j.turno y j.pasosConsumidos respectivamente.

# Predicados auxiliares

## Ejercicio 1: Buena formacion
tableroBienFormado(t:Tablero)
    := |t| = ALTO 
     y para todo i:Z,(0 <= i < |t| -> |t[i]| = ANCHO)

posicionEnTablero(pos: Posicion)
    := 0 <= pos.fila < ALTO 
     y 0 <= pos.columna < ANCHO

movimientoBienFormado(m: Movimiento)
    := posicionEnTablero(m.origen)
     y (m.accion = Mover_A_Secas           -> |m.pasos| = 1)
     y (m.accion = Arrastrar o Empujar     -> |m.pasos| = 2)

juegoBienFormado(j: Juego)
    := tableroBienFormado(j.tablero)
     y 0 <= j.pasosConsumidos < Max_Pasos

## Ejercicio 2: Tablero y contenido

esPosicionVecinaHacia(pos: Posicion, d: Direccion, pos': Posicion)
    := (d = NORTE -> (pos'.fila = pos.fila + 1 y pos'.columna = pos.columna))
     y (d = SUR   -> (pos'.fila = pos.fila - 1 y pos'.columna = pos.columna))
     y (d = ESTE  -> (pos'.fila = pos.fila y pos'.columna = pos.columna + 1))
     y (d = OESTE -> (pos'.fila = pos.fila y pos'.columna = pos.columna - 1))

hayCasillaVacia(t: Tablero, pos: Posicion)
    := posicionEnTablero(pos)
     y t[pos.fila][pos.columna] = Vacia

hayFiguraDeColor(t: Tablero, pos: Posicion, f: Figura, col: Color)
    := posicionEnTablero(pos)
     y no(hayCasillaVacia(t, pos))
     y t[pos.fila][pos.columna].figura = f
     y t[pos.fila][pos.columna].color  = col

hayCasillaVaciaHacia(t: Tablero, pos: Posicion, d: Direccion)
    := existe pos': Posicion . (
        esPosicionVecinaHacia(pos, d, pos')
        y hayCasillaVacia(t, pos')      
    )

tablerosCoincidenEnLaPosicion(t1, t2: Tablero, pos: Posicion)
    := t1[pos.fila][pos.columna] = t2[pos.fila][pos.columna]

tablerosCoincidenSalvoEnLaPosicion(t1, t2: Tablero, pos: Posicion)
    := para todo pos': Posicion .(
        (posicionEnTablero(pos') y pos' ≠ pos) ->
            tablerosCoincidenEnLaPosicion(t1, t2, pos')
    )

esTableroSacandoPieza(t0, t1: Tablero, pos: Posicion)
    := tablerosCoincidenSalvoEnLaPosicion(t0, t1, pos)
     y hayCasillaVacia(t1, pos)

esTableroPoniendoPieza(t0, t1: Tablero, pos: Posicion, f: Figura, col: Color)
    := tablerosCoincidenSalvoEnLaPosicion(t0, t1, pos)
     y hayFiguraDeColor(t1, pos, f, col)

esTableroTrasladandoPieza(t0, t1: Tablero, posorigen, posdestino: Posicion)
    := existe f:Figura, existe col: Color, existe tintermedio: Tablero, (
        hayFiguraDeColor(t0, posorigen, f, col)
        y esTableroSacandoPieza(t0, tintermedio, posorigen)
        y esTableroPoniendoPieza(tintermedio, t1, posdestino, f, col)
    )

## Ejercicio 3: Logica del juego

hayPieza(t: Tablero, pos: Posicion)
    := existe f:Figura, existe col:Color, hayFiguraDeColor(t, pos, f, col)

hayPiezaDeColor(t: Tablero, pos: Posicion, col: Color)
    := existe f:Figura, hayFiguraDeColor(t, pos, f, col)

hayPiezaAmigaHacia(t: Tablero, pos: Posicion, d: Direccion)
    := existe col:Color, existe posamiga: Posicion, (
        hayPiezaDeColor(t, pos, col)
        y esPosicionVecinaHacia(pos, d, posamiga)
        y hayPiezaDeColor(t, posamiga, col)
    )

hayPiezaAmigaVacina(t: Tablero, pos: Posicion)
    := existe d:Direccion, hayPiezaAmigaHacia(t, pos, d)

hayPiezaEnemigaMasDebilHacia(t: Tablero, pos: Posicion, d: Direccion)
    := existe f:Figura, existe col:Color, existe posenemiga: POsicion, existe fenemiga: Figura, (
        hayFiguraDeColor(t, pos, f, col)
        y esPOsicionVecinaHacia(pos, d, posenemiga)
        y hayFiguraDeColor(t, posenemiga, fenemiga, oponente(col))
        y fuerza(f) > fuerza(fenemiga)
    )

hayPiezaEnemigaMasFuerteHacia(t: Tablero, pos: Posicion, d: DIreccion)
    := existe f:Figura, existe col: Color, existe posEnemiga: Posicion, existe fEnemiga: Figura, (
        hayFiguraDeColor(t, pos, f, col)
        y esPosicionVecinaHacia(pos, d, posenemiga)
        y hayFiguraDeColor(t, posenemiga, fenemiga, oponente(col))
        y fuerza(f) < fuerza(fenemiga)
    )

hayPiezaEnemigaMasFuerteVecina(t: Tablero, pos: Posicion)
    := existe d: Direccion, hayPiezaEnemigaMasFuerteHacia(t, pos, d)

hayPiezaCongelada(t: Tablero, pos: Posicion)
    := hayPieza(t, pos)
     y hayPiezaEnemigaMasFuerteVecina(t, pos)
     y no(hayPiezaAmigaVecina(t, pos))

## Ejercicio 4: Es posible Realizar un movimiento?

direccionDeMovimientoHabilitada(t: Tablero, pos: Posicino, d: Direccion)
    := existe f:FIgura, existe col:Color, (
        hayFiguraDeColor(t, pos, f, col)
        y ((f = CONEJO y col = DORADO) -> d ≠ SUR)
        y ((f = CONEJO y col = PLATEADO) -> d ≠ NORTE)
    )

puedeMoverASecas(t: Tablero, pos: Posicion, d: Direccion)
    := hayCasillaVaciaHacia(t, pos, d)

puedeArrastrar(t: Tablero, pos: Posicion, d, darrastre: Direccion)
    := hayCasillaVaciaHacia(t, pos, d)
     y hayPiezaEnemigaMasDebilHacia(t, pos, opuesta(darrastre))

puedeEmpujar(t: Tablero, pos: Posicion, d, dempuje: DIreccion)
    := hayPiezaEnemigaMasDebilHacia(t, pos, d)
     y existe posEnemiga: Posicion, (
        esPosicionVecinaHacia(pos, d, posenemiga)
        y hayCasillaVaciaHacia(t, posenemiga, dempuje)
     )

puedeRealizarAccion(t: Tablero, m: Movimiento)
    := (m.accion = Mover_A_Secas ->
        puedeMoverASecas(t, m.origen, m.pasos[0]))
     y (m.accion = Arrastrar ->
        puedeArrastrar(t, m.origen, m.pasos[0], m.pasos[1]))
     y (m.accion = Empujar ->
        puedeEmpujar(t, m.origen, m.pasos[0], m.pasos[1]))

puedeRealizarMovimiento(j: Juego, m: Movimiento)
    := hayPiezaDeColor(j.tablero, m.origen, j.turno)
     y no(hayPiezaCongelada(j.tablero, m.origen))
     y direccionDeMovimientoHabilitada(j.tablero, m.origen, m.pasos[0])
     y j.pasosCOnsumidos + |m.pasos| <= Max_Pasos
     y puedeRealizarAccion(j.tablero, m)

## Ejercicio 5: Casillas trampa

esTableroDespuesDeActivarTrampa(t0, t1: Tablero, posTrampa: Posicion)
    := ( hayPiezaAmigaVecina(t0, posTrampa) -> t1 = t0)
     y ( no(hayPiezaAmigaVecina(t0, posTrampa) -> esTableroSacandoPieza(t0, t1, posTrampa)))

esTableroDespuesDeActivarTodasLasTrampas(t0, t1: Tablero)
    := existe tintermedio1, tintermedio2, tintermedio3: Tablero, (
        esTableroDespuesDeActivarTrampa(t0, tintermedio1, Posiciones_Trampa[0])
        y esTableroDespuesDeActivarTrampa(tintermedio1, tintermedio2, Posiciones_Trampa[1])
        y esTableroDespuesDeActivarTrampa(tintermedio2, tintermedio3, Posiciones_Trampa[2])
        y esTableroDespuesDeActivarTrampa(tintermedio3, t1, Posiciones_Trampa[3])
    )

## Ejercicio 6: Determinar el estado del juego despues de un movimiento

tableroPostMoverASecas(t0, t1: Tablero, pos: Posicion, d: Direccion)
    := existe posDestino: Posicion, existe tintermedio: Tablero, (
        esPosicionVecinaHacia(pos, d, posDestino)
        y esTableroTrasladandoPieza(t0, tintermedio, pos, posdestino)
        y esTableroDespuesDeActivarTodasLasTrampas(tintermedio, t1)
    )

tableroPostArrastrar(t0, t1: Tablero, pos: Posicion, d, darrastre: Direccion)
    := existe posHueco, posEnemiga: Posicion, existe tintermedio, tintermedio2: Tablero, (
        esPosicionVecinaHacia(pos, d, poshueco)
        y esPosicionVecinaHacia(pos, opuesta(darrastre), posenemiga)
        y esTableroTrasladandoPieza(t0, tintermedio1, pos, poshueco)
        y esTableroTrasladandoPieza(tintermedio1, tintermedio2, posenemiga, pos)
        y esTableroDespuesDeActivarTOdasLasTrampas(tintermedio2, t1)
    )

tableroPostEmpujar(t0, t1: Tablero, pos: Posicion, d, dempuje: DIreccion)
    := existe posenemiga, poshueco: Posicion, existe tintermedio1, tintermedio2: Tablero, (
        esPosicionVecinaHacia(pos, d, posenemiga)
        y esPosicionVecinaHacia(posenemiga, dempuje, poshueco)
        y esTableroTrasladandoPieza(t0, tintermedio1, posenemiga, poshueco)
        y esTableroTrasladandoPieza(tintermedio1, tintermedio2, pos, posEnemiga)
        y esTableroDespuesDeActivarTodasLasTrampas(tintermedio2, t1)
    )

tableroPostMovimiento(t0, t1: Tablero, m: Movimiento)
    := (m.accion = Mover_A_Secas -> tableroPostMoverASecas(t0, t1, m.origen, m.pasos[0]))
     y (m.accion = Arrastrar -> tableroPostArrastrar(t0, t1, m.origen, m.pasos[0], m.pasos[1]))
     y (m.accion = Empujar -> tableroPostEmpujar(t0, t1, m.origen, m.pasos[0], m.pasos[1]))

hayQueCambiarDeTurno(j: Juego, m: Movimiento)
    := j.pasosConsumidos + |m.pasos| = Max_Pasos

juegoConTurnoPosiblementeAvanzado(j0, j1: Juego, m: Movimiento)
    := (hayQUeCambiarDeTUrno(j0, m) ->
        (j1.turno = oponente(j0.turno) y j1.pasosConsumidos= 0))
     y (no(hayQueCambiarDeTUrno(j0, m) ->
        (j1.turno = j0.turno y j1.pasosConsumidos = j0.pasosConsumidos + |m.pasos|)))
    
juegoPostMovimiento(j0, j1: Juego, m: Movimiento)
    := tableroPostMovimiento(j0.tablero, j1.tablero, m)
     y juegoConTUrnoPosiblementeAvanzado(j0, j1, m)

## Ejercicio 7: Determinar el ganador

esInicioDeTUrno(j: Juego, col: Color)
    := j.turno = col
     y j.pasosConsumidos = 0

hayCOnejoEnTablero(j: Juego, col: Color)
    := existe pos: Posicion, hayFiguraDeColor(j.tablero, pos, Conejo, col)

posicionEnFilaInicial(pos: Posicion, col: Color)
    := (col = Dorado -> pos.fila = 0)
     y (col = Plateado -> pos.fila = 7)

hayCOnejoEnFilaInicialOponente(j: Juego, col: Color)
    := existe pos: Posicion , (
        posicionEnFIlaInicial(pos, oponente(col))
        y hayFiguraDeColor(j.tablero, pos, Conejo, col)
    )

reuneCondicionesDeGanar(j: Juego, col: Color)
    := hayCOnejoEnFilaInicialOponente(j, col)
     y no(hayCONejoEnTablero(j, oponnete(col)))

reuneCOndicionesDeGanarExclusivas(j: Juego, col: Color)
    := reuneCondicionesDeGanar(col)
     y no(reuneCondicionesDeGanar(j, oponente(col)))

esJugadorGanador(j, Juego, col: Color)
    := (esInicioDeTurno(j, oponente(col)) y reuneCondicionesDeGanar(j, col))
     y (esInicioDeTUrno(j, col) y reuneCondicionesDeGanarExclusivas(j, col))

hayGanadorDeterminado(j: Juego)
    := existe col:Color, esJugadorGanador(j, col)

# Ejercicios

## Ejercicio 1

tablero_bien_formado: recibe t: Tablero y devuelve Bool.
    requiere: True
    asegura: res true si tableroBienFormado(t) da True.

posicion_en_tablero: recibe pos: Posicion y devuelve Bool
    requiere: True
    asegura: res true si posicionEnTablero(pos) da True.

movimiento_bien_formado: recibe m: Movimiento y devuelve BOol
    requiere: True
    asegura: res true si movimientoBienFormado(m) da True

juego_bien_formado: recibe j: Juego y devuelve Bool
    requiere: True
    assegura: res true si juegoBienFormado(j) da True

## Ejercicio 2

posicion_vecina_hacia: recibe pos: Posicion y d: Direccion y devuelve Posicion
    requiere: True
    asegura: esPosicionVecinaHacia(pos,d, res)

casilla_en_posicion: recibe t:Tablero y pos: Posicion y devuelve Casilla
    requiere: tableroBienFormado(t) y posicionEnTablero(pos)
    asegura: res = t[pos.fila][pos.columna]

hay_casilla_vacia: recibe t: Tablero y pos: Posicion y devuelve booleano
    requiere: tableroBienFormado(t) y posicionEnTablero(pos)
    asegura: res true si hayCasillaVacia(t, pos)

hay_pieza_de_color: recibe t: Tablero, pos: Posicion y col: Color y devuelve booleano
    requiere: tableroBienFormado(t) y posicionEnTablero(pos)
    asegura: res true si hayPiezaDeColor(t, pos, col)

## Ejercicio 3

hay_casilla_vacia_hacia: recibe t: Tablero, pos: Posicion y d: Direccino y devuelve booleano
    requiere: tableroBienFormado(t) y posicionEnTablero(pos)
    asegura: res true si hayCasillaVaciaHacia(t, pos, d)

hay_pieza_amiga_vecina: recibe t: Tablero, pos: Posicion y devuelve booleano
    requiere: tableroBienFormado(t) y posicionEnTablero(pos)
    requiere: hayPieza(t, pos)
    asegura: res true si hayPiezaAmigaVecina(t, pos)

hay_pieza_enemiga_mas_debil_hacia: recibe t: Tablero, pos: Posicion y d: Direccion, devuelve booleano
    requiere: tableroBienFormado(t) y posicionEnTablero(pos)
    requiere: hayPieza(t, pos)
    asegura: res true si hayPiezaEnemigaMasDebilHacia(t, pos, d)

hay_pieza_enemiga_mas_fuerte_vecina: recibe t: Tablero, pos: Posicion, devuelve booleano
    requiere: tableroBienFormado(t) y posicionEnTablero(pos)
    requiere: hayPieza(t, pos)
    asegura: res true si hayPiezaEnemigaMasFuerteVecina(t, pos)

hay_pieza_congelada: recibe t: Tablero, pos: Posicion, devuelve booleano
    requiere: tableroBienFormado(t) y posicionEnTablero(pos)
    asegura: res true si hayPiezaCongelada(t, pos)

## Ejercicio 4
puede_realizar_movimiento: recibe j: Juego, m: Movimiento, devuelve boleano
    requiere: juegoBienFormado(j) y movimientoBienFormado(m)
    asegura: res true si puedeRealizarMovimiento(j, m)

## Ejercicio 5
activar_trampas: recibe t: Tablero y devuelve Tablero
    requiere: tableroBienFormado(t)
    asegura:  tableroBienFormado(res)
    asegura: esTableroDespuesDeActivarTodasLasTrampas(t, res)

## Ejercicio 6
realizar_movimiento: recibe j: Juego y m: Movimiento, devuelve Juego
    requiere: juegoBienFormado(j) y movimientoBienFormado(m)
    requiere: puedeRealizarMovimiento(j, m)
    asegura: juegoBienFOrmado(res)
    asegura: juegoPostMovimiento(j, res, m)

## Ejercicio 7
hay_ganador_determinado: recibe j: Juego y devuelve booleano.
    requiere: juegoBienFormado(j)
    asegura: res true si hayGanadorDeterminado(j)

ganador_del_juego: recibe j: Juego y devuelve Color
    requiere: juegoBIenFormado(j)
    requiere: hayGanadorDeterminado(j)
    asegura: esJugadorGanador(j, res)


## Comandos útiles

1) Para hacer chequeo de tipos del código:

  python -m mypy arimaa.py

2) Para correr los casos de test:

  python -m unittest tests.py

3) Para evaluar el cubrimiento del código por los casos de test:

  python -m coverage run --include arimaa.py --branch -m unittest tests.py && python -m coverage json && python cubrimiento.py

4) Para correr la interfaz gráfica:
      python interfaz.py
