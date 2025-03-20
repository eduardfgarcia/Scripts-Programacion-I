class vehicule:
    def __init__(self,brand,model):
        self.brand = brand 
        self.model = model 
    
    def move(self):
        print("move!!")

## Salta turno class
class car(vehicule):
    pass

class plane(vehicule):
    def move(self):
        print(f"Fly!! ")


class boat(vehicule):
    def move(self):
        print("Scrach!!")     


btax = boat("musta2x23","BoatAustralian")
planex = plane("AxEWR","AustralianAirPlane")

for i in btax,planex:
    print(i.brand)
    print(i.model)
    i.move()


class person:
    def __init__(object,name,age):
        object.name = name
        object.age = age

    def welcome(self):
        print(self.name,self.age)

class student(person):
    def welcome(self):
        print(self.name,self.age)

    
st1 = student("John Doe", 25)
st1.welcome()


class iterator:
    def __iter__(self):
        self.x = 1
        self.y = 10
        return self

    def __next__(self):
        if self.x <= 30 and self.y >= 1:
            x = self.x
            y = self.y
            z = self.x * self.y
            self.x += 1
            self.y -= 1
            return x,y,z
        raise StopIteration

myIter = iterator()
x = iter(myIter)

for i in x:
    print(f"Number : {i}")


class VideoGame():
    def __init__(self,name,version,valoracion):
        self.name =name
        self.version = version
        self.valoracion = valoracion

    def name(self): print(f"El Nombre del Videojuego es : {self.name}")

    def version(self): print(f"La version del Videojuego {self.name} es : {self.version}")
    def ranking(self): print(f"La Valoracion del Videojuego {self.name} es : {self.valoracion} Estrellas")


game_1 = VideoGame("Counter Strike",2.0,5)
game_1.ranking()




#class users():
#    def __init__(self,name,surname,email):
 #       self.name = name
  #      self.surname = surname
   #     self.email = email
    
  #  def welcome(self): print( f"Welcome!! {self.name} | {self.surname}")
  #  def register(self): print( f"Su email es : {self.email}")

#user_1 = users("Eduard","Garcia","eduardfgarcia@ucundinamarca.....")

#user_1.welcome()