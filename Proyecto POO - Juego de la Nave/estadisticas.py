import pygame
import os
import json
import time
import ventanaPrincipal
# import juegoNave # Se mantiene si es parte de un proyecto más grande, aunque no se usa directamente aquí.

class Estadisticas:
    def __init__(self):
        pygame.init()
        self.width, self.height = 1000, 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Estadisticas")
        self.background = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        # Carga de la fuente personalizada
        # Asegúrate de que esta ruta sea correcta en tu sistema
        try:
            self.title_font = pygame.font.Font(r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\juegodeNave\assets\game_of_squids\Game Of Squids.ttf", 36)
        except FileNotFoundError:
            print("Advertencia: No se encontró la fuente personalizada. Usando fuente predeterminada.")
            self.title_font = pygame.font.SysFont("arial", 36, bold=True)

        self.stats_file = "estadisticas.json"
        self.rutaDirectorio = r"C:\Users\eduar\Desktop\U Cundinamarca\DIrectorio PRORAMACION - UDEC\Programacion  I -204 - Segundo Semestre\game\juegodeNave"
        self.rutaCompleta = os.path.join(self.rutaDirectorio, self.stats_file)
        self.table_rect = pygame.Rect(80, 80, self.width - 160, 400)
        self.header_bg = (40, 40, 40)
        self.row_bg = (20, 20, 20)
        self.header_font = pygame.font.SysFont("arial", 28, bold=True)
        self.font = pygame.font.SysFont("arial", 24) 
        self.cell_font = pygame.font.SysFont("arial", 24)
        self.ColorBotonRegresar = (255,255,255)
        self.animationProgress = 0.0
        self.animationSpeed = 8.0
        self.animationTarget = 7
        self.hoverButton = True
        
        # Botón para borrar datos
        self.delete_button_text = "Borrar Todos los Datos"
        self.delete_button_font = pygame.font.SysFont("arial", 26, bold=True)
        self.delete_button_color = (180, 0, 0) # Rojo oscuro
        self.delete_button_hover_color = (255, 50, 50) # Rojo más claro al pasar el ratón
        self.delete_button_rect = pygame.Rect(self.width // 3 - 150, self.height - 80, 300, 50)

        self.botonRegresar = pygame.Rect(self.width // 2 + 35, self.height - 80, 10, 10)
        self.botonRegresar.width = self.width // 3
        self.botonRegresar.height = 50
        self.botonRegresarText = self.title_font.render("Regresar", True, (0, 0, 0))
        self.rectBotonRegresarText = self.botonRegresarText.get_rect(center = (self.botonRegresar.center))
        self.ColorBotonRegresar = (255,255,255)
        self.pocisionOriginal = self.botonRegresar.copy()

        
        self.confirm_delete = False # Estado para la confirmación de borrado
        self.confirm_message_font = pygame.font.SysFont("arial", 30, bold=True)

        self.estadisticas = self.cargar_estadisticas()

    def guardar_estadistica(self, nombre, puntaje):
        self.estadisticas.append({"nombre": nombre, "puntaje": puntaje})
        with open(self.rutaCompleta, "w", encoding="utf-8") as f:
            json.dump(self.estadisticas, f, indent=4)
        print(f"Estadistica guardada: {nombre} - {puntaje}")

    def cargar_estadisticas(self):
        if os.path.exists(self.rutaCompleta):
            try:
                with open(self.rutaCompleta, "r", encoding="utf-8") as f:
                    # Intenta cargar el JSON. Si el archivo está vacío, json.load() fallará.
                    content = f.read()
                    if content:
                        return json.loads(content)
                    else:
                        return [] # Archivo vacío
            except json.JSONDecodeError:
                print(f"Error: El archivo '{self.stats_file}' no es un JSON válido o está corrupto. Se creará uno nuevo.")
                return []
            except Exception as e:
                print(f"Error inesperado al cargar estadísticas: {e}")
                return []
        return [] # El archivo no existe

    def borrar_todos_los_datos(self):
        self.estadisticas = []  # Vacía la lista en memoria
        try:
            with open(self.rutaCompleta, "w", encoding="utf-8") as f:
                json.dump(self.estadisticas, f, indent=4) # Escribe una lista vacía en el archivo
            print("Todos los datos han sido borrados exitosamente.")
        except Exception as e:
            print(f"Error al borrar los datos: {e}")

    def mostrar_estadisticas(self):
        self.screen.fill(self.background)
        # Dibuja el botón "Regresar"
        pygame.draw.rect(self.screen, self.ColorBotonRegresar, self.botonRegresar, border_radius=10)
        self.screen.blit(self.botonRegresarText, self.rectBotonRegresarText)
        # Título
        titulo = self.title_font.render("Estadisticas", True, self.white)
        self.screen.blit(titulo, (self.width // 2 - titulo.get_width() // 2, 30))
        
        # Encabezados de la tabla
        header_row_rect = pygame.Rect(self.table_rect.x, self.table_rect.y, self.table_rect.width, 40)
        pygame.draw.rect(self.screen, self.header_bg, header_row_rect)
        nombre_header = self.header_font.render("Nombre", True, self.white)
        puntaje_header = self.header_font.render("Puntaje", True, self.white)
        self.screen.blit(nombre_header, (self.table_rect.x + 20, header_row_rect.y + 8))
        self.screen.blit(puntaje_header, (self.table_rect.right - puntaje_header.get_width() - 20, header_row_rect.y + 8))

        # Ordenar estadísticas de mayor a menor puntaje
        estadisticas_ordenadas = sorted(self.estadisticas, key=lambda x: x['puntaje'], reverse=True)
        
        # Mostrar las estadísticas (últimos 10, ordenados)
        for i, stat in enumerate(estadisticas_ordenadas[:10]):  # Muestra los 10 mejores puntajes
            row_rect = pygame.Rect(self.table_rect.x, self.table_rect.y + (i + 1) * 40, self.table_rect.width, 40)
            pygame.draw.rect(self.screen, self.row_bg if i % 2 == 0 else self.header_bg, row_rect)
            
            nombre_text = self.cell_font.render(stat['nombre'], True, self.white)
            puntaje_text = self.cell_font.render(str(stat['puntaje']), True, self.white)
            
            self.screen.blit(nombre_text, (self.table_rect.x + 20, row_rect.y + 8))
            self.screen.blit(puntaje_text, (self.table_rect.right - puntaje_text.get_width() - 20, row_rect.y + 8))
        
        # Dibuja el botón "Borrar Todos los Datos"
        mouse_pos = pygame.mouse.get_pos()
        button_color = self.delete_button_hover_color if self.delete_button_rect.collidepoint(mouse_pos) else self.delete_button_color
        pygame.draw.rect(self.screen, button_color, self.delete_button_rect, border_radius=10)
        delete_text_surface = self.delete_button_font.render(self.delete_button_text, True, self.white)
        self.screen.blit(delete_text_surface, delete_text_surface.get_rect(center=self.delete_button_rect.center))

        # Si se está en modo de confirmación
        if self.confirm_delete:
            # Fondo semi-transparente para el mensaje de confirmación
            overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180)) # Negro semi-transparente
            self.screen.blit(overlay, (0, 0))

            confirm_msg = self.title_font.render("¿Estás seguro de que quieres borrar TODOS los datos?", True, self.white)
            confirm_options = self.confirm_message_font.render("Presiona 'Y' para Sí, 'N' para No", True, self.white)
            
            self.screen.blit(confirm_msg, confirm_msg.get_rect(center=(self.width // 2, self.height // 2 - 30)))
            self.screen.blit(confirm_options, confirm_options.get_rect(center=(self.width // 2, self.height // 2 + 20)))

        pygame.display.flip()

    def ejecutar(self):
        activo = True
        currentTime = time.time()
        while activo:
            lastTime = time.time()
            dt = lastTime - currentTime
            lastTime = currentTime

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    activo = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        activo = False
                    
                    if self.confirm_delete:
                        if event.key == pygame.K_y: # Confirmar borrado
                            self.borrar_todos_los_datos()
                            self.confirm_delete = False # Sale del modo de confirmación
                        elif event.key == pygame.K_n: # Cancelar borrado
                            self.confirm_delete = False # Sale del modo de confirmación
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # Clic izquierdo del ratón
                        if not self.confirm_delete: # Solo procesa clics si no estamos en modo de confirmación
                            if self.delete_button_rect.collidepoint(event.pos):
                                self.confirm_delete = True # Entra en modo de confirmación
                if event.type == pygame.MOUSEMOTION:
                    if self.botonRegresar.collidepoint(event.pos):
                        self.hoverButton = True
                    else: self.hoverButton = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.botonRegresar.collidepoint(event.pos):
                        activo = False
                        mainMenu = ventanaPrincipal.lobby()
                        mainMenu.dibujarVentana()


            if self.hoverButton:
                self.ColorBotonRegresar = (200,200,200)
                self.animationProgress = min(1.0, self.animationProgress + self.animationSpeed * dt)
            else: 
                self.animationProgress = max(0.0, self.animationProgress - self.animationSpeed * dt)
                self.ColorBotonRegresar = (255,255,255)
            offset = self.animationTarget * self.animationProgress
            self.botonRegresar.centery = int(self.pocisionOriginal.centery + offset)
            self.rectBotonRegresarText.center = self.botonRegresar.center

            self.mostrar_estadisticas()
