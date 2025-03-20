
## Ejercicio en Clase: Clase Videojuegos POO

# Estudiantes : Eddy Gomez  y  Eduard Garcia 

class VideoGame():
    # Atributos
    def __init__(self,name,version,gender,developer,plataforms,valoracion):
        self.name =name
        self.version = version
        self.valoracion = valoracion
        self.gender = gender
        self.developer = developer
        self.plataforms = plataforms
        
    #Metodos
    def c_name(self): print(f"El Nombre del Videojuego es : {self.name}")
    def vers(self): print(f"La version del Videojuego {self.name} es : {self.version}")
    def c_gender(self): print(f"El genero del Videojuego {self.name} es : {self.gender}")
    def c_developer(self): print(f"El desarrollador del Videojuego {self.name} es : {self.developer}")
    def c_plataforms(self): print(f"Las plataformas del Videojuego {self.name} es : {self.plataforms}")
    def ranking(self): print(f"La Valoracion del Videojuego {self.name} es : {self.valoracion} Estrellas")
    

    
game_1 = VideoGame("Counter Strike",2.0,"FPS","Valve corporation",["Microsoft Windows", "macOS", "GNU/Linux", "Xbox", "Mac OS"],5)

#game_1.vers()
#game_1.ranking()

# Llama a todos los metodos del objeto

for nombre_atributo in dir(game_1):
    atributo = getattr(game_1, nombre_atributo)
    if callable(atributo) and not nombre_atributo.startswith("__"):
        atributo()
