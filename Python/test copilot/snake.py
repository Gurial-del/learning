import pygame
import time
import random

pygame.init()

# Colores
blanco = (255, 255, 255)
amarillo = (255, 255, 102)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Dimensiones de la pantalla
ancho = 600
alto = 400

# Inicializar pantalla
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Juego de la Serpiente')

# Reloj
reloj = pygame.time.Clock()

# Tamaño del bloque
tamaño_bloque = 10
velocidad = 15

# Fuente
fuente = pygame.font.SysFont(None, 35)

def mensaje(msg, color):
    mesg = fuente.render(msg, True, color)
    pantalla.blit(mesg, [ancho / 6, alto / 3])

def juego():
    game_over = False
    game_close = False

    x1 = ancho / 2
    y1 = alto / 2

    x1_cambio = 0
    y1_cambio = 0

    cuerpo_serpiente = []
    longitud_serpiente = 1

    comida_x = round(random.randrange(0, ancho - tamaño_bloque) / 10.0) * 10.0
    comida_y = round(random.randrange(0, alto - tamaño_bloque) / 10.0) * 10.0

    while not game_over:

        while game_close:
            pantalla.fill(negro)
            mensaje("Perdiste! Presiona Q-Quit o C-Play Again", rojo)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        juego()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_cambio = -tamaño_bloque
                    y1_cambio = 0
                elif event.key == pygame.K_RIGHT:
                    x1_cambio = tamaño_bloque
                    y1_cambio = 0
                elif event.key == pygame.K_UP:
                    y1_cambio = -tamaño_bloque
                    x1_cambio = 0
                elif event.key == pygame.K_DOWN:
                    y1_cambio = tamaño_bloque
                    x1_cambio = 0

        if x1 >= ancho or x1 < 0 or y1 >= alto or y1 < 0:
            game_close = True
        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(azul)
        pygame.draw.rect(pantalla, verde, [comida_x, comida_y, tamaño_bloque, tamaño_bloque])
        cabeza_serpiente = []
        cabeza_serpiente.append(x1)
        cabeza_serpiente.append(y1)
        cuerpo_serpiente.append(cabeza_serpiente)
        if len(cuerpo_serpiente) > longitud_serpiente:
            del cuerpo_serpiente[0]

        for x in cuerpo_serpiente[:-1]:
            if x == cabeza_serpiente:
                game_close = True

        for x in cuerpo_serpiente:
            pygame.draw.rect(pantalla, negro, [x[0], x[1], tamaño_bloque, tamaño_bloque])

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho - tamaño_bloque) / 10.0) * 10.0
            comida_y = round(random.randrange(0, alto - tamaño_bloque) / 10.0) * 10.0
            longitud_serpiente += 1

        reloj.tick(velocidad)

    pygame.quit()
    quit()

juego()