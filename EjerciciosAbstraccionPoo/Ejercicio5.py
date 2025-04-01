# Ejercicio 5: Implementar una clase Menú que permita interactuar con el usuario y ejecutar un menú de opciones
import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod

class Menu(ABC, tk.Frame): 
    def __init__(self, root): #Atributos Principales
        self.root = root
        self.contador = 0 
        self.Frame = tk.Frame(root, height=1200,width=1200,bg = "lightgreen") #Lienzo
        self.activateAnimation = True 
        self.fondoAnimado() #Fondo animado en bucle
    # Fondo dinamico
    def fondoAnimado(self):
        if self.activateAnimation:
            colores = ["red", "green", "blue", "yellow"]
            self.Frame.config(bg=colores[self.contador % len(colores)])
            self.contador += 1
            self.Frame.after(500, self.fondoAnimado) # Llama a la funcion cada 500 ms

    #Metodos abstractos
    @abstractmethod # Abstraccion
    def inicializarSesion(self):  
        pass
        
    def mostrarSesion(self): #Mostrar cada interfaz
        self.Frame.pack(fill=tk.BOTH, expand=True) #Ajustar el tamaño del lienzo a la ventana como tal

    def ocultarSesion(self):
        self.Frame.pack_forget()

# Menu Principal
class principal(Menu):
    def inicializarSesion(self):
        tk.Label(self.Frame, text="Menu Principal",font = ("Roboto mono",20),relief="solid").pack(pady = 80)
        tk.Label(self.Frame, text="Hecho por Eduard Garcia",font = ("Roboto mono",10),fg ="white",bg = "black").pack(pady = 10)
        buttonUI = tk.Button(self.Frame, text="Calculadora de UI", command=lambda: controlador.mostrar_seccion("CalculadoraUI"),font = ("Roboto mono",14),bg = "white",fg = "black",relief='solid')
        buttonUI.pack(pady=10)
        buttonIMC = tk.Button(self.Frame, text="Calculadora de Masa corporal IMC", command=lambda: controlador.mostrar_seccion("CalculadoraIMC"),font = ("Roboto mono",14),bg = "white",fg = "black",relief='solid')
        buttonIMC.pack(pady=10)   
        buttonSisNumericos = tk.Button(self.Frame, text="Calculadora de Sistemas Numericos", command=lambda: controlador.mostrar_seccion("calculadorSisNumericos"),font = ("Roboto mono",14),bg = "white",fg = "black",relief='solid')
        buttonSisNumericos.pack(pady=10)
        buttonDatosPersonales = tk.Button(self.Frame, text="Deja tus Datos Personales", command=lambda: controlador.mostrar_seccion("datosPersonales"),font = ("Roboto mono",14),bg = "white",fg = "black",relief='solid')
        buttonDatosPersonales.pack(pady=10)
        buttonIMC.bind("<Enter>",lambda e: buttonIMC.config(bg="lightgreen",fg="green"))
        buttonIMC.bind("<Leave>",lambda e: buttonIMC.config(bg="white",fg="black"))
        buttonUI.bind("<Enter>",lambda e: buttonUI.config(bg="lightgreen",fg="green"))
        buttonUI.bind("<Leave>",lambda e: buttonUI.config(bg="white",fg="black"))
        buttonSisNumericos.bind("<Enter>",lambda e: buttonSisNumericos.config(bg="lightgreen",fg="green"))
        buttonSisNumericos.bind("<Leave>",lambda e: buttonSisNumericos.config(bg="white",fg="black"))
        buttonDatosPersonales.bind("<Enter>",lambda e: buttonDatosPersonales.config(bg="lightgreen",fg="green"))
        buttonDatosPersonales.bind("<Leave>",lambda e: buttonDatosPersonales.config(bg="white",fg="black"))
        exit = tk.Button(self.Frame, text= "Salir",font=("Roboto mono",14),command=root.destroy, bg= "red",fg="white",relief="solid")
        exit.pack(pady =10)
        exit.bind("<Enter>",lambda e: exit.config(bg="white",fg="red"))
        exit.bind("<Leave>",lambda e: exit.config(bg="red",fg="white"))

#Calculadora de unidades de longitud
class calculadoraDeUnidades(Menu):
    def inicializarSesion(self):
        self.activateAnimation = False
        self.Frame.config(bg="lightgreen")
        button = tk.Button(self.Frame, text="Regresar", font=("Roboto mono",14),command=lambda: controlador.mostrar_seccion("Menu"),relief='solid', bg = "blue",fg ="white")
        button.place(y=0,x=0)
        button.bind("<Enter>",lambda e: button.config(bg= "white",fg ="blue"))
        button.bind("<Leave>",lambda e: button.config(bg= "blue",fg ="white"))
        def calcule(num,op):
            match op:
                case "Centimetros": result.config(text = f'Conversion: {num * 100}cm')
                case "Decimetro": result.config(text = f'Conversion: {num * 10}dm')
                case "Decametro": result.config(text = f'Conversion: {round(num / 10)}Dm') 
                case "Hectometro": result.config(text = f'Conversion: {round(num / 100)}Hm') 
                case "Kilometros": result.config(text = f'Conversion: {round(num / 1000)}Km') 

        tittle = tk.Label(self.Frame,text= "Conversor de SUI",font=("Roboto mono", 20),fg = "green",bg = "light green")
        tittle.pack(pady= 70)
        subtext = tk.Label(self.Frame, text= "Ingrese un Valor (m)", font = "calibri",fg = "green",bg = "light green")
        subtext.pack(pady = 5)
        #subtext.place(x = 180,y= 180)

        inputU = tk.Entry(self.Frame,font=("Roboto mono", 15),relief="solid")
        inputU.pack(pady = 10)

        subtextU = tk.Label(self.Frame, text= "Ingrese la Unidad de Longitud", font = "calibri",fg = "green",bg = "light green")
        subtextU.pack(pady = 2)

        listOptions = ["Centimetros","Decimetro","Decametro","Hectometro","Kilometros"]
        options = ttk.Combobox(self.Frame, values=listOptions)
        options.pack()

        Button = tk.Button(self.Frame, text = "Submit",font=("Roboto mono", 15),command = lambda : calcule(int(inputU.get()),options.get()) ,bg = "green", fg ="white", relief= "solid")
        Button.pack(pady = 30)
        Button.bind("<Enter>", lambda e : Button.config(bg= "white", fg = "green"))
        Button.bind("<Leave>", lambda e : Button.config(bg= "green", fg = "white"))

        result = tk.Label(self.Frame, bg = "light green", fg = "green", font=("Roboto mono", 15))
        result.pack(pady = 40)

#Calculadora de Masa corporal IMC
class calculadoraIMC(Menu):
    def inicializarSesion(self):
        self.activateAnimation = False
        self.Frame.config(bg="white")
        button = tk.Button(self.Frame, text="Regresar", font=("Roboto mono",14),command=lambda: controlador.mostrar_seccion("Menu"),relief='solid', bg = "blue",fg ="white")
        button.place(y=0,x=0)
        button.bind("<Enter>",lambda e: button.config(bg= "white",fg ="blue"))
        button.bind("<Leave>",lambda e: button.config(bg= "blue",fg ="white"))
        def calculeInfo(pes,alt):
            IMC = round(pes / (alt**2))
            if 1.5 < alt <= 2:
                if IMC < 18.5: result.config(text = f'IMC  :  {IMC}  |  Bajo Peso')
                if 19 <= IMC < 25: result.config(text = f'IMC  :  {IMC}  |  Peso Normal')
                if 25 <= IMC < 30: result.config(text = f'IMC  :  {IMC}  |  Sobrepeso')
                if 30 <= IMC < 35: result.config(text = f'IMC  :  {IMC}  |  Obesidad I')
                if 35 <= IMC < 40: result.config(text = f'IMC  :  {IMC}  |  Obesidad II')
                if IMC >= 40: result.config(text = f'IMC  :  {IMC}  |  Obesidad III')
            else: result.config(text = f'Ingrese una Altura coherente malparido')

        title = tk.Label(self.Frame, text = "Calculadora de Masa Corporal IMC",font=("Roboto mono", 20),fg = "black",bg="white")
        title.pack(pady = 70)
        spinbox1 = tk.Spinbox(self.Frame,from_ = 44, to = 145,font=("Roboto mono", 15),relief="solid")
        subtext = tk.Label(self.Frame,text = "Ingrese su Masa (Kg)",font = "Calibri",bg="white")
        spinbox1.pack(pady=10)
        subtext.pack(pady = 10)

        spinbox2 = tk.Spinbox(self.Frame,from_ = 1.5, to = 2.0,font=("Roboto mono", 15),relief="solid")
        subtext2 = tk.Label(self.Frame,text = "Ingrese su Altura (m)",font = "Calibri",bg="white")
        spinbox2.pack(pady= 10)
        subtext2.pack(pady= 10)
        Button = tk.Button(self.Frame, text = "Submit", command = lambda : calculeInfo(int(spinbox1.get()),float(spinbox2.get())),font=("Roboto mono", 15), bg = "light green", fg ="green", relief= "solid")
        Button.pack(pady = 10)
        Button.bind("<Enter>", lambda e : Button.config(bg= "white"))
        Button.bind("<Leave>", lambda e : Button.config(bg= "lightgreen"))

        result = tk.Label(self.Frame)
        result.pack(pady = 10)

class calculadorSisNumericos(Menu):
    def inicializarSesion(self):
        self.activateAnimation = False
        self.Frame.config(bg= "lightblue")
        button = tk.Button(self.Frame, text="Regresar", font=("Roboto mono",14),command=lambda: controlador.mostrar_seccion("Menu"),relief='solid', bg = "blue",fg ="white")
        button.place(y=0,x=0)
        button.bind("<Enter>",lambda e: button.config(bg= "white",fg ="blue"))
        button.bind("<Leave>",lambda e: button.config(bg= "blue",fg ="white"))
        def calculeNums(num , op):
            match op:
                case "Binario": result.config(text = f'Binario : {bin(num)[2:]}')
                case "Octal": result.config(text = f'Octal : {oct(num)[2:]}')
                case "Hexadecimal": result.config(text = f'Hexadecimal : {hex(num)[2:]}')
        title = tk.Label(self.Frame, text = "Conversor de Sistemas Numericos",font=("Roboto mono", 20),fg = "blue",bg = "light blue")
        title.pack(pady = 80)    
        subtext = tk.Label(self.Frame, text= "Ingrese un Valor Decimal", font = "calibri",fg = "blue",bg = "light blue")
        subtext.pack(pady = 5)
        inputU = tk.Entry(self.Frame,font=("Roboto mono", 15),relief="solid")
        inputU.pack(pady = 10)
        subtextU = tk.Label(self.Frame, text= "Ingrese un tipo de Numeracion", font = "calibri",fg = "blue",bg = "light blue")
        subtextU.pack(pady = 2)
        listOptions = ["Binario","Octal","Hexadecimal"]
        options = ttk.Combobox(self.Frame, values=listOptions, font=("Roboto mono", 14))
        options.pack()
        Button = tk.Button(self.Frame, text = "Submit",font=("Roboto mono", 15),command = lambda : calculeNums(int(inputU.get()),options.get()) ,bg = "green", fg ="white", relief= "solid")
        Button.pack(pady = 30)
        Button.bind("<Enter>", lambda e : Button.config(bg= "white", fg = "green"))
        Button.bind("<Leave>", lambda e : Button.config(bg= "green", fg = "white"))
        result = tk.Label(self.Frame, bg = "light blue", fg = "blue", font=("Roboto mono", 15))
        result.pack(pady = 40)

class datosPersonales(Menu):
    def inicializarSesion(self):
        self.activateAnimation = False
        self.Frame.config(bg= "white")
        def guardar_datos():
            nombre = nombre_entry.get()
            edad = edad_entry.get()
            ciudad = ciudad_entry.get()

            tabla.insert('', 'end', values=(nombre, edad, ciudad))

            nombre_entry.delete(0, tk.END)
            edad_entry.delete(0, tk.END)
            ciudad_entry.delete(0, tk.END)
        button = tk.Button(self.Frame, text="Regresar", font=("Roboto mono",14),command=lambda: controlador.mostrar_seccion("Menu"),relief='solid', bg = "blue",fg ="white")
        button.place(y=0,x=0)
        button.bind("<Enter>",lambda e: button.config(bg= "white",fg ="blue"))
        button.bind("<Leave>",lambda e: button.config(bg= "blue",fg ="white"))
        
        tk.Label(self.Frame, text="Nombre:",bg="white").grid(row=0, column=0)
        nombre_entry = tk.Entry(self.Frame)
        nombre_entry.grid(row=0, column=1)

        tk.Label(self.Frame, text="Edad:",bg="white").grid(row=1, column=0)
        edad_entry = tk.Entry(self.Frame)
        edad_entry.grid(row=1, column=1)

        tk.Label(self.Frame, text="Ciudad:",bg="white").grid(row=2, column=0)
        ciudad_entry = tk.Entry(self.Frame)
        ciudad_entry.grid(row=2, column=1)

        # Botón para guardar datos
        guardar_button = tk.Button(self.Frame, text="Guardar", command=guardar_datos,font =("Roboto mono",14),bg="green",fg="white",relief="solid")
        guardar_button.grid(row=3, column=0, columnspan=2)

        # Tabla para mostrar los datos
        tabla = ttk.Treeview(self.Frame, columns=('Nombre', 'Edad', 'Ciudad'), show='headings')
        tabla.heading('Nombre', text='Nombre')
        tabla.heading('Edad', text='Edad')
        tabla.heading('Ciudad', text='Ciudad')
        tabla.grid(row=4, column=0, columnspan=2)

#Control de flujo de secciones de interfaz
class ControladorSecciones:
    def __init__(self, root):
        self.root = root
        self.secciones = dict() #Diccionario de secciones
        self.seccion_activa = None

    def agregar_seccion(self, nombre, seccion):
        self.secciones[nombre] = seccion
        seccion.inicializarSesion()

    def mostrar_seccion(self, nombre):
        if self.seccion_activa:
            self.secciones[self.seccion_activa].ocultarSesion()   #gestion de secciones para inicializar cada seccion para luego mostrarla en pantalle de acuerdo a la accion del usuarioa a travez del diccionario de secciones y metodos abstractos
        self.secciones[nombre].mostrarSesion()
        self.seccion_activa = nombre


#Control de Flujo
root = tk.Tk()
root.title("Menu de usuario")
root.geometry("600x600")
controlador = ControladorSecciones(root)

menu = principal(root)
calculdoraDeUnidades = calculadoraDeUnidades(root)
calculadorIMC = calculadoraIMC(root)
calculadorSisNumericos = calculadorSisNumericos(root)
datosPersonales = datosPersonales(root)

# Agregar secciones al diccionario para despues mostrarlos en pantalla
controlador.agregar_seccion("CalculadoraUI", calculdoraDeUnidades)
controlador.agregar_seccion("CalculadoraIMC",calculadorIMC)
controlador.agregar_seccion("calculadorSisNumericos",calculadorSisNumericos)
controlador.agregar_seccion("datosPersonales",datosPersonales)
controlador.agregar_seccion("Menu", menu)

# MenuPrincipal
controlador.mostrar_seccion("Menu") # Muestra la sección inicial.

root.mainloop()
