# Estudiantes:
# EDUARD FERNANDO GARCIA NIÑO
# EDDU SEBASTIAN GOMEZ VEGA
# CADI:
# Programacion I 

# Ejecutable
# Menu Principal del Juego de la Nave 
import pygame
from pygame.locals import *
from PIL import Image
import time
from juegoNave import *
import juegoNave
import creditos
import estadisticas
class lobby:
    # Variables iniciales 
    # Tamaño de la ventana
    # Interfaz inicial: Botonoes y carga de textos
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        self.white = (255, 255, 255)
        self.size = 1000, 700
        self.width, self.height = self.size
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.title = pygame.display.set_caption("Juego de Nave")
        self.git_frame, self.duration = self.cargar_frames_gif(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\juegodeNave\assets\1749ea089c2bb9cc69761c267628c6fb.gif")
        self.font = pygame.font.Font(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\juegodeNave\assets\game_of_squids\Game Of Squids.ttf", 36)
        self.sonidoBotonConfirmacion = pygame.mixer.Sound(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\juegodeNave\assets\botonConfirmacion.wav")
        self.rects = []
        self.texts = []
        self.original_rects = [] 
        self.hovered_button = -1 
        self.animation_progress = [0.0] * 5 
        self.animation_speed = 5.0 
        self.target_offset = 20 
        # Lista de textos y botones a crear
        self.text_strings = [
            "< JUEGO DE LA NAVE >",
            "JUGAR",
            "ESTADISTICAS",
            "CREDITOS",
            "SALIR"
        ]
        y = 100
        button_width = self.width // 2
        button_height = 50
        # Iterecion y renderizacion de botones
        for i, t in enumerate(self.text_strings):
            text_surface = self.font.render(t, True, self.white)
            if i in [1, 2, 3, 4]:
                rect = pygame.Rect(0, 0, button_width, button_height)
                rect.center = (self.width / 2, y)
                rect.top = rect.bottom + 50
            else:
                rect = text_surface.get_rect(center=(self.width // 2, y))
                rect.top = rect.bottom + 20
            self.texts.append(text_surface)
            self.rects.append(rect.copy()) # Guardar una copia inicial
            self.original_rects.append(rect.copy())
            y += 70
        self.button_colors = [(30, 144, 255)] * len(self.rects)  # Color normal
        self.button_hover_color = (100, 181, 246)  # Color al pasar el mouse
        self.button_down_color = (255, 200, 0)  # Color al presionar
        self.button_pressed = [False] * len(self.rects) # Estado de los botones a modificar
    
    # Carga de imagenes Frame por Frame
    def cargar_frames_gif(self, ruta_gif):
        gif = Image.open(ruta_gif)
        frames = []
        for i in range(gif.n_frames):
            gif.seek(i)
            frame_pil = gif.convert("RGBA")
            frame_pygame = pygame.image.fromstring(frame_pil.tobytes(), frame_pil.size, frame_pil.mode)
            frames.append(frame_pygame)
        return frames, gif.info.get('duration', 100) / 1000.0
    
    # Dibujo de objetos de las vetnana
    def dibujarVentana(self):
        background = (0, 0, 0)
        currentFrame = 0
        animationFrame = 0.0
        running = True
        self.last_time = time.time()
        while running:
            self.currentTime = time.time()
            dt = self.currentTime - self.last_time
            self.last_time = self.currentTime
            pos_raton = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                if event.type == MOUSEBUTTONDOWN:
                    for idx, rect in enumerate(self.rects):
                        if idx >= 1 and rect.collidepoint(event.pos):
                            self.button_colors[idx] = self.button_down_color
                            self.button_pressed[idx] = True

                # Eventos para inicializar los botones con sus respectivos modulos
                if event.type == MOUSEBUTTONUP:
                    for idx, rect in enumerate(self.rects):
                        if idx >= 1 and self.button_pressed[idx]:
                            self.button_pressed[idx] = False
                            if rect.collidepoint(pos_raton):
                                if idx == 1: # Juego Principal
                                    self.sonidoBotonConfirmacion.play()
                                    print("Ventana | JUGAR")
                                    juego = juegoNave.JuegoDeNave()
                                    juego.ejecutar()
                                elif idx == 2: # Ventana de Estadisticas
                                    self.sonidoBotonConfirmacion.play()
                                    print("Ventana | ESTADISTICAS")
                                    ventanaEstadisticas = estadisticas.Estadisticas()
                                    ventanaEstadisticas.ejecutar()
                                elif idx == 3: # Ventana de Creditos 
                                    self.sonidoBotonConfirmacion.play()
                                    print("Ventana | CREDITOS")
                                    ventanaCreditos = creditos.Creditos()
                                    ventanaCreditos.ejecutar()
                                elif idx == 4:  # Evento para Salir del programa
                                    self.sonidoBotonConfirmacion.play()
                                    print("Ventana | SALIR")
                                    pygame.quit()
                                    return
                            else:
                                self.button_colors[idx] = (30, 144, 255) # Volver a normal si se soltó fuera


                # Cambio de color de los botones y el estado de evento del mouse
                if event.type == MOUSEMOTION:
                    self.hovered_button = -1
                    for idx, rect in enumerate(self.rects):
                        if idx >= 1 and rect.collidepoint(pos_raton):
                            self.hovered_button = idx
                            break
                    for i in range(1, len(self.rects)):
                        if i == self.hovered_button and not self.button_pressed[i]:
                            self.button_colors[i] = self.button_hover_color
                        elif not self.button_pressed[i]:
                            self.button_colors[i] = (30, 144, 255)

            # Animación de los botones
            for i in range(1, len(self.rects)):
                if i == self.hovered_button:
                    self.animation_progress[i] = min(1.0, self.animation_progress[i] + self.animation_speed * dt)
                else:
                    self.animation_progress[i] = max(0.0, self.animation_progress[i] - self.animation_speed * dt)

                offset = self.target_offset * self.animation_progress[i]
                self.rects[i].centerx = int(self.original_rects[i].centerx + offset)

            # animacion de la ventana video
            self.screen.fill(background)
            if self.git_frame:
                frame = pygame.transform.scale(
                    self.git_frame[currentFrame], (self.width, self.height)
                )
                self.screen.blit(frame, (0, 0))
                animationFrame += dt
                if animationFrame >= self.duration:
                    currentFrame += 1
                    if currentFrame >= len(self.git_frame):
                        currentFrame = 0
                    animationFrame = 0.0

            # Iterar y mostrar en pantalla los respectivos objetos creados
            for i, (text, rect) in enumerate(zip(self.text_strings, self.rects)):
                if i in [1, 2, 3, 4]:
                    pygame.draw.rect(self.screen, self.button_colors[i], rect, border_radius=20)
                    text_surface = self.font.render(text, True, self.white)
                    text_rect = text_surface.get_rect(center=rect.center)
                    self.screen.blit(text_surface, text_rect)
                else:
                    pygame.draw.rect(self.screen, (0,255,0), rect, border_radius=20)
                    text_surface = self.font.render(text, True, self.white)
                    text_rect = text_surface.get_rect(center=rect.center)
                    self.screen.blit(text_surface, text_rect)

            self.clock.tick(60)
            pygame.display.flip()

if __name__ == "__main__":
    ventanaJuego = lobby()
    ventanaJuego.dibujarVentana()