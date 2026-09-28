import pygame
import sys

pygame.init()

# -----------------------------
# CONFIGURACIÓN
# -----------------------------
ANCHO = 800
ALTO = 600
TAM = 50

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Bomberman - 2 Niveles")

reloj = pygame.time.Clock()

# Colores
NEGRO = (20, 20, 20)
BLANCO = (255, 255, 255)
AZUL = (40, 120, 200)
VERDE = (50, 180, 70)
GRIS = (100, 100, 100)
MARRON = (160, 100, 40)
ROJO = (220, 40, 40)
AMARILLO = (255, 220, 40)

# -----------------------------
# MAPA 1
# 1 = pared
# 2 = bloque destruible
# 0 = espacio
# -----------------------------

mapa1 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,2,0,0,1,0,0,0,1,0,2,0,0,1],
    [1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1],
    [1,2,1,0,0,0,0,0,1,0,0,0,0,2,0,1],
    [1,0,1,0,1,1,1,0,1,0,1,1,1,0,0,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,0,2,1],
    [1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,1,0,1,0,1,0,1,1,1,1,0,1],
    [1,0,0,2,0,0,0,0,1,0,0,0,2,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# -----------------------------
# MAPA 2
# -----------------------------

mapa2 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,2,0,0,1,0,0,2,0,0,1,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,2,0,1],
    [1,1,1,0,1,1,0,1,0,1,1,1,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,1,0,2,1],
    [1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,2,0,0,0,0,0,0,0,0,2,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# -----------------------------
# JUGADOR
# -----------------------------

jugador_x = 1
jugador_y = 1

nivel = 1


# -----------------------------
# DIBUJAR MAPA
# -----------------------------

def dibujar_mapa(mapa):

    for fila in range(len(mapa)):
        for columna in range(len(mapa[fila])):

            x = columna * TAM
            y = fila * TAM

            if mapa[fila][columna] == 1:

                # Pared
                pygame.draw.rect(
                    pantalla,
                    GRIS,
                    (x, y, TAM, TAM)
                )

                pygame.draw.rect(
                    pantalla,
                    NEGRO,
                    (x, y, TAM, TAM),
                    2
                )

            elif mapa[fila][columna] == 2:

                # Bloque destruible
                pygame.draw.rect(
                    pantalla,
                    MARRON,
                    (x + 3, y + 3, TAM - 6, TAM - 6)
                )

                pygame.draw.rect(
                    pantalla,
                    NEGRO,
                    (x, y, TAM, TAM),
                    2
                )

            else:

                # Piso
                pygame.draw.rect(
                    pantalla,
                    VERDE,
                    (x, y, TAM, TAM)
                )

                pygame.draw.rect(
                    pantalla,
                    (40, 130, 50),
                    (x, y, TAM, TAM),
                    1
                )


# -----------------------------
# BUCLE DEL JUEGO
# -----------------------------

while True:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Cambiar de nivel con N
        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_n:

                if nivel == 1:
                    nivel = 2
                    jugador_x = 1
                    jugador_y = 1

                else:
                    nivel = 1
                    jugador_x = 1
                    jugador_y = 1


    # -------------------------
    # MOVIMIENTO
    # -------------------------

    teclas = pygame.key.get_pressed()

    if nivel == 1:
        mapa_actual = mapa1
    else:
        mapa_actual = mapa2

    nuevo_x = jugador_x
    nuevo_y = jugador_y

    if teclas[pygame.K_LEFT]:
        nuevo_x -= 1

    if teclas[pygame.K_RIGHT]:
        nuevo_x += 1

    if teclas[pygame.K_UP]:
        nuevo_y -= 1

    if teclas[pygame.K_DOWN]:
        nuevo_y += 1

    # Comprobar que no atraviese paredes
    if mapa_actual[nuevo_y][nuevo_x] == 0:

        jugador_x = nuevo_x
        jugador_y = nuevo_y


    # -------------------------
    # DIBUJAR
    # -------------------------

    pantalla.fill(NEGRO)

    dibujar_mapa(mapa_actual)

    # Jugador
    pygame.draw.rect(
        pantalla,
        AZUL,
        (
            jugador_x * TAM + 8,
            jugador_y * TAM + 8,
            TAM - 16,
            TAM - 16
        )
    )

    # Cabeza
    pygame.draw.circle(
        pantalla,
        AMARILLO,
        (
            jugador_x * TAM + 25,
            jugador_y * TAM + 20
        ),
        10
    )

    # Texto del nivel
    fuente = pygame.font.Font(None, 32)

    texto = fuente.render(
        f"Nivel {nivel}   |   N = Cambiar nivel",
        True,
        BLANCO
    )

    pantalla.blit(texto, (10, 565))

    pygame.display.flip()

    reloj.tick(10)
