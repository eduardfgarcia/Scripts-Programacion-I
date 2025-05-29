# Programacion del juego de la nave
import pygame
from pygame.locals import *
import time
import random
import ventanaPrincipal # Asegúrate de que este módulo exista
import pyttsx3 # Asegúrate de que esto esté instalado si lo usas para voz
import estadisticas # Asegúrate de que este módulo exista y contenga la lógica de guardado

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\Proyecto POO - Juego de la Nave\assets\player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.corazones = 10
        self.height, self.width = 700, 1000
        self.rect.center = (self.width // 2, self.height // 2)
        self.rect.bottom = (self.height - 20)
        self.speed = 600
        self.vx = 0.0
        self.vy = 0.0
        self.ax = 0.0
        self.ay = 0.0
      
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.ax = -self.speed
        elif keys[pygame.K_RIGHT] or keys[K_d]:
            self.ax = self.speed
        else:
            self.ax = 0

        if keys[pygame.K_UP] or keys[K_w]:
            self.ay = -self.speed
        elif keys[pygame.K_DOWN] or keys[K_s]:
            self.ay = self.speed
        else:
            self.ay = 0

        self.vx += self.ax * dt
        self.vy += self.ay * dt
        self.rect.x += self.vx * dt
        self.rect.y += self.vy * dt
        
        if self.rect.left < 0:
            self.rect.left = 0
            self.vx = 0
        if self.rect.right > self.width:
            self.rect.right = self.width
            self.vx = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.vy = 0
        if self.rect.bottom > self.height:
            self.rect.bottom = self.height
            self.vy = 0
        # print(f"Coordenadas de la nave: {self.rect.x, self.rect.y}") # Descomenta si necesitas depurar

class Asteroides(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\Proyecto POO - Juego de la Nave\assets\meteorGrey_big4.png").convert_alpha()
        self.image2 = pygame.image.load(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\Proyecto POO - Juego de la Nave\assets\meteorGrey_small1.png").convert_alpha()
        self.image3 = pygame.image.load(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\Proyecto POO - Juego de la Nave\assets\meteorGrey_tiny1.png")
        self.image4 = pygame.image.load(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\Proyecto POO - Juego de la Nave\assets\meteorGrey_tiny2.png")
        self.original = random.choice([self.image1, self.image2,self.image3,self.image4])
        self.tamañoRandomAsteroides = random.randint(30,100) # Ajusta el rango para que los asteroides no sean enormes
        self.image = pygame.transform.scale(self.original, (self.tamañoRandomAsteroides, self.tamañoRandomAsteroides))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1000 - self.rect.width) # Asegura que no se salgan al nacer
        self.rect.y = random.randint(-100, -20) 
        self.speed = random.randint(100, 200) 
        self.rotation = 0
        self.rotation_speed = random.randint(-5, 5)
        if self.rotation_speed == 0:
            self.rotation_speed = 1 if random.random() > 0.5 else -1
        
    def update(self, dt):
        self.rect.y += self.speed * dt
        self.rotation += self.rotation_speed * dt * 100
        self.rotation %= 360 # Mantiene el ángulo entre 0 y 359
        self.image = pygame.transform.rotate(self.original, self.rotation)
        self.image = pygame.transform.scale(self.image, (self.tamañoRandomAsteroides, self.tamañoRandomAsteroides)) # Re-escalar después de rotar
        self.rect = self.image.get_rect(center = self.rect.center) # Mantener el centro al rotar
        
        if self.rect.top > 700:
            self.rect.x = random.randint(0, 1000 - self.rect.width)
            self.rect.y = random.randint(-100, -20)
            self.speed = random.randint(200, 600)
            self.rotation_speed = random.randint(-5, 5) # Reiniciar velocidad de rotación
            if self.rotation_speed == 0:
                self.rotation_speed = 1 if random.random() > 0.5 else -1

class AtaqueLaser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((7,30))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x        
        self.rect.bottom = y 
        self.speed = 13

    def update(self, dt):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

class JuegoDeNave:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        self.size = 1000, 700
        self.width, self.height = self.size
        self.backgraundImage = pygame.image.load(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\Proyecto POO - Juego de la Nave\assets\background.png")
        self.backgraundImage = pygame.transform.scale(self.backgraundImage, (self.width, self.height))
        self.rectImage = self.backgraundImage.get_rect()
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.title = pygame.display.set_caption("Juego de Nave")
        
        self.font = pygame.font.Font(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\Proyecto POO - Juego de la Nave\assets\game_of_squids\Game Of Squids.ttf", 36)
        
        self.puntuacion = 0
        self.textPuntuacion = self.font.render(f"Puntuacion: {self.puntuacion}", True, (255, 255, 255))
        self.rectTextPuntuacion = self.textPuntuacion.get_rect()
        self.rectTextPuntuacion.topleft = (10, 10)
        self.engine = True
        #self.music = pygame.mixer.music.load(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion I -204 - Segundo Semestre\game\juegodeNave\assets\music.ogg")
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.asteroids = pygame.sprite.Group()
        self.lasers = pygame.sprite.Group()
        self.last_shot_time = time.time()
        self.shoot_delay = 0.2
        self.sonidoLaser = pygame.mixer.Sound(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\Proyecto POO - Juego de la Nave\assets\laser5.ogg")
        self.sonidoDestruccion = pygame.mixer.Sound(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\Proyecto POO - Juego de la Nave\assets\destruccionMeteoro.wav")
        self.botonRegresar = pygame.Rect(0, 0, 200, 50)
        self.botonRegresar.width = self.width // 2
        self.botonRegresar.height = 50
        self.botonRegresar.topright = (self.width - 10, 10)
        self.botonRegresarText = self.font.render("Regresar", True, (0, 0, 0))
        self.rectBotonRegresarText = self.botonRegresarText.get_rect(center = (self.botonRegresar.center))
        self.ColorBotonRegresar = (255,255,255)
        self.pocisionOriginal = self.botonRegresar.copy()
        self.animationProgress = 0.0
        self.animationSpeed = 8.0
        self.animationTarget = 7
        self.hoverButton = True
        self.sonidoMeteoro = pygame.mixer.Sound(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\Proyecto POO - Juego de la Nave\assets\Efecto colision.wav")
        self.sonidoLoser = pygame.mixer.Sound(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\Proyecto POO - Juego de la Nave\assets\gameOverSound.wav")
        self.textHightHp = pygame.font.Font(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\Proyecto POO - Juego de la Nave\assets\game_of_squids\Game Of Squids.ttf", 16)
        self.textSaludHP = self.textHightHp.render("HP", True, (255,255,255))
        self.vida_maxima = 10
        self.barra_ancho = 200
        self.barra_alto = 20
        self.barra_x = 10
        self.barra_y = 70
        self.rectTextSaludHP = self.textSaludHP.get_rect()
        self.rectTextSaludHP.midleft = (self.barra_x + self.barra_ancho + 15, self.barra_y + self.barra_alto // 2)
        # Texto de instrucciones en el pie de la ventana
        self.fontInstrucciones = pygame.font.Font(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\Proyecto POO - Juego de la Nave\assets\game_of_squids\Game Of Squids.ttf", 18)
        self.textoInstrucciones = self.fontInstrucciones.render(
            "Mover: WASD o Flechas  |  Disparar: Espacio o Click Izquierdo", True, (255, 255, 255)
        )
        self.rectTextoInstrucciones = self.textoInstrucciones.get_rect()
        self.rectTextoInstrucciones.midbottom = (self.width // 2, self.height - 10)
    
        #self.menuPrincipal = ventanaPrincipal.lobby()

    def ejecutar(self):
        #self.menuPrincipal.musica.stop() 
        #pygame.mixer.music.play(-1) # Reproducir música del juego en bucle
        
        self.player.corazones = 10 # Reiniciar corazones al iniciar el juego
        self.puntuacion = 0 
        
        # Limpieza de datos (re-crea los grupos para asegurar que estén vacíos)
        self.all_sprites = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.lasers = pygame.sprite.Group()
        self.all_sprites.add(self.player) # Añadir el jugador de nuevo
        
        running = True
        current_game_state = "playing" # 'playing', 'game_over', 'quit', 'main_menu'

        lastTime = time.time() # Inicializar lastTime correctamente
        
        while running:
            dt = time.time() - lastTime # Calcular dt al inicio del bucle
            lastTime = time.time()
            pos_raton = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    current_game_state = "quit"
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.botonRegresar.collidepoint(event.pos):
                        running = False
                        current_game_state = "main_menu" # Cambiar estado para volver al menú
                    
                    # Manejo de disparo con click (si no es con barra espaciadora)
                    if event.button == 1 and self.rectImage.collidepoint(event.pos): # Botón izquierdo del ratón
                        current_time = time.time()
                        if current_time - self.last_shot_time > self.shoot_delay:
                            self.sonidoLaser.play()
                            laser = AtaqueLaser(self.player.rect.centerx, self.player.rect.top)
                            self.all_sprites.add(laser)
                            self.lasers.add(laser)
                            self.last_shot_time = current_time

                if event.type == pygame.MOUSEMOTION:
                    if self.botonRegresar.collidepoint(pos_raton):
                        self.hoverButton = True
                    else: self.hoverButton = False
                    
            keys = pygame.key.get_pressed()
            
            # Disparo con barra espaciadora (si es preferido)
            if keys[pygame.K_SPACE]:
                current_time = time.time()
                if current_time - self.last_shot_time > self.shoot_delay:
                    self.sonidoLaser.play()
                    laser = AtaqueLaser(self.player.rect.centerx, self.player.rect.top)
                    self.all_sprites.add(laser)
                    self.lasers.add(laser)
                    self.last_shot_time = current_time

            # Animación independiente de botones
            if self.hoverButton:
                self.ColorBotonRegresar = (200,200,200)
                self.animationProgress = min(1.0, self.animationProgress + self.animationSpeed * dt)
            else: 
                self.animationProgress = max(0.0, self.animationProgress - self.animationSpeed * dt)
                self.ColorBotonRegresar = (255,255,255)
            offset = self.animationTarget * self.animationProgress
            self.botonRegresar.centery = int(self.pocisionOriginal.centery + offset)
            self.rectBotonRegresarText.center = self.botonRegresar.center
            
            # Generación de asteroides
            if random.randint(1, 100) < 2:
                self.asteroide = Asteroides()
                self.all_sprites.add(self.asteroide)
                self.asteroids.add(self.asteroide)
                
            self.all_sprites.update(dt)
            
            # Detección de colisiones láser-asteroide
            laser_collisions = pygame.sprite.groupcollide(self.lasers, self.asteroids, True, True)
            for hit in laser_collisions: 
                self.puntuacion += 10 # Puntos por cada asteroide
                self.textPuntuacion = self.font.render(f"Puntuacion: {self.puntuacion}", True, (255, 255, 255))
                self.sonidoDestruccion.play()

            self.clock.tick(120)
            self.screen.blit(self.backgraundImage,(0,0))
            self.screen.blit(self.textPuntuacion, self.rectTextPuntuacion)
            pygame.draw.rect(self.screen, self.ColorBotonRegresar, self.botonRegresar, border_radius=20)
            self.screen.blit(self.botonRegresarText, self.rectBotonRegresarText)
            self.screen.blit(self.textSaludHP,self.rectTextSaludHP)
            self.all_sprites.draw(self.screen)

            # Detección de colisiones nave-asteroide
            collisions = pygame.sprite.spritecollide(self.player, self.asteroids, True)
            for hit in collisions:
                self.sonidoMeteoro.play() # Reproducir sonido de colisión
                print("La nave fue golpeada")
                self.player.corazones -= 1
                print(f"Corazones restantes: {self.player.corazones}")
                if self.player.corazones <= 0:
                    pygame.mixer.music.stop() # Detener la música del juego
                    self.sonidoLoser.play()
                    lose_screen = gameOver(self.screen, self.puntuacion) # Pasar la puntuación
                    game_over_state = lose_screen.gameOver() # Captura el resultado de gameOver
                    
                    running = False # Sale del bucle de juego
                    current_game_state = game_over_state # Establece el estado final del juego
            
            # Mostrar instrucciones de controles en la parte inferior
            self.screen.blit(self.textoInstrucciones, self.rectTextoInstrucciones)
            # Dibujo barra de vida
            barra_actual = int(self.barra_ancho * (self.player.corazones / self.vida_maxima))
            pygame.draw.rect(self.screen, (100,100,100),(self.barra_x,self.barra_y,self.barra_ancho,self.barra_alto), border_radius = 10)
            pygame.draw.rect(self.screen, (255, 0, 0), (self.barra_x,self.barra_y, barra_actual, self.barra_alto), border_radius=10)
            
            pygame.display.flip()
        
        # Al salir del bucle de juego, retorna el estado para el bucle principal
        return current_game_state 

class gameOver:
    def __init__(self, screen, puntaje):
        self.screen = screen
        self.puntaje = puntaje # La puntuación de la partida actual
        self.width,self.height = 520,450
        self.window = pygame.Rect(0,0,self.width,self.height)
        self.window.center = self.screen.get_rect().center
        self.sonidoBotonConfirmacion = pygame.mixer.Sound(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\Proyecto POO - Juego de la Nave\assets\botonConfirmacion.wav")
        self.backgroundColor = (245, 183, 177)
        try:
            self.fontTitleGameOver = pygame.font.Font(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\Proyecto POO - Juego de la Nave\assets\game_of_squids\Game Of Squids.ttf", 36)
            self.fontButtons = pygame.font.Font(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\Proyecto POO - Juego de la Nave\assets\game_of_squids\Game Of Squids.ttf", 12)
        except FileNotFoundError:
            print("Advertencia: No se encontró la fuente personalizada para Game Over. Usando fuente predeterminada.")
            self.fontTitleGameOver = pygame.font.SysFont("arial", 36, bold=True)
            self.fontButtons = pygame.font.SysFont("arial", 12, bold=True)
            
        self.textGameOver = self.fontTitleGameOver.render("Has perdido!",True,(10,10,10))
        self.rectTextGameOver = self.textGameOver.get_rect(center = self.window.center)
    
        self.botonDejarDatos = pygame.Rect(0,0,200,50)
        self.botonDejarDatos.left = self.window.left + 36
        self.botonDejarDatos.top = self.rectTextGameOver.bottom + 30
        self.textSurface = self.fontButtons.render("Deja tus datos",True,(10,10,10))
        self.textSurfaceRect = self.textSurface.get_rect(center = self.botonDejarDatos.center)
        
        self.botonSalir = pygame.Rect(0, 0, 40, 40)
        self.botonSalir.topright = (self.window.right - 10, self.window.top + 10)
        self.textSalir = self.fontButtons.render("X", True, (255, 255, 255))
        self.rectTextSalir = self.textSalir.get_rect(center=self.botonSalir.center)
        
        self.botonReintentar = pygame.Rect(0, 0, 200, 50)
        self.botonReintentar.centery = self.botonDejarDatos.centery
        self.botonReintentar.left = self.botonDejarDatos.right + 20
        self.textReintentar = self.fontButtons.render("Reintentar", True, (10, 10, 10))
        self.rectTextReintentar = self.textReintentar.get_rect(center=self.botonReintentar.center)
        
        self.result = 'none' # Inicializar como 'none' para que el bucle inicial se ejecute
        
        # Variables para el input de nombre (inicializadas aquí para la primera vez)
        self.player_name = ""
        self.input_active = False
        self.input_rect = pygame.Rect(self.window.left + 36, self.botonDejarDatos.bottom + 5, 300, 40)
        self.input_color_inactive = pygame.Color('lightskyblue3')
        self.input_color_active = pygame.Color('dodgerblue2')
        self.current_input_color = self.input_color_inactive
        self.font_input = pygame.font.SysFont("arial", 32)
        
        self.botonConfirmar = pygame.Rect(0, 0, 150, 40)
        self.botonConfirmar.left = self.input_rect.right + 20
        self.botonConfirmar.centery = self.input_rect.centery
        self.textConfirmar = self.fontButtons.render("Confirmar", True, (10, 10, 10))
        self.rectTextConfirmar = self.textConfirmar.get_rect(center=self.botonConfirmar.center)
        
        self.data_saved_message = False 
        self.confirmar_text_surface = None
        self.confirmar_text_rect = None

    def gameOver(self):
        pygame.mixer.music.stop() 
        self.result = 'none' 
        self.showing_input_screen = False 
        self.data_saved_message = False
        self.player_name = "" 
        self.input_active = False 
        self.current_input_color = self.input_color_inactive

        while self.result == 'none':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.result = "quit"
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.botonSalir.collidepoint(event.pos):
                        self.result = "main_menu" # Retorna al menú principal
                        self.sonidoBotonConfirmacion.play()
                    elif self.botonReintentar.collidepoint(event.pos) and not self.showing_input_screen:
                        self.result = "reintentar" # Retorna para reiniciar el juego
                        self.sonidoBotonConfirmacion.play()
                    elif self.botonDejarDatos.collidepoint(event.pos) and not self.showing_input_screen:
                        self.sonidoBotonConfirmacion.play()
                        self.showing_input_screen = True # Activa la pantalla de input
                        self.player_name = "" # Resetear el nombre al entrar a la pantalla de input
                        self.input_active = True
                        self.current_input_color = self.input_color_active
                    
                    # Manejo de clics en la pantalla de input
                    if self.showing_input_screen:
                        if self.input_rect.collidepoint(event.pos):
                            self.input_active = not self.input_active
                        else:
                            self.input_active = False # Clic fuera del input lo desactiva
                        self.current_input_color = self.input_color_active if self.input_active else self.input_color_inactive
                        
                        if self.botonConfirmar.collidepoint(event.pos):
                            if self.player_name: # Solo guardar si hay un nombre
                                # Instanciar Estadisticas para guardar los datos
                                self.sonidoBotonConfirmacion.play()
                                stats_manager = estadisticas.Estadisticas()
                                stats_manager.guardar_estadistica(self.player_name, self.puntaje)
                                print(f"Nombre y puntuación guardados: {self.player_name}, {self.puntaje}")
                                
                                self.data_saved_message = True
                                self.confirmar_text_surface = self.fontButtons.render("Datos guardados con éxito!", True, (0, 255, 0))
                                self.confirmar_text_rect = self.confirmar_text_surface.get_rect()
                                self.confirmar_text_rect.midbottom = (self.window.centerx, self.window.bottom - 20)
                                self.showing_input_screen = False # Vuelve a la pantalla de Game Over normal
                                self.input_active = False # Asegura que el input no esté activo
                                
                if event.type == pygame.KEYDOWN:
                    if self.showing_input_screen and self.input_active:
                        if event.key == pygame.K_RETURN: # Tecla Enter
                            if self.player_name:
                                # Instanciar Estadisticas para guardar los datos
                                stats_manager = estadisticas.Estadisticas()
                                stats_manager.guardar_estadistica(self.player_name, self.puntaje)
                                print(f"Nombre y puntuación guardados: {self.player_name}, {self.puntaje}")
                                
                                self.data_saved_message = True
                                self.confirmar_text_surface = self.fontButtons.render("Datos guardados con éxito!", True, (0, 255, 0))
                                self.confirmar_text_rect = self.confirmar_text_surface.get_rect()
                                
                                self.confirmar_text_rect.midbottom = (self.window.centerx, self.window.bottom - 20)
                                self.showing_input_screen = False
                                self.input_active = False
                        elif event.key == pygame.K_BACKSPACE:
                            self.player_name = self.player_name[:-1]
                        else:
                            self.player_name += event.unicode

            # Dibujar la ventana de Game Over
            pygame.draw.rect(self.screen, self.backgroundColor, self.window, border_radius=20)
            
            # Siempre dibujar el mensaje de "Has perdido!" y el botón "X"
            self.screen.blit(self.textGameOver, self.rectTextGameOver)
            pygame.draw.rect(self.screen, (255,0,0), self.botonSalir, border_radius= 3)
            self.screen.blit(self.textSalir,self.rectTextSalir)
            
            if not self.showing_input_screen: # Si no estamos en la pantalla de input
                # Dibujar los botones "Deja tus datos" y "Reintentar"
                pygame.draw.rect(self.screen, (93, 173, 226), self.botonDejarDatos, border_radius = 10)
                pygame.draw.rect(self.screen, (46, 204, 113), self.botonReintentar, border_radius=10)
                self.screen.blit(self.textReintentar, self.rectTextReintentar)
                self.screen.blit(self.textSurface, self.textSurfaceRect) # Texto de "Deja tus datos"
            else: # Estamos en la pantalla de input
                self._draw_name_input_screen() # Llama a la función para dibujar la pantalla de input

            if self.data_saved_message: # Si el mensaje de guardado debe mostrarse
                self.screen.blit(self.confirmar_text_surface, self.confirmar_text_rect)

            pygame.display.flip()
            
        return self.result # Retorna el estado cuando se sale del bucle

    def _draw_name_input_screen(self):
        pygame.draw.rect(self.screen, self.current_input_color, self.input_rect, border_radius=10)
        pygame.draw.rect(self.screen, (0,0,0), self.input_rect, 2, border_radius=10) # Borde
        
        input_surface = self.font_input.render(self.player_name, True, (10, 10, 10))
        text_width = input_surface.get_width()
        if text_width > self.input_rect.width - 20:
            self.screen.blit(input_surface, (self.input_rect.x + 10 + (self.input_rect.width - 20 - text_width), self.input_rect.y + 5))
        else:
            self.screen.blit(input_surface, (self.input_rect.x + 10, self.input_rect.y + 5))
        
        pygame.draw.rect(self.screen, (150, 250, 150), self.botonConfirmar, border_radius=10) # Un verde más claro
        self.screen.blit(self.textConfirmar, self.rectTextConfirmar)

