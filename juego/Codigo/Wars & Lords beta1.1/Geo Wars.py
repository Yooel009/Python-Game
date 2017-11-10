import pygame, sys, random

from pygame.locals import *

# variables globales

ANCHOVENTANA = 1080

ALTOVENTANA = 800

NEGRO = (0, 0, 0)

BLANCO = (255, 255, 255)

ROJO = (255, 0, 0)

VERDE = (0, 255, 0)

AZUL = (0, 0, 255)

FPS = 25

# funciones globales

def terminar():

     pygame.quit()

     sys.exit()

def cargar_imagen(direccion, transparente=False):

    try:
        imagen = pygame.image.load(direccion)
    except pygame.error, message:
        raise SystemExit, message
    if transparente:
        color = imagen.get_at((0, 0))
        imagen.set_colorkey(color, RLEACCEL)
    return imagen

def dibujarTexto(texto, fuente, superficie, posision, color):

    objetotexto = fuente.render(texto, 1, color)

    rectangulotexto = objetotexto.get_rect()

    rectangulotexto.topleft = posision

    superficie.blit(objetotexto, rectangulotexto)

def crear_enemigos(probabilidad):

    if probabilidad == 0:

        probabilidad = 3

    opcion = random.randrange(500/probabilidad)

    if opcion == 1:

       player_2.poblacion -= 1

       if player_2.poblacion >= 0:

           soldado_enemigo = Soldado(soldado_frente1, soldado_frente2, False)

           tropas_player2.add(soldado_enemigo)
       else:
           player_2.poblacion +=1

    if opcion == 2:

       player_2.poblacion -= 2

       if player_2.poblacion >= 0:

          arquero_enemigo = Arquero(arquero_frente1, arquero_frente2, False)

          tropas_player2.add(arquero_enemigo)
       else:
          player_2.poblacion += 2

    if opcion == 3:
       player_2.poblacion -= 3

       if player_2.poblacion >= 0:

          lancero_enemigo = Lancero(lancero_frente1, lancero_frente2, False)

          tropas_player2.add(lancero_enemigo)
       else:
           player_2.poblacion += 3

    if opcion == 4:

       player_2.poblacion -= 4

       if player_2.poblacion >= 0:

          monje_enemigo = Monje(monje_frente1, monje_frente2, False)

          tropas_player2.add(monje_enemigo)
       else:
           player_2.poblacion += 4

    if opcion == 5:

       player_2.poblacion -= 5

       if player_2.poblacion >= 0:

          cazador_enemigo = Cazador(cazador_frente1, cazador_frente2, False)

          tropas_player2.add(cazador_enemigo)
       else:
           player_2.poblacion += 5

    if opcion == 6:

       player_2.poblacion -= 6

       if player_2.poblacion >= 0:

          gladiador_enemigo = Gladiador(gladiador_frente1, gladiador_frente2, False)

          tropas_player2.add(gladiador_enemigo)
       else:
           player_2.poblacion += 6

def colision_batalla():

    for tropa_p1 in tropas_player1:

        for tropa_p2 in tropas_player2:

            if tropa_p1.rect.colliderect(tropa_p2) == True:

                if tropa_p1.rect.y < ALTOVENTANA / 2:

                   tropa_p1.vida -= 2

                   tropa_p2.vida -= 1

                   tropa_p1.rect.move_ip(0, 16)

                   tropa_p2.rect.move_ip(0, -16)
                else:
                    tropa_p2.vida -= 2

                    tropa_p1.vida -= 1

                    tropa_p2.rect.move_ip(0, -16)

                    tropa_p1.rect.move_ip(0, 16)

                if tropa_p1.vida <= 0:

                    tropas_player1.remove(tropa_p1)

                if tropa_p2.vida <= 0:

                    tropas_player2.remove(tropa_p2)

def nueva_partida():

    decorar_mapa()

    decoracion_secundaria = True

    while True:  # el ciclo del juego se mantiene mientras se este jugando

        pygame.mouse.set_visible(True)

        pygame.display.flip()

        relojPrincipal.tick(FPS)

        verificar_creacion()

        for evento in pygame.event.get():

            if evento.type == QUIT:
                terminar()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:
                    pausa()

                if evento.key == pygame.K_1:

                    player_1.poblacion -= 1

                    if player_1.poblacion >= 0:

                        soldado = Soldado(soldado_atras1, soldado_atras2, True)

                        tropas_player1.add(soldado)

                        num = random.randrange(10)

                        crear_enemigos(num)
                    else:
                        player_1.poblacion += 1

                if evento.key == pygame.K_2:

                    player_1.poblacion -= 2

                    if player_1.poblacion >= 0:

                        arquero = Arquero(arquero_atras1, arquero_atras2, True)

                        tropas_player1.add(arquero)

                        num = random.randrange(10)

                        crear_enemigos(num)
                    else:
                        player_1.poblacion += 2

                if evento.key == pygame.K_3:

                    player_1.poblacion -= 3

                    if player_1.poblacion >= 0:

                        lancero = Lancero(lancero_atras1, lancero_atras2, True)

                        tropas_player1.add(lancero)

                        num = random.randrange(10)

                        crear_enemigos(num)
                    else:
                        player_1.poblacion += 3

                if evento.key == pygame.K_4:

                    player_1.poblacion -= 4

                    if player_1.poblacion >= 0:

                        monje = Monje(monje_atras1, monje_atras2, True)

                        tropas_player1.add(monje)

                        num = random.randrange(10)

                        crear_enemigos(num)
                    else:
                        player_1.poblacion += 4

                if evento.key == pygame.K_5:

                    player_1.poblacion -= 5

                    if player_1.poblacion >= 0:

                        cazador = Cazador(cazador_atras1, cazador_atras2, True)

                        tropas_player1.add(cazador)

                        num = random.randrange(10)

                        crear_enemigos(num)
                    else:
                        player_1.poblacion += 5

                if evento.key == pygame.K_6:

                    player_1.poblacion -= 6

                    if player_1.poblacion >= 0:

                        gladiador = Gladiador(gladiador_atras1, gladiador_atras2, True)

                        tropas_player1.add(gladiador)

                        num = random.randrange(10)

                        crear_enemigos(num)
                    else:
                        player_1.poblacion += 6

        crear_enemigos(4)

        pantalla.blit(fondo, (0, 0))

        colision_batalla()

        tropas_player2.draw(pantalla)

        tropas_player1.draw(pantalla)

        # actualizo las vidas

        player_1.estado_vida()

        player_2.estado_vida()

        if player_1.vida <= 0 or player_2.vida <= 0:
            terminar()

        if player_1.vida > 0 and player_1.poblacion == 0 and player_2.vida > 0 and player_2.poblacion == 0:

            player_1.escuadron += 1

            if player_1.escuadron == 2:

                pausa()

                player_1.poblacion = 150

                player_2.poblacion = 150

                nueva_partida()

            if player_1.escuadron == 3:

                pausa()

                player_1.poblacion = 200

                player_2.poblacion = 200

                nueva_partida()

        # genero ambientacion

        lista_decoracion.draw(pantalla)

        indicadores.draw(pantalla)

        casas.draw(pantalla)

        # actualizo la posicion de las tropas

        tropas_player2.update()

        tropas_player1.update()

        dibujarTexto(str(player_1.vida), fuente, pantalla, (70, ALTOVENTANA - 40), NEGRO)

        dibujarTexto(str(player_2.vida), fuente, pantalla, ((ANCHOVENTANA - 110), 30), NEGRO)

        dibujarTexto(str(player_1.poblacion), fuente, pantalla, (995, ALTOVENTANA - 50), NEGRO)

        dibujarTexto(str(player_2.poblacion), fuente, pantalla, (40, 20), NEGRO)

def pausa():

    pygame.init()

    pantalla_pausa = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA))

    fondo_pausa = cargar_imagen('imagenes/lienzo.jpg')

    fondo_pausa = pygame.transform.scale(fondo_pausa, (ANCHOVENTANA, ALTOVENTANA))

    pantalla_pausa.blit(fondo_pausa, (0, 0))

    pausa = True

    while pausa:  # el ciclo del juego se mantiene mientras se este jugando
        pygame.mouse.set_visible(True)

        pygame.display.flip()

        dibujarTexto('presione SPACE para continuar...', fuente, pantalla_pausa, (ANCHOVENTANA/3, ALTOVENTANA/2), NEGRO)

        dibujarTexto('ESC para salir', fuente_chica, pantalla_pausa, (10, 10), NEGRO)

        for evento in pygame.event.get():

            if evento.type == QUIT:
                terminar()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:
                    terminar()

                if evento.key == pygame.K_SPACE:
                    pausa = False

def decorar_mapa():

    for i in range(50):

        arbol_c_izq = Decoracion(arbol_chico, (random.randrange(80), random.randrange(800)))

        lista_decoracion.add(arbol_c_izq)

    for i in range(50):

        arbol_c_der = Decoracion(arbol_chico, (random.uniform(990, 1080), random.randrange(800)))

        lista_decoracion.add(arbol_c_der)

def verificar_creacion():

    ubicacion = pygame.mouse.get_pos()

    if ubicacion[0] < 100:
        pygame.mouse.set_pos(100, ubicacion[1])

    if ubicacion[0] > 960:
        pygame.mouse.set_pos(960, ubicacion[1])

# clases de tropas
class Jugador():

    def __init__(self, vida, poblacion, bando=True):
          self.vida = vida
          self.poblacion = poblacion
          self.bando = bando
          self.escuadron = 1

    def estado_vida(self):

          if self.bando == True:

              for tropa in tropas_player2:
                  if tropa.rect.y > ALTOVENTANA+20:
                      tropas_player2.remove(tropa)
                      self.vida -= 1
          else:

              for tropa in tropas_player1:
                  if tropa.rect.y < -20:
                      tropas_player1.remove(tropa)
                      self.vida -= 1

class Tropa(pygame.sprite.Sprite):

    def __init__(self, imagen_1, imagen_2, ubicacion, vida, velocidad, bando =True):
          pygame.sprite.Sprite.__init__(self)
          self.bando = bando
          self.image = imagen_1
          self.image_1 = imagen_1
          self.image_2 = imagen_2
          self.rect = self.image.get_rect()
          self.rect.x = ubicacion[0]
          self.ubicacion = self.rect
          self.frame = 1
          self.delay_frame = 0
          self.rect.y = ALTOVENTANA-1
          self.vida = vida
          self.velocidad = velocidad

          if self.bando == False:
              self.rect.x = random.uniform(80, 990)
              self.rect.y = 0

          if self.bando == True:
              for tropa in tropas_player1:
                  if self.rect.colliderect(tropa) == True:
                      self.rect.move_ip(0, 64)
          else:
              for tropa in tropas_player2:
                  if self.rect.colliderect(tropa) == True:
                      self.rect.move_ip(0, -64)

    def update(self):

      if self.bando == True:
          self.rect.y -= self.velocidad
          self.delay_frame += 1

          if self.delay_frame == 10:

              if self.frame == 1:
                self.ubicacion = self.rect
                self.image = self.image_2
                self.rect = self.image.get_rect()
                self.rect = self.ubicacion
                self.frame = 2
              else:
                self.ubicacion = self.rect
                self.image = self.image_1
                self.rect = self.image.get_rect()
                self.rect = self.ubicacion
                self.frame = 1

              self.delay_frame = 0
      else:
         self.rect.y += self.velocidad
         self.delay_frame += 1

         if self.delay_frame == 10:
             if self.frame == 1:
                 self.ubicacion = self.rect
                 self.image = self.image_2
                 self.rect = self.image.get_rect()
                 self.rect = self.ubicacion
                 self.frame = 2
             else:
                 self.ubicacion = self.rect
                 self.image = self.image_1
                 self.rect = self.image.get_rect()
                 self.rect = self.ubicacion
                 self.frame = 1

             self.delay_frame = 0

class Soldado(Tropa):

    def __init__(self, imagen_1, imagen_2, bando):
        Tropa.__init__(self, imagen_1, imagen_2, pygame.mouse.get_pos(), 20, 3, bando)

class Arquero(Tropa):

    def __init__(self, imagen_1, imagen_2, bando):
        Tropa.__init__(self, imagen_1, imagen_2, pygame.mouse.get_pos(), 10, 1, bando)

class Lancero(Tropa):

    def __init__(self, imagen_1, imagen_2, bando):
        Tropa.__init__(self, imagen_1, imagen_2, pygame.mouse.get_pos(), 15, 5, bando)

class Monje(Tropa):

    def __init__(self, imagen_1, imagen_2, bando):
        Tropa.__init__(self, imagen_1, imagen_2, pygame.mouse.get_pos(), 10, 1, bando)

class Cazador(Tropa):

    def __init__(self, imagen_1, imagen_2, bando):
        Tropa.__init__(self, imagen_1, imagen_2, pygame.mouse.get_pos(), 15, 3, bando)

class Gladiador(Tropa):

    def __init__(self, imagen_1, imagen_2, bando):
        Tropa.__init__(self, imagen_1, imagen_2, pygame.mouse.get_pos(), 30, 2, bando)

class Decoracion(pygame.sprite.Sprite):

    def __init__(self, imagen, ubicacion):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.x = ubicacion[0]
        self.rect.y = ubicacion[1]

# creo los dos bandos

tropas_player1 = pygame.sprite.Group()

tropas_player2 = pygame.sprite.Group()

# creo las decoracion del mapa

casas = pygame.sprite.Group()

indicadores = pygame.sprite.Group()

lista_decoracion  = pygame.sprite.Group()

# cargo las imagenes de cada tipo de tropa
soldado_atras1 = cargar_imagen('imagenes/soldado-atras1.png', True)

soldado_atras2 = cargar_imagen('imagenes/soldado-atras2.png', True)

soldado_frente1 = cargar_imagen('imagenes/soldado-frente1.png', True)

soldado_frente2 = cargar_imagen('imagenes/soldado-frente2.png', True)

arquero_atras1 = cargar_imagen('imagenes/arquero-atras1.png', True)

arquero_atras2 = cargar_imagen('imagenes/arquero-atras2.png', True)

arquero_frente1 = cargar_imagen('imagenes/arquero-frente1.png', True)

arquero_frente2 = cargar_imagen('imagenes/arquero-frente2.png', True)

lancero_atras1 = cargar_imagen('imagenes/lancero-atras1.png', True)

lancero_atras2 = cargar_imagen('imagenes/lancero-atras2.png', True)

lancero_frente1 = cargar_imagen('imagenes/lancero-frente1.png', True)

lancero_frente2 = cargar_imagen('imagenes/lancero-frente2.png', True)

monje_atras1 = cargar_imagen('imagenes/monje-atras1.png', True)

monje_atras2 = cargar_imagen('imagenes/monje-atras2.png', True)

monje_frente1 = cargar_imagen('imagenes/monje-frente1.png', True)

monje_frente2 = cargar_imagen('imagenes/monje-frente2.png', True)

cazador_atras1 = cargar_imagen('imagenes/cazador-atras1.png', True)

cazador_atras2 = cargar_imagen('imagenes/cazador-atras2.png', True)

cazador_frente1 = cargar_imagen('imagenes/cazador-frente1.png', True)

cazador_frente2 = cargar_imagen('imagenes/cazador-frente2.png', True)

gladiador_atras1 = cargar_imagen('imagenes/gladiador-atras1.png', True)

gladiador_atras2 = cargar_imagen('imagenes/gladiador-atras2.png', True)

gladiador_frente1 = cargar_imagen('imagenes/gladiador-frente1.png', True)

gladiador_frente2 = cargar_imagen('imagenes/gladiador-frente2.png', True)

castillo = cargar_imagen('imagenes/castillo.png', True)

arbol_chico = cargar_imagen('imagenes/arbol-chico.png', True)

papiro = cargar_imagen('imagenes/papiro.png', True)

papiro_castillo = pygame.transform.smoothscale(papiro,(130, 90))

papiro_poblacion = pygame.transform.smoothscale(papiro,(115, 70))

# establece un pygame, la ventana y el cursor del raton

pygame.init()

relojPrincipal = pygame.time.Clock()

pantalla = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA))

pygame.display.set_caption('Wars and Lords')

# establece las fuentes

fuente = pygame.font.SysFont(None, 48)

fuente_chica = pygame.font.SysFont(None, 32)

# establece los sonidos



while True:

# establece el comienzo del juego

    pygame.init()

    fondo = cargar_imagen('imagenes/pared.jpg')

    fondo = pygame.transform.scale(fondo,(ANCHOVENTANA, ALTOVENTANA))

    pantalla.blit(fondo, (0, 0))

    player_1 = Jugador(50, 100, True)

    player_2 = Jugador(50, 100, False)

    casa1 = Decoracion(castillo, (ANCHOVENTANA- 70, 0))

    casa2 = Decoracion(castillo, (10, (ALTOVENTANA-70)))

    papiro_castillo1 = Decoracion(papiro_castillo, (0,(ALTOVENTANA-80)))

    papiro_castillo2 = Decoracion(papiro_castillo, (950,-10))

    papiro_poblacion1 = Decoracion(papiro_poblacion, (960,(ALTOVENTANA-70)))

    papiro_poblacion2 = Decoracion(papiro_poblacion, (0,0))

    indicadores.add(papiro_castillo1)

    indicadores.add(papiro_castillo2)

    indicadores.add(papiro_poblacion1)

    indicadores.add(papiro_poblacion2)

    casas.add(casa1)

    casas.add(casa2)

    nueva_partida()
