class person:
    name : str
    Age : int
    DNI : float
    def __init__(self,name,Age,DNI):
        self.name = name
        self.Age = Age
        self.DNI = DNI
    
    def isMayorAge(self):
        if self.Age >= 18: 
            print("Es Mayor de Edad")
            return
        else: print("Es Menor de Edad")
    
    def getDMI(self):
        if self.Age >= 18: 
            print(f"\t\n- Tipo de Documento: CC\nDNI => {self.DNI}")
            return
        else: print(f"\t\n- Tipo de Documento: TI\nDNI => {self.DNI}")

    def info(self):
        print(f"\n\tNombre: {self.name}\n\tEdad: {self.Age}\n\tDNI: {self.DNI}")

person1 = person("Eduard",17,10.70596978)

person1.getDMI()

class cuenta:
    fondos : float
    def __init__(self,name,DMI):
        super().__init__(name,DMI)

    def mostrar(self,titular):
        print(f"EL titular:")

    def consignar_cuenta(self,titular,cantidad : int):
        self.fondos += cantidad
        print(f"El Titular {titular.name} identificado con DMI : {titular.DMI} Consigno {self.fondos} a su cuenta")
        return
    def retirar_fondos(self,titular,cantidad : int):
        self.fondos -= cantidad
        print(f"El Titular {titular.name} identificado con DMI : {titular.DMI} Consigno {self.fondos} a su cuenta")
        return 

