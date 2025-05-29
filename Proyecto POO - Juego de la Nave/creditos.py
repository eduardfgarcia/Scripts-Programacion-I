# creditos.py
# Autor: [Tu Nombre/Equipo]
# Fecha: [Fecha de Creación/Modificación]
# Descripción: Módulo encargado de desplegar la ventana de créditos del juego.
#              Muestra información sobre los desarrolladores, herramientas y agradecimientos.

import pygame
from pygame.locals import *
# from PIL import Image # PIL/Pillow no parece usarse directamente aquí, podría eliminarse si no es necesaria.
import time
# from juegoNave import * # Importación global no recomendada, mejor importar específicamente lo necesario.
import ventanaPrincipal # Se utiliza para instanciar el menú principal al regresar.

class Creditos:
    #Clase que gestiona la visualización de la pantalla de créditos del juego.
    #Se encarga de inicializar los componentes de Pygame necesarios, cargar recursos,
    #manejar eventos y dibujar los elementos en pantalla.
    def __init__(self):
        
        #Constructor de la clase Creditos.
        #Inicializa Pygame, configura la pantalla, las fuentes, los colores,
        #carga las imágenes necesarias y define los elementos interactivos como el botón de regreso.
        
        # Inicialización de Pygame
        pygame.init()

        # Configuración de las dimensiones de la pantalla
        self.width, self.height = 1000, 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Créditos del Juego") # Título de la ventana

        # Definición de colores básicos
        self.background = (0, 0, 0) # Negro
        self.white = (255, 255, 255) # Blanco
        self.dodger_blue = (30, 144, 255) # Azul para el botón
        self.hover_green = (30, 144, 100) # Verde para el hover del botón

        # Carga de fuentes
        # Es importante asegurarse de que la ruta de la fuente sea correcta o manejar la excepción.
        try:
            self.font = pygame.font.Font(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\Proyecto POO - Juego de la Nave\assets\game_of_squids\Game Of Squids.ttf", 25)
        except pygame.error:
            print("Advertencia: Fuente 'Game Of Squids' no encontrada. Usando fuente del sistema.")
            self.font = pygame.font.SysFont("arial", 25)
        self.Simplefont = pygame.font.SysFont("arial", 24) # Fuente para el texto de los créditos

        # Configuración del botón "Regresar"
        self.botonRegresar = pygame.Rect(0, 0, 200, 50) # Dimensiones iniciales y posición (se ajustará)
        self.botonRegresar.topright = (self.width - 10, 10) # Posiciona el botón en la esquina superior derecha
        self.botonRegresarText = self.font.render("Regresar", True, (0,0,0)) # Texto del botón (negro)
        self.rectBotonRegresarText = self.botonRegresarText.get_rect(center=self.botonRegresar.center) # Centra el texto en el botón
        self.botonRegresarColor = self.dodger_blue # Color inicial del botón
        self.posicionOriginalBoton = self.botonRegresar.copy() # Guarda la posición original para la animación
        self.animationProgress = 0.0 # Progreso de la animación (0.0 a 1.0)
        self.animationSpeed = 14.0 # Velocidad de la animación
        self.animationTarget = 7 # Desplazamiento objetivo de la animación en píxeles
        self.hoverBoton = False # Estado para saber si el cursor está sobre el botón

        # Instancia del menú principal para poder regresar a él
        # Se asume que ventanaPrincipal.lobby() es la clase del menú principal.
        self.menuPrincipal = ventanaPrincipal.lobby()

    def ejecutar(self):
        #Método principal que ejecuta el bucle de la ventana de créditos.
        #Maneja los eventos, actualiza la lógica de la animación del botón
        #y dibuja todos los elementos en pantalla.
        # Detiene la música del menú principal si se está reproduciendo.
        # Es una buena práctica verificar si el objeto musica existe y tiene el método stop.
        if hasattr(self.menuPrincipal, 'musica') and hasattr(self.menuPrincipal.musica, 'stop'):
            self.menuPrincipal.musica.stop()

        active = True # Controla si el bucle principal debe continuar
        last_time_dt = time.time() # Tiempo anterior para calcular el delta time (dt)

        while active:
            # Cálculo del delta time (dt) para un movimiento y animaciones fluidas e independientes del framerate.
            current_time_dt = time.time()
            dt = current_time_dt - last_time_dt
            last_time_dt = current_time_dt

            # Gestión de eventos de Pygame
            for event in pygame.event.get():
                if event.type == QUIT: # Evento para cerrar la ventana (ej: click en la 'X')
                    active = False
                    # Considerar si al cerrar créditos se debe cerrar todo el juego o volver al menú.
                    # Por ahora, solo cierra esta ventana.
                if event.type == KEYDOWN: # Evento de tecla presionada
                    if event.key == K_ESCAPE: # Tecla ESC para salir/regresar
                        active = False
                    # Podría ser útil que K_RETURN también regrese si no hay otros inputs.
                    # if event.key == K_RETURN:
                    # active = False
                if event.type == MOUSEBUTTONDOWN: # Evento de clic del ratón
                    if event.button == 1: # Clic izquierdo
                        if self.botonRegresar.collidepoint(event.pos): # Verifica si el clic fue sobre el botón "Regresar"
                            active = False # Sale de la ventana de créditos
                            # Aquí se debería llamar al método para dibujar/ejecutar el menú principal.
                            # self.menuPrincipal.dibujarVentana() # Asumiendo que dibujarVentana reinicia el loop del menú.

                if event.type == MOUSEMOTION: # Evento de movimiento del ratón
                    # Verifica si el cursor está sobre el botón "Regresar" para la animación de hover.
                    if self.botonRegresar.collidepoint(event.pos):
                        self.hoverBoton = True
                    else:
                        self.hoverBoton = False

            # Lógica de la animación para el botón "Regresar"
            if self.hoverBoton:
                # Animación de entrada (cursor sobre el botón)
                # El progreso va de 0.0 (sin efecto) a 1.0 (efecto completo).
                # Aquí parece que se intenta un efecto de "hundimiento" o "empuje".
                # La lógica actual con min(0.0, ...) y max(1.0, ...) parece invertida o necesita revisión.
                # Si se quiere que el botón se mueva hacia abajo (offset positivo) al hacer hover:
                self.animationProgress = min(1.0, self.animationProgress + self.animationSpeed * dt)
                self.botonRegresarColor = self.hover_green # Cambia el color al hacer hover
            else:
                # Animación de salida (cursor fuera del botón)
                self.animationProgress = max(0.0, self.animationProgress - self.animationSpeed * dt)
                self.botonRegresarColor = self.dodger_blue # Restaura el color original

            # Aplica el desplazamiento de la animación al botón
            offset = self.animationTarget * self.animationProgress
            self.botonRegresar.centery = int(self.posicionOriginalBoton.centery + offset)
            # Recalcula la posición del texto del botón para que se mueva con el botón
            self.rectBotonRegresarText.center = self.botonRegresar.center

            # ---- Sección de Dibujo ----
            self.screen.fill(self.background) # Limpia la pantalla con el color de fondo

            # Dibuja el título "Creditos"
            text_titulo = self.font.render("Creditos", True, self.white)
            # Posiciona el título. Usar // para división entera es buena práctica para coordenadas.
            # El ancho // 3 puede ser un poco arbitrario, centrarlo sería width // 2.
            text_rect_titulo = text_titulo.get_rect(center=(self.width // 2, self.height // 4)) # Ajustado para mejor posición
            self.screen.blit(text_titulo, text_rect_titulo)

            # Contenido de los créditos
            credits_text_lines = [
                "Desarrollado por:",
                "Eduard Fernando Garcia",
                "Eddy Sebastian Gomez",
                "", 
                "Curso: Programación I - Grupo 204",
                "Enfoque: Programación Orientada a Objetos (POO)",
                "Semestre: Segundo",
                "",
                "Herramientas Utilizadas:",
                "Framework Pygame (Python)",
                "Gestión de Datos: JSON",
                "",
                "Institución: UDEC (Universidad de Cundinamarca)"
            ]

            # Renderiza y dibuja cada línea de los créditos
            line_y_start = self.height // 2 - 80 # Posición Y inicial para la primera línea de créditos
            line_height = 30 # Espacio vertical entre líneas
            for i, line in enumerate(credits_text_lines):
                text_surface_line = self.Simplefont.render(line, True, self.white)
                text_rect_line = text_surface_line.get_rect(center=(self.width // 2, line_y_start + i * line_height))
                self.screen.blit(text_surface_line, text_rect_line)

            # Dibuja el botón "Regresar"
            pygame.draw.rect(self.screen, self.botonRegresarColor, self.botonRegresar, border_radius=20)
            self.screen.blit(self.botonRegresarText, self.rectBotonRegresarText)

            pygame.display.flip() # Actualiza toda la pantalla para mostrar los cambios

        # Al salir del bucle, se puede decidir si volver al menú principal o cerrar.
        # Si se quiere volver al menú, el código que llama a self.menuPrincipal.dibujarVentana()
        # debería estar aquí, después de que el bucle de créditos termine.
        # print("Saliendo de créditos, volviendo al menú...")
        # self.menuPrincipal.dibujarVentana() # Esto reiniciaría el menú.