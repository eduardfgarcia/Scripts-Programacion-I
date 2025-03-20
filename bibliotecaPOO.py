# Estudiantes: Garcia Niño Eduard Fernando | Gomez Vega Eddy Sebastian
# CADI : Programacion I 
# Grupo : 204
# Semestre : 2

# Actividad: Programacion Orientada a Objetos (POO), Crear Librerias que implemente metodos manipulando libros con sus respectivos atributos

# Universidad de Cundinamarca Seccional Girardot

import time

# Clase Libros
class books:
    #Establecer tipos de datos
    name : str
    autor: str
    año_publicacion : int
    disponibilidad : bool
    def __init__(self,name,autor,año_publicacion,disponibilidad):
        self.name = name
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.disponibilidad = disponibilidad
        
    def prestar(self):
        if self.disponibilidad:
            self.disponibilidad = False
            print(f"El libro ha sido prestado")
        else:
            print("El libro no esta disponible")
    def devolver(self):
        if not self.disponibilidad:
            self.disponibilidad = True
            print(f"El libro se devolbió.")
        else: print("El libro fué Devuelto")
    
    def informacion(self):
        print(f"El libro contiene esta Informacion: \n\n\t- Nombre : {self.name}\n\t- Autor : {self.autor}\n\t- Año de Publicacion : {self.año_publicacion}")
            
# Clase bibliotecas
class library:
    name_library : str
    lista_libro : list
    
    def __init__(self,name_library,lista_libro):
        self.name_library = name_library
        self.lista_libro = lista_libro
        
    def agregar_libro(self,titulo):
        # Ordenando y almacenando atributos del libro mediante el diccionario
        description = dict(libro = titulo.name,autor= titulo.autor,publicacion= titulo.año_publicacion,disponibilidad= titulo.disponibilidad)
        self.lista_libro.append(description)
        print("\nEspere un momento...")
        time.sleep(2)
        print(f"\n\tEl libro {description['libro']} \nfue Agregado a la {self.name_library} con exito...:)")

    def mostrar_libros(self):
        print("\nEspere un momento...")
        time.sleep(1.5)
        # Iterando los elementos de la libreria 
        for i,val in enumerate(self.lista_libro):
            print(f"\nlibro {i+1} : Datos: {val}")   
            return
        print(f"\n\t- Estos son Todos los libros de la respectiva biblioteca {self.name_library} :)")     
    
    def buscar_libro(self, titulo):
        print(f"\nEspere un momento...\n Buscando {titulo.name} de la libreria {self.name_library}")
        time.sleep(1.5)
        for libro in self.lista_libro:
            if libro['libro'] == titulo:
                print(f"\n\t- El libro contiene esta información: \n\n\t- Nombre: {libro['libro']}\n\t- Autor: {libro['autor']}\n\t- Año de publicación: {libro['publicacion']}")
                return 
        print(f"\tX - El libro no se encuentra en la Biblioteca {self.name_library}:(")

    def prestar_libro(self, titulo):
        print(f"\nEspere un momento... Analizando la libreria {self.name_library}")
        time.sleep(1.5)
        for libro in self.lista_libro:
            if libro['libro'] == titulo:
                if libro['disponibilidad']:
                    libro['disponibilidad'] = False
                    print(f"El libro {titulo.name} ha sido prestado")
                    return
                else:
                    print(f"El libro {titulo.name} no está disponible")
                    return
        print(f"\tX - El libro {titulo.name} no se encuentra en la Biblioteca {self.name_library}:(")

    def devolver_libro(self, titulo):
        print("Espere un momento...")
        time.sleep(1.5)
        for libro in self.lista_libro:
            if libro['libro'] == titulo:
                if not libro['disponibilidad']:
                    libro['disponibilidad'] = True
                    print(f"El libro {titulo.name} se devolvió. Esta disponible en la libreria : {self.name_library}")
                    return
                else:
                    print(f"El libro {titulo.name} ya fue devuelto a la libreria {self.name_library}")
                    return
        print(f"\tX - El libro {titulo.name} no se encuentra en la Biblioteca {self.name_library}:(")


# libros Ejemplos
cien_anios = books("Cien años de soledad", "Gabriel García Márquez", 1967, True)
mil_novecientos_ochenta_y_cuatro = books("1984", "George Orwell", 1949, True)
el_senor_de_los_anillos = books("El señor de los anillos", "J.R.R. Tolkien", 1954, True)
orgullo_y_prejuicio = books("Orgullo y prejuicio", "Jane Austen", 1813, True)
don_quijote = books("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, True)

#Bibliotecas o Librerias Ejemplos
library_1 = library("Libreria 1",[])
library_2 = library("Libreria 2",[])
library_3 = library("Libreria 3",[])


library_1.agregar_libro(cien_anios)
library_1.agregar_libro(el_senor_de_los_anillos)

library_1.buscar_libro(cien_anios)
library_1.mostrar_libros()

