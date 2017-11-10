import pygame, sys, random

from pygame.locals import *

# variables globales

ANCHOVENTANA = 1080

ALTOVENTANA = 800

NEGRO = (0, 0, 0)

BLANCO = (255, 255, 255)

MARRON = (40, 5, 0)

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

def crear_enemigos(probabilidad, posicion_mause):

    if probabilidad == 0:

        probabilidad = 3

    opcion = random.randrange(400/probabilidad)

    if opcion == 1:

       boton_soldado_p2.crear(posicion_mause)

    if opcion == 2:

       boton_arquero_p2.crear(posicion_mause)

    if opcion == 3:

       boton_lancero_p2.crear(posicion_mause)

    if opcion == 4:

       boton_monje_p2.crear(posicion_mause)

    if opcion == 5:

       boton_cazador_p2.crear(posicion_mause)

    if opcion == 6:

       boton_gladiador_p2.crear(posicion_mause)

def colision_batalla():

    espada_1 = pygame.mixer.Sound("sonidos/espada1.wav")

    espada_2 = pygame.mixer.Sound("sonidos/espada2.wav")

    golpe_hierro = pygame.mixer.Sound("sonidos/golpe-hierro.wav")

    flecha_golpe = pygame.mixer.Sound("sonidos/flecha-golpe.wav")

    sonido_trampa = pygame.mixer.Sound("sonidos/trampa.wav")

    for tropa_p1 in tropas_player1:

        for tropa_p2 in tropas_player2:

            if tropa_p1.rect.colliderect(tropa_p2) == True:

                efectos = random.randrange(100)

                if tropa_p1.disparar() == 'flecha':
                   flecha_golpe.play()
                   efectos = 0

                if efectos != 0:
                    if efectos < 10:
                      espada_1.play()
                    if efectos > 90:
                      espada_2.play()
                    if efectos > 45 and efectos < 50:
                      golpe_hierro.play()

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

    for tropa in tropas_player1:

        for trampa in trampas:

            if tropa.rect.colliderect(trampa) == True:

                trampas.remove(trampa)

                sonido_trampa.play()

                tropa.vida -= 10

                tropa.rect.move_ip(0, 16)

                if tropa.vida <= 0:

                    tropas_player1.remove(tropa)

    for tropa in tropas_player2:

        for trampa in trampas:

            if tropa.rect.colliderect(trampa) == True:

                trampas.remove(trampa)

                sonido_trampa.play()

                tropa.vida -= 10

                tropa.rect.move_ip(0, -16)

                if tropa.vida <= 0:
                    tropas_player2.remove(tropa)

def nueva_partida(dificultad):

    limpiar()

    decorar_mapa()

    pygame.mixer.music.load("sonidos/tambor-ambiente.wav")

    pygame.mixer.music.play(-1)

    if dificultad == 1:

        player_1.poblacion = 200

        player_1.vida = 50

        player_2.poblacion = 200

        player_2.vida = 50

    if dificultad == 2:

        player_1.poblacion = 300

        player_1.vida = 40

        player_2.poblacion = 300

        player_2.vida = 40

    if dificultad == 3:

        player_1.poblacion = 500

        player_1.vida = 30

        player_2.poblacion = 500

        player_2.vida = 30

    while True:  # el ciclo del juego se mantiene mientras se este jugando

        pygame.mouse.set_visible(False)

        pygame.display.flip()

        relojPrincipal.tick(FPS)

        verificar_creacion()

        for evento in pygame.event.get():

            if evento.type == QUIT:
                terminar()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:

                    pygame.mixer.music.stop()

                    pausa()

                boton_soldado.update(evento, dificultad*2, pygame.mouse.get_pos())

                boton_arquero.update(evento, dificultad*2, pygame.mouse.get_pos())

                boton_lancero.update(evento, dificultad*2, pygame.mouse.get_pos())

                boton_monje.update(evento, dificultad*2, pygame.mouse.get_pos())

                boton_cazador.update(evento, dificultad*2, pygame.mouse.get_pos())

                boton_gladiador.update(evento, dificultad*2, pygame.mouse.get_pos())

        crear_enemigos(dificultad*5, (random.uniform(80, 990), 0))

        pantalla.blit(fondo, (0, 0))

        colision_batalla()

        trampas.draw(pantalla)

        tropas_player2.draw(pantalla)

        tropas_player1.draw(pantalla)

        # genero ambientacion

        lista_decoracion.draw(pantalla)

        indicadores.draw(pantalla)

        casas.draw(pantalla)

        botones.draw(pantalla)

        avisos.draw(pantalla)

        # actualizo la posicion de las tropas

        tropas_player2.update()

        tropas_player1.update()

        avisos.update(pygame.mouse.get_pos())

        for tropa in tropas_player1:

            tropa.disparar()

        for tropa in tropas_player2:

            tropa.disparar()

        dibujarTexto(str(player_1.vida), fuente, pantalla, (70, ALTOVENTANA - 55), NEGRO)

        dibujarTexto(str(player_2.vida), fuente, pantalla, ((ANCHOVENTANA - 115), 15), NEGRO)

        dibujarTexto(str(player_1.poblacion), fuente, pantalla, (985, ALTOVENTANA - 60), NEGRO)

        dibujarTexto(str(player_2.poblacion), fuente, pantalla, (25, 10), NEGRO)

        boton_soldado.actulizar_reloj()

        boton_arquero.actulizar_reloj()

        boton_lancero.actulizar_reloj()

        boton_monje.actulizar_reloj()

        boton_cazador.actulizar_reloj()

        boton_gladiador.actulizar_reloj()

        boton_soldado_p2.actulizar_reloj()

        boton_arquero_p2.actulizar_reloj()

        boton_lancero_p2.actulizar_reloj()

        boton_monje_p2.actulizar_reloj()

        boton_cazador_p2.actulizar_reloj()

        boton_gladiador_p2.actulizar_reloj()

        # actualizo las vidas

        player_1.estado_vida()

        player_2.estado_vida()

        if player_1.vida <= 0 or player_2.vida <= 0:

            player_1.calcular_puntos()

            fin_partida()

def fin_partida():

    for cartel in carteles:
        carteles.remove(cartel)

    pygame.init()

    piedras.play()

    pantalla.blit(fondo, (0, 0))

    while True:

        pygame.display.flip()

        tropas_player1.draw(pantalla)

        tropas_player2.draw(pantalla)

        lista_decoracion.draw(pantalla)

        carteles.add(papiro_mensaje3)

        if player_1.vida <= 0:

            carteles.add(papiro_mensaje1)

            carteles.draw(pantalla)

            dibujarTexto('tu castillo ha caido', fuente, pantalla, (ANCHOVENTANA / 2, ALTOVENTANA / 2), MARRON)

        if player_2.vida <= 0:

            carteles.add(papiro_mensaje2)

            carteles.draw(pantalla)

            dibujarTexto('el castillo enemigo ha caido', fuente, pantalla, ((ANCHOVENTANA / 2) -30, ALTOVENTANA / 2), MARRON)

        dibujarTexto('[ESC]', fuente_chica, pantalla, (10, 13), MARRON)

        for evento in pygame.event.get():

            if evento.type == QUIT:
                terminar()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:

                    menu_pincipal()

def limpiar():

  for tropa in tropas_player1:
       tropas_player1.remove(tropa)

  for tropa in tropas_player2:
       tropas_player2.remove(tropa)

  for trampa in trampas:
       trampas.remove(trampa)

def menu_pincipal():

    pygame.init()

    pantalla_menu = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA))

    fondo_menu = cargar_imagen('imagenes/fondo-menu.jpg')

    fondo_menu = pygame.transform.scale(fondo_menu, (ANCHOVENTANA, ALTOVENTANA))

    pantalla_menu.blit(fondo_menu, (0, 0))

    trueno.play()

    pygame.mixer.music.load("sonidos/viento.wav")

    pygame.mixer.music.play(-1)

    salir = True

    while salir:

        pygame.mouse.set_visible(True)

        pygame.display.flip()

        dibujarTexto('presione [SPACE] para comenzar...', fuente, pantalla_menu, (ANCHOVENTANA/3, ALTOVENTANA/2), BLANCO)

        dibujarTexto('[ESC] para salir', fuente_chica, pantalla_menu, (10, 10), BLANCO)

        dibujarTexto('[TAB] para ayuda', fuente_chica, pantalla_menu, ((ANCHOVENTANA - 200), 10), BLANCO)

        for evento in pygame.event.get():

            if evento.type == QUIT:
                terminar()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:
                    terminar()

                if evento.key == pygame.K_SPACE:

                    salir = False

                    elegir_dificultad(fondo_menu)

                if evento.key == pygame.K_TAB:

                    ayuda()

def ayuda():

    pygame.init()

    pantalla_ayuda = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA))

    fondo_menu = cargar_imagen('imagenes/fondo-menu.jpg')

    fondo_menu = pygame.transform.scale(fondo_menu, (ANCHOVENTANA, ALTOVENTANA))

    pantalla_ayuda.blit(fondo_menu, (0, 0))

    trueno.play()

    pygame.mixer.music.load("sonidos/viento.wav")

    pygame.mixer.music.play(-1)

    salir = True

    while salir:

        pygame.mouse.set_visible(True)

        pygame.display.flip()

        dibujarTexto('[ESC] para salir', fuente_chica, pantalla_ayuda, (10, 10), BLANCO)

        dibujarTexto('Teclas:', fuente, pantalla_ayuda, (30, (ALTOVENTANA - 400)), BLANCO)

        dibujarTexto('[1] crear Soldado   (unidad estandar rapida de crear)', fuente_chica, pantalla_ayuda, (50 , (ALTOVENTANA - 350)), BLANCO)

        dibujarTexto('[2] crear Arquero  (unidad a distancia rapida)', fuente_chica, pantalla_ayuda,(50, (ALTOVENTANA - 320)), BLANCO)

        dibujarTexto('[3] crear Lancero   (unidad ligera)', fuente_chica, pantalla_ayuda,(50, (ALTOVENTANA - 290)), BLANCO)

        dibujarTexto('[4] crear Monje  (unidad distancia lenta)', fuente_chica, pantalla_ayuda,(50, (ALTOVENTANA - 260)), BLANCO)

        dibujarTexto('[5] crear Cazador   (unidad con habilidad de dejar trampas)', fuente_chica, pantalla_ayuda,(50, (ALTOVENTANA - 230)), BLANCO)

        dibujarTexto('[6] crear Gladiador   (unidad pesada lenta)', fuente_chica, pantalla_ayuda,(50, (ALTOVENTANA - 200)), BLANCO)

        dibujarTexto('Mouse:', fuente, pantalla_ayuda, (30, (ALTOVENTANA - 150)), BLANCO)

        dibujarTexto('usa el mouse para seleccionar en que linea salen las tropas', fuente_chica, pantalla_ayuda, (50, (ALTOVENTANA - 100)), BLANCO)

        dibujarTexto('el costo de poblacion de cada unidad', fuente_chica, pantalla_ayuda,((ANCHOVENTANA - 500), 100), BLANCO)

        dibujarTexto('es correspondiente a su numero asignado', fuente_chica, pantalla_ayuda, ((ANCHOVENTANA - 500), 130), BLANCO)

        for evento in pygame.event.get():

            if evento.type == QUIT:
                terminar()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:

                    menu_pincipal()

def elegir_dificultad(fondo):

    pantalla_dificultad = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA))

    pantalla_dificultad.blit(fondo, (0, 0))

    salir = True

    while salir:

        pygame.mouse.set_visible(True)

        pygame.display.flip()

        dibujarTexto('[ESC] para salir', fuente_chica, pantalla_dificultad, (10, 10), BLANCO)

        dibujarTexto('[1] Facil', fuente_chica, pantalla_dificultad, (700, 500), BLANCO)

        dibujarTexto('[2] Normal', fuente_chica, pantalla_dificultad, (700, 600), BLANCO)

        dibujarTexto('[3] Dificil', fuente_chica, pantalla_dificultad, (700, 700), BLANCO)

        dibujarTexto('Puntuaciones:', fuente_chica, pantalla_dificultad, (10, (ALTOVENTANA - 130)), BLANCO)

        dibujarTexto('- '+ str(player_1.max_puntuacion), fuente_chica, pantalla_dificultad, (10, (ALTOVENTANA - 100)), BLANCO)

        dibujarTexto('- '+ str(player_1.segunda_puntuacion), fuente_chica, pantalla_dificultad, (10, (ALTOVENTANA - 75)), BLANCO)

        dibujarTexto('- '+ str(player_1.tercer_puntuacion), fuente_chica, pantalla_dificultad, (10, (ALTOVENTANA - 50)), BLANCO)

        for evento in pygame.event.get():

            if evento.type == QUIT:
                terminar()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:
                    menu_pincipal()

                if evento.key == pygame.K_1:

                    nueva_partida(1)

                if evento.key == pygame.K_2:
                    nueva_partida(2)

                if evento.key == pygame.K_3:
                    nueva_partida(3)

def pausa():

    pygame.init()

    pantalla_pausa = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA))

    fondo_pausa = cargar_imagen('imagenes/lienzo.jpg')

    fondo_pausa = pygame.transform.scale(fondo_pausa, (ANCHOVENTANA, ALTOVENTANA))

    pantalla_pausa.blit(fondo_pausa, (0, 0))

    trueno.play()

    pygame.mixer.music.play(-1)

    pausa = True

    while pausa:

        pygame.mouse.set_visible(True)

        pygame.display.flip()

        dibujarTexto('presione [SPACE] para continuar...', fuente, pantalla_pausa, (ANCHOVENTANA/3, (ALTOVENTANA/2)+ 100), MARRON)

        dibujarTexto('[ESC] para salir', fuente_chica, pantalla_pausa, (10, 10), MARRON)

        for evento in pygame.event.get():

            if evento.type == QUIT:
                terminar()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:
                    menu_pincipal()

                if evento.key == pygame.K_SPACE:

                    pygame.mixer.music.stop()

                    pygame.mixer.music.load("sonidos/tambor-ambiente.wav")

                    pygame.mixer.music.play(-1)

                    pausa = False

def decorar_mapa():

    for deco in lista_decoracion:
        lista_decoracion.remove(deco)

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

    def __init__(self, bando=True):
          self.vida = 0
          self.poblacion = 0
          self.bando = bando
          self.max_puntuacion = 0
          self.segunda_puntuacion = 0
          self.tercer_puntuacion = 0

    def estado_vida(self):

          if self.bando == True:

              for tropa in tropas_player2:

                  if tropa.disparar() == True and tropa.rect.y >= ALTOVENTANA-10:
                      tropas_player2.remove(tropa)

                  if tropa.rect.y > ALTOVENTANA+20:
                      tropas_player2.remove(tropa)
                      self.vida -= 1
          else:

              for tropa in tropas_player1:

                  if tropa.disparar() == True and tropa.rect.y <= 10:
                      tropas_player1.remove(tropa)

                  if tropa.rect.y < -20:
                      tropas_player1.remove(tropa)
                      self.vida -= 1

    def calcular_puntos(self):

        puntos = (self.poblacion * player_2.poblacion) * self.vida

        if puntos >= self.tercer_puntuacion and puntos <= self.segunda_puntuacion:

                self.tercer_puntuacion = puntos

        if puntos >= self.segunda_puntuacion and puntos <= self.max_puntuacion:

            self.tercer_puntuacion = self.segunda_puntuacion

            self.segunda_puntuacion = puntos

        if puntos >= self.max_puntuacion:

            self.tercer_puntuacion = self.segunda_puntuacion

            self.segunda_puntuacion = self.max_puntuacion

            self.max_puntuacion = puntos

class Boton(pygame.sprite.Sprite):

    def __init__(self, imagen_encendido, imagen_apagado , ubicacion, delay, bando):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen_encendido
        self.encendido = imagen_encendido
        self.apagado = imagen_apagado
        self.trasparente = trasparente
        self.rect = self.image.get_rect()
        self.rect.x = ubicacion[0]
        self.rect.y = ubicacion[1]
        self.ubicacion = ubicacion
        self.reloj_boton = delay/ FPS
        self.contador_reloj = self.reloj_boton
        self.delay = delay
        self.contador_delay = 0
        self.activo = True
        self.bando = bando
        if self.bando == False:
            self.image = trasparente
            self.encendido = trasparente
            self.apagado = trasparente

    def actulizar_reloj(self):

        self.image = self.apagado
        self.rect = self.ubicacion

        if self.activo == False:

            if self.bando == True:

               dibujarTexto(str(self.contador_reloj), fuente_chica, pantalla, ((self.ubicacion[0]+45),(self.ubicacion[1]- 10)), NEGRO)

            self.contador_delay += 1

            if self.contador_delay % FPS == 0:

                self.contador_reloj -= 1

            if self.contador_reloj == 0:

                self.contador_reloj = self.reloj_boton

            if self.contador_delay == self.delay:

               self.activo = True

               self.contador_delay = 0
        else:
             self.image = self.encendido
             self.rect = self.ubicacion

    def crear(self, posicion_mause):

        None

class Boton_soldado(Boton):

    def __init__(self, bando):
        Boton.__init__(self, boton_1, boton_1_apagado, (360, (ALTOVENTANA-50)), 25, bando)

    def update(self, evento, dificultad, posicion_mause):

        if self.activo == True:

            if evento.key == pygame.K_1:

                player_1.poblacion -= 1

                if player_1.poblacion >= 0:

                    soldado = Soldado(soldado_atras1, soldado_atras2, True)

                    tropas_player1.add(soldado)

                    crear_enemigos(dificultad*10, posicion_mause)

                    self.activo = False

                else:
                    player_1.poblacion += 1

    def crear(self, posicion_mause):

        if self.activo == True:

            player_2.poblacion -= 1

            if player_2.poblacion >= 0:

                soldado_enemigo = Soldado(soldado_frente1, soldado_frente2, False)

                soldado_enemigo.rect.x = posicion_mause[0]

                tropas_player2.add(soldado_enemigo)

                self.activo = False

            else:
                player_2.poblacion += 1

class Boton_arquero(Boton):

    def __init__(self, bando):
        Boton.__init__(self, boton_2, boton_2_apagado, (420, (ALTOVENTANA-50)), 50, bando)

    def update(self, evento, dificultad, posicion_mause):

        if self.activo == True:

            if evento.key == pygame.K_2:

                player_1.poblacion -= 2

                if player_1.poblacion >= 0:

                    arquero = Arquero(arquero_atras1, arquero_atras2, True)

                    tropas_player1.add(arquero)

                    crear_enemigos(dificultad*10, posicion_mause)

                    self.activo = False

                else:
                    player_1.poblacion += 2

    def crear(self, posicion_mause):

        if self.activo == True:

            player_2.poblacion -= 2

            if player_2.poblacion >= 0:

                arquero_enemigo = Arquero(arquero_frente1, arquero_frente2, False)

                arquero_enemigo.rect.x = posicion_mause[0]

                tropas_player2.add(arquero_enemigo)

                self.activo = False

            else:
                player_2.poblacion += 2

class Boton_lancero(Boton):

    def __init__(self, bando):
        Boton.__init__(self, boton_3, boton_3_apagado, (480, (ALTOVENTANA-50)), 75, bando)

    def update(self, evento, dificultad, posicion_mause):

        if self.activo == True:

            if evento.key == pygame.K_3:

                player_1.poblacion -= 3

                if player_1.poblacion >= 0:

                    lancero = Lancero(lancero_atras1, lancero_atras2, True)

                    tropas_player1.add(lancero)

                    crear_enemigos(dificultad*10, posicion_mause)

                    self.activo = False

                else:
                    player_1.poblacion += 3

    def crear(self, posicion_mause):

        if self.activo == True:

            player_2.poblacion -= 3

            if player_2.poblacion >= 0:

                lancero_enemigo = Lancero(lancero_frente1, lancero_frente2, False)

                lancero_enemigo.rect.x = posicion_mause[0]

                tropas_player2.add(lancero_enemigo)

                self.activo = False

            else:
                player_2.poblacion += 3

class Boton_monje(Boton):

    def __init__(self, bando):
        Boton.__init__(self, boton_4, boton_4_apagado, (540, (ALTOVENTANA-50)), 100, bando)

    def update(self, evento, dificultad, pisicion_mause):

        if self.activo == True:

            if evento.key == pygame.K_4:

                player_1.poblacion -= 4

                if player_1.poblacion >= 0:

                    monje = Monje(monje_atras1, monje_atras2, True)

                    tropas_player1.add(monje)

                    crear_enemigos(dificultad*10, pisicion_mause)

                    self.activo = False

                else:
                    player_1.poblacion += 4

    def crear(self, posicion_mause):

        if self.activo == True:

            player_2.poblacion -= 4

            if player_2.poblacion >= 0:

                monje_enemigo = Monje(monje_frente1, monje_frente2, False)

                monje_enemigo.rect.x = posicion_mause[0]

                tropas_player2.add(monje_enemigo)

                self.activo = False

            else:
                player_2.poblacion += 4

class Boton_cazador(Boton):

    def __init__(self, bando):
        Boton.__init__(self, boton_5, boton_5_apagado, (600, (ALTOVENTANA-50)), 125, bando)

    def update(self, evento, dificultad, posicion_mause):

        if self.activo == True:

            if evento.key == pygame.K_5:

                player_1.poblacion -= 5

                if player_1.poblacion >= 0:

                    cazador = Cazador(cazador_atras1, cazador_atras2, True)

                    tropas_player1.add(cazador)

                    crear_enemigos(dificultad*10, posicion_mause)

                    self.activo = False

                else:
                    player_1.poblacion += 5

    def crear(self, posicion_mause):

        if self.activo == True:

            player_2.poblacion -= 5

            if player_2.poblacion >= 0:

                cazador_enemigo = Cazador(cazador_frente1, cazador_frente2, False)

                cazador_enemigo.rect.x = posicion_mause[0]

                tropas_player2.add(cazador_enemigo)

                self.activo = False

            else:
                player_2.poblacion += 5

class Boton_gladiador(Boton):

    def __init__(self, bando):
        Boton.__init__(self, boton_6, boton_6_apagado, (660, (ALTOVENTANA-50)), 150, bando)

    def update(self, evento, dificultad, posicion_mause):

         if self.activo == True:

             if evento.key == pygame.K_6:

                  player_1.poblacion -= 6

                  if player_1.poblacion >= 0:

                     gladiador = Gladiador(gladiador_atras1, gladiador_atras2, True)

                     tropas_player1.add(gladiador)

                     crear_enemigos(dificultad*10, posicion_mause)

                     self.activo = False

                  else:
                      player_1.poblacion += 6

    def crear(self, posicion_mause):

        if self.activo == True:

            player_2.poblacion -= 6

            if player_2.poblacion >= 0:

                gladiador_enemigo = Gladiador(gladiador_frente1, gladiador_frente2, False)

                gladiador_enemigo.rect.x = posicion_mause[0]

                tropas_player2.add(gladiador_enemigo)

                self.activo = False

            else:
                player_2.poblacion += 6

class Tropa(pygame.sprite.Sprite):

    def __init__(self, imagen_1, imagen_2, ubicacion, vida, velocidad, bando):
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

    def disparar(self):

        None

class Soldado(Tropa):

    def __init__(self, imagen_1, imagen_2, bando):
        Tropa.__init__(self, imagen_1, imagen_2, pygame.mouse.get_pos(), 20, 3, bando)

class Arquero(Tropa):

    def __init__(self, imagen_1, imagen_2, bando):
        Tropa.__init__(self, imagen_1, imagen_2, pygame.mouse.get_pos(), 4, 1, bando)
        self.delay_disparo = 100
        self.contador_disparo = 0
        if self.bando == True:
            self.disparo = flecha_arriba
        else:
            self.disparo = flecha_abajo

    def disparar(self):

        self.contador_disparo += 1

        if self.contador_disparo == self.delay_disparo:

            disparo = Disparo(self.disparo, ((self.ubicacion[0]+10), self.ubicacion[1]), 1, 8, self.bando)

            if self.bando == True:
              tropas_player1.add(disparo)
            else:
              tropas_player2.add(disparo)

            flecha_lanzada.play()

            self.contador_disparo = 0

class Lancero(Tropa):

    def __init__(self, imagen_1, imagen_2, bando):
        Tropa.__init__(self, imagen_1, imagen_2, pygame.mouse.get_pos(), 15, 5, bando)

class Monje(Tropa):

    def __init__(self, imagen_1, imagen_2, bando):
        Tropa.__init__(self, imagen_1, imagen_2, pygame.mouse.get_pos(), 10, 1, bando)
        self.delay_disparo = 400
        self.contador_disparo = 0
        self.disparo = bola_energia

    def disparar(self):

        self.contador_disparo += 1

        if self.contador_disparo == self.delay_disparo:

            disparo = Disparo(self.disparo, ((self.ubicacion[0]+10), self.ubicacion[1]), 10, 20, self.bando)

            if self.bando == True:
              tropas_player1.add(disparo)
            else:
              tropas_player2.add(disparo)

            bola_lanzada.play()

            self.contador_disparo = 0

class Cazador(Tropa):

    def __init__(self, imagen_1, imagen_2, bando):
        Tropa.__init__(self, imagen_1, imagen_2, pygame.mouse.get_pos(), 15, 3, bando)
        self.delay_trampa = 200
        self.contador_trampa = 0
        self.disparo = trampa

    def disparar(self):

        self.contador_trampa += 1

        if self.contador_trampa == self.delay_trampa:

            if self.bando == True:

                disparo = Disparo(self.disparo, ((self.ubicacion[0] + 10), self.ubicacion[1] + 54), 1, 0, self.bando, True)

                trampas.add(disparo)
            else:

                disparo = Disparo(self.disparo, ((self.ubicacion[0] - 10), self.ubicacion[1] - 60), 1, 0, self.bando, True)

                trampas.add(disparo)

            self.contador_trampa = 0

class Gladiador(Tropa):

    def __init__(self, imagen_1, imagen_2, bando):
        Tropa.__init__(self, imagen_1, imagen_2, pygame.mouse.get_pos(), 30, 2, bando)

class Disparo(pygame.sprite.Sprite):

    def __init__(self, imagen, ubicacion, vida, velocidad, bando, trampa= False):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.x = ubicacion[0]
        self.rect.y = ubicacion[1]
        self.vida = vida
        self.velocidad = velocidad
        self.bando = bando
        self.trampa = trampa
        if self.bando  == False:
            self.rect.y += 40

    def update(self):

        if self.bando == True:

            self.rect.y -= self.velocidad
        else:
            self.rect.y += self.velocidad

    def disparar(self):

       if self.trampa == False:
           return 'flecha'
       else:
           return 'trampa'

class Decoracion(pygame.sprite.Sprite):

    def __init__(self, imagen, ubicacion):
       pygame.sprite.Sprite.__init__(self)
       self.image = imagen
       self.rect = self.image.get_rect()
       self.rect.x = ubicacion[0]
       self.rect.y = ubicacion[1]

class Mouse(Decoracion):

    def __init__(self):
        Decoracion.__init__(self, mouse_indicador, (0,0))

    def update(self, mouse_ubicacion):

        self.rect.x = mouse_ubicacion[0]
        self.rect.y = ALTOVENTANA - 20

# creo los dos bandos

tropas_player1 = pygame.sprite.Group()

tropas_player2 = pygame.sprite.Group()

trampas = pygame.sprite.Group()

# creo las decoracion del mapa

avisos = pygame.sprite.Group()

carteles = pygame.sprite.Group()

casas = pygame.sprite.Group()

indicadores = pygame.sprite.Group()

lista_decoracion  = pygame.sprite.Group()

botones = pygame.sprite.Group()

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

boton_1 = cargar_imagen('imagenes/simbolo-soldado.png')

boton_1_apagado = cargar_imagen('imagenes/simbolo-soldado-apagado.png')

boton_2 = cargar_imagen('imagenes/simbolo-arquero.png')

boton_2_apagado = cargar_imagen('imagenes/simbolo-arquero-apagado.png')

boton_3 = cargar_imagen('imagenes/simbolo-lancero.png')

boton_3_apagado = cargar_imagen('imagenes/simbolo-lancero-apagado.png')

boton_4 = cargar_imagen('imagenes/simbolo-monje.png')

boton_4_apagado = cargar_imagen('imagenes/simbolo-monje-apagado.png')

boton_5 = cargar_imagen('imagenes/simbolo-cazador.png')

boton_5_apagado = cargar_imagen('imagenes/simbolo-cazador-apagado.png')

boton_6 = cargar_imagen('imagenes/simbolo-gladiador.png')

boton_6_apagado = cargar_imagen('imagenes/simbolo-gladiador-apagado.png')

castillo = cargar_imagen('imagenes/castillo.png', True)

trasparente = cargar_imagen('imagenes/simbolo-trasparente.png')

arbol_chico = cargar_imagen('imagenes/arbol-chico.png', True)

papiro = cargar_imagen('imagenes/papiro.png', True)

mouse_indicador = cargar_imagen('imagenes/indicador-mause.png', True)

mouse_indicador = pygame.transform.smoothscale(mouse_indicador,(40, 20))

flecha_arriba = cargar_imagen('imagenes/flecha-arriba.png', True)

flecha_arriba = pygame.transform.smoothscale(flecha_arriba,(10, 30))

flecha_abajo = cargar_imagen('imagenes/flecha-abajo.png', True)

flecha_abajo = pygame.transform.smoothscale(flecha_abajo,(10, 30))

bola_energia = cargar_imagen('imagenes/bola-energia.png', True)

bola_energia = pygame.transform.smoothscale(bola_energia,(20, 20))

trampa = cargar_imagen('imagenes/trampa.png', True)

trampa = pygame.transform.smoothscale(trampa,(20, 20))

trasparente = pygame.transform.smoothscale(trasparente,(50, 50))

boton_1 = pygame.transform.smoothscale(boton_1,(50, 50))

boton_1_apagado = pygame.transform.smoothscale(boton_1_apagado,(50, 50))

boton_2 = pygame.transform.smoothscale(boton_2,(50, 50))

boton_2_apagado = pygame.transform.smoothscale(boton_2_apagado,(50, 50))

boton_3 = pygame.transform.smoothscale(boton_3,(50, 50))

boton_3_apagado = pygame.transform.smoothscale(boton_3_apagado,(50, 50))

boton_4 = pygame.transform.smoothscale(boton_4,(50, 50))

boton_4_apagado = pygame.transform.smoothscale(boton_4_apagado,(50, 50))

boton_5 = pygame.transform.smoothscale(boton_5,(50, 50))

boton_5_apagado = pygame.transform.smoothscale(boton_5_apagado,(50, 50))

boton_6 = pygame.transform.smoothscale(boton_6,(50, 50))

boton_6_apagado = pygame.transform.smoothscale(boton_6_apagado,(50, 50))

papiro_castillo = pygame.transform.smoothscale(papiro,(130, 90))

papiro_poblacion = pygame.transform.smoothscale(papiro,(115, 70))

papiro_botones = pygame.transform.smoothscale(papiro,(460, 90))

papiro_cartel_1 = pygame.transform.smoothscale(papiro,(500, 90))

papiro_cartel_2 = pygame.transform.smoothscale(papiro,(550, 90))

papiro_cartel_3 = pygame.transform.smoothscale(papiro,(75, 50))

# establece un pygame, la ventana

pygame.init()

relojPrincipal = pygame.time.Clock()

pantalla = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA))

pygame.display.set_caption('Wars and Lords')

# establece las fuentes

fuente = pygame.font.SysFont('Segoe Print', 30)

fuente_chica = pygame.font.SysFont('Segoe Print', 20)

flecha_lanzada = pygame.mixer.Sound("sonidos/flecha-lanzada.wav")

bola_lanzada = pygame.mixer.Sound("sonidos/bola-lanzada.wav")

trueno = pygame.mixer.Sound("sonidos/truenos.wav")

piedras = pygame.mixer.Sound("sonidos/piedras.wav")

pygame.mixer.music.load("sonidos/viento.wav")

while True:

    pygame.init()

    pared = cargar_imagen('imagenes/pared.jpg')

    fondo = pygame.transform.scale(pared,(ANCHOVENTANA, ALTOVENTANA))

    player_1 = Jugador(True)

    player_2 = Jugador(False)

    casa1 = Decoracion(castillo, (ANCHOVENTANA- 70, 0))

    casa2 = Decoracion(castillo, (10, (ALTOVENTANA-70)))

    papiro_castillo1 = Decoracion(papiro_castillo, (0,(ALTOVENTANA-80)))

    papiro_castillo2 = Decoracion(papiro_castillo, (950,-10))

    papiro_poblacion1 = Decoracion(papiro_poblacion, (960,(ALTOVENTANA-70)))

    papiro_poblacion2 = Decoracion(papiro_poblacion, (0,0))

    papiro_boton1 = Decoracion(papiro_botones, (310, (ALTOVENTANA-70)))

    papiro_mensaje1 = Decoracion(papiro_cartel_1, (440, 385))

    papiro_mensaje2 = Decoracion(papiro_cartel_2, (440, 385))

    papiro_mensaje3 = Decoracion(papiro_cartel_3, (0, 5))

    # creo los botones del juego

    boton_soldado = Boton_soldado(True)

    boton_arquero = Boton_arquero(True)

    boton_lancero = Boton_lancero(True)

    boton_monje = Boton_monje(True)

    boton_cazador = Boton_cazador(True)

    boton_gladiador = Boton_gladiador(True)

    boton_soldado_p2 = Boton_soldado(False)

    boton_arquero_p2 = Boton_arquero(False)

    boton_lancero_p2 = Boton_lancero(False)

    boton_monje_p2 = Boton_monje(False)

    boton_cazador_p2 = Boton_cazador(False)

    boton_gladiador_p2 = Boton_gladiador(False)

    flecha_mouse = Mouse()

    # agrego los botones a los grupos

    botones.add(boton_soldado)

    botones.add(boton_arquero)

    botones.add(boton_lancero)

    botones.add(boton_monje)

    botones.add(boton_cazador)

    botones.add(boton_gladiador)

    indicadores.add(papiro_castillo1)

    indicadores.add(papiro_castillo2)

    indicadores.add(papiro_poblacion1)

    indicadores.add(papiro_poblacion2)

    indicadores.add(papiro_boton1)

    casas.add(casa1)

    casas.add(casa2)

    avisos.add(flecha_mouse)

    menu_pincipal()