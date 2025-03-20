import abc
import random
class person:
    def __init__(object,name,age):
        object.name = name
        object.age = age

    def printname(self):
        print(self.name)

class student(person):
    def __init__(self,name,age,lname):
        ## Funcion para relacioar a la clase 'padre'
        super().__init__(name,age)
        self.lastname = lname 

    def welcome(self):
        print(self.name,self.age,self.lastname)


personX = student('John',17,'Doe')

personX.welcome()
personX.printname()
print(personX.name)


del personX 

## Iterador iter() para listas,tuplas,sets, diccionarios devuelve e itera los elementos cada uno

## Iteracion basica
my_tuple = (2,4,6,8)
myit = iter(my_tuple)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Iterador bucles loops 

#for i,val in enumerate(my_tuple):
##  print(val)

## Creando clases para iterar elementos 
class Numbers:
    ## Funcion __iter__ actua como constructor e iterable de elementos
    def __iter__(self):
        self.x = 0
        self.y = 10 
        self.z = 50
        return self

    def __next__(self):
        if self.x <= 30 and self.y <= 100:
            x = self.x
            y = self.y
            z = self.z
            self.x += 1
            self.y += 10
            self.z += 50
            return x,y,z
        else:
            raise StopIteration 

myClass = Numbers()
myIter = iter(myClass)
## Bucle iterador de clase 

for i in myIter:
    print(f'\nNumber iterable Class  ::  {i}')
    print(f'\n{type(i)}')

## Polimorfismo en clases

class Runner():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Run!!")

class walk():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Walk**")

class plane():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model 

    def move(self):
        print("Fly!!")

car1 = Runner("Car","Mazda")
pers = walk("John","Doe")
planex = plane("AirPlane","Australian")

#Invocando una funcion que en las tres clases la tienen por igual

for i in car1,pers,planex:
    i.move()
    
    
    
question = float(input("ingrese un numero para sacarle mitad   ::  "))  
lambda_question = lambda x : x / 2 
print(lambda_question(question))


def my_condition(n):
    if n %2 == 0:
        return n
    
my_list = [1,2,3,4,5,6]
question1 = filter(my_condition,my_list)
print(list(question1))



question2 = filter(lambda n : n % 2 == 1 , my_list)
print(list(question2))
    


    


    
    







