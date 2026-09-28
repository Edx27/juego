import pygame
import sys

# Inicializar Pygame
pygame.init()

# Ventana
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego - 2 Mapas")

# Colores
VERDE = (80, 180, 80)
AZUL = (70, 130, 200)
GRIS = (100, 100, 100)
MARRON = (140, 90, 40)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (200, 50, 50)

# Jugador
jugador = pygame.Rect(100, 100, 40, 40)
velocidad = 5

# Mapa actual
mapa = 1

# Fuente
fuente = pygame.font.Font(None, 36)


def dibujar_mapa1():
    # Fondo
    pantalla.fill(VERDE)

    # Caminos
    pygame.draw.rect(pantalla, MARRON, (0, 250, 800, 100))
    pygame.draw.rect(pantalla, MARRON, (350, 0, 100, 600))

    # Árboles
    for x, y in [(80, 80), (650, 100), (100, 450), (650, 450)]:
        pygame.draw.circle(pantalla, VERDE, (x, y), 30)
        pygame.draw.rect(pantalla, MARRON, (x - 8, y + 20, 16, 30))

    # Zona para cambiar de mapa
    pygame.draw.rect(pantalla, ROJO, (720, 250, 80, 100))


def dibujar_mapa2():
    # Fondo
    pantalla.fill(AZUL)

    # Islas
    pygame.draw.ellipse(pantalla, VERDE, (50, 100, 250, 180))
    pygame.draw.ellipse(pantalla, VERDE, (500, 350, 250, 180))

    # Puentes
    pygame.draw.rect(pantalla, MARRON, (280, 170, 240, 50))
    pygame.draw.rect(pantalla, MARRON, (300, 400, 220, 50))

    # Zona para volver al mapa 1
    pygame.draw.rect(pantalla, ROJO, (0, 250, 80, 100))


# Bucle principal
reloj = pygame.time.Clock()

while True:

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        jugador.x -= velocidad
    if teclas[pygame.K_RIGHT]:
        jugador.x += velocidad
    if teclas[pygame.K_UP]:
        jugador.y -= velocidad
    if teclas[pygame.K_DOWN]:
        jugador.y += velocidad

    # Mantener jugador dentro de la pantalla
    jugador.clamp_ip(pantalla.get_rect())

    # Dibujar mapa
    if mapa == 1:
        dibujar_mapa1()
    else:
        dibujar_mapa2()

    # Cambiar de mapa
    if mapa == 1 and jugador.colliderect(pygame.Rect(720, 250, 80, 100)):
        mapa = 2
        jugador.x = 100
        jugador.y = 300

    elif mapa == 2 and jugador.colliderect(pygame.Rect(0, 250, 80, 100)):
        mapa = 1
        jugador.x = 650
        jugador.y = 300

    # Dibujar jugador
    pygame.draw.rect(pantalla, ROJO, jugador)

    # Texto
    texto = fuente.render(f"Mapa {mapa}", True, NEGRO)
    pantalla.blit(texto, (20, 20))

    instrucciones = fuente.render(
        "Flechas: mover | Zona roja: cambiar mapa",
        True,
        BLANCO
    )
    pantalla.blit(instrucciones, (180, 550))

    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(60)
