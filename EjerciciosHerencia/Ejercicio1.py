#Ejercicio 1: Herencia Simple - Persona y Estudiante
#Crea una clase Persona con atributos nombre y edad, y un método presentarse() que imprima una presentación. Luego, crea una clase Estudiante que herede de Persona y agregue el atributo carrera.
#Requisitos:
#El estudiante debe heredar el método presentarse() y agregar información sobre la carrera, crear al menos un objeto de Estudiante y mostrar su presentación.

class personas:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    
    def Presentarse(self):
        return f"name : {self.name} | age : {self.age}"

class estudiante(personas):
    def __init__(self,name,age,programa):
        super().__init__(name,age)
        self.programa = programa

    def Presentarse(self):
        return f'Nombre Estudiante: {self.name}\n\nEdad: {self.age}\n\nPrograma: {self.programa}'


student1 = estudiante('Eddy',18,'INGENIERIA DE SOFTWARE')

print(student1.Presentarse())

