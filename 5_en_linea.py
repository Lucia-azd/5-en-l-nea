import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 350

VACIO = ' '

ANCHO_GRILLA = 10
LARGO_GRILLA = 10

JUGADOR_O = 'O'
JUGADOR_X = 'X'

def juego_crear():
    """Inicializar el estado del juego"""

    grilla = []

    for f in range(ANCHO_GRILLA):
        grilla.append([])
        for c in range(LARGO_GRILLA):
            grilla[f].append(VACIO)
    
    return grilla

def definir_turno(juego):
    """ Define de quien es el turno """

    contador = 0
    f = 0
    
    while f < ANCHO_GRILLA:
        for c in range(len(juego[f])):
            if juego[f][c] != VACIO:
                contador = contador + 1
                continue
        f = f + 1

    if contador % 2 == 0:
        return JUGADOR_O
    
    return JUGADOR_X

def verificar_turno(juego, turno, fila, columna):
    """ Verifica si la posicion esta vacia, en el caso del que sea VACIO devuelve el turno pasado por parametro """
    
    if juego[fila][columna] == VACIO:
        return turno
    
    return juego[fila][columna] 

def juego_actualizar(juego, x, y):
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    x_1 = 0
    x_2 = 30
    y_1 = 0
    y_2 = 30

    turno = definir_turno(juego)

    juego_nuevo = []
    for f in range(len(juego)):
        juego_nuevo.append([])
        for c in range(len(juego[f])):
            juego_nuevo[f].append(juego[f][c])

    while y_2 < 300:
        for f in range(ANCHO_GRILLA):
            x_1 = 0
            x_2 = 30
            for c in range(LARGO_GRILLA):
                if (x_1 < x < x_2) and (y_1 < y < y_2):
                    turno = verificar_turno(juego, turno, f, c)
                    juego_nuevo[f][c] = turno
                    return juego_nuevo
                elif x_2 < 300:
                    x_1 += 30
                    x_2 += 30
                    continue
            y_1 += 30
            y_2 += 30

def coordenada_columna(columna):
    """ Devuelve la coordenada en pixeles de la posicion columna """

    coordenada = 15

    for i in range(LARGO_GRILLA):
        if columna == i:
            return coordenada
        coordenada += 30

def coordenada_fila(fila):
    """ Devuelve la coordenada en pixeles de la posicion fila """

    coordenada = 15

    for i in range(ANCHO_GRILLA):
        if fila == i:
            return coordenada
        coordenada += 30


def juego_mostrar(juego):
    """Actualizar la ventana"""
    x_1 = 30
    x_2 = 30
    y_1 = 30
    y_2 = 30

    turno = definir_turno(juego)

    gamelib.draw_text(f"Turno: {turno}", 120, 315, fill='violet', anchor='nw')
    for f in range(len(juego)):
        gamelib.draw_line(0, y_1, 300, y_2, fill='white')
        for c in range(len(juego[f])):
            gamelib.draw_line(x_1, 0, x_2, 300, fill='white')
            x_1 += 30
            x_2 += 30
        y_1 += 30
        y_2 += 30

    for f in range(len(juego)):
        for c in range(len(juego[f])):
            if juego[f][c] != VACIO:
                gamelib.draw_text(juego[f][c], coordenada_columna(c), coordenada_fila(f), fill='violet')

def main():
    juego = juego_crear()
    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click

            juego = juego_actualizar(juego, x, y)

gamelib.init(main)

