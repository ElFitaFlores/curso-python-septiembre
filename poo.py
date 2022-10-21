class Persona():
    nombre = 'John'
    apellido = 'Doe'
    
    def __init__(self, nombre=None, apellido=None):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'''
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        '''

    def caminar(self):
        print(f'{self.nombre} está caminando')

    def __dormir(self):
        print('Estoy durmiendo')

    def avisar(self):
        self.__dormir()

persona = Persona()
print(type(persona))
print(persona.nombre)
print(persona.caminar())

rafa = Persona('Rafael', 'Flores')
print(rafa.nombre)
print(rafa.apellido)
print(rafa)
print(rafa.avisar())


class Animal():
    altura = None
    peso = 0

    def caminar(self):
        print('El animal está caminando')

class Perro(Animal):
    def caminar(self):
        print('El perro camina en 4 patas')

    def moverCola(self):
        print('El perro mueve la cola')


bobby = Perro()
bobby.caminar()
print(bobby.altura)
bobby.moverCola()

x = Animal()
x.caminar()
print(x.altura)

class Pato(Animal):
    def volar(self):
        print('El pato vuela')

donald = Pato()
donald.volar()
print(donald.altura)
donald.altura = 5
print(donald.altura)

from abc import ABC, abstractmethod

class Equipo(ABC):
    @abstractmethod
    def encender(self):
        pass

class SmartPhone(Equipo):
    def encender(self):
        print('Teléfono encendido...')

equipo = SmartPhone()
print(equipo)
equipo.encender()

class Carro():
    ruedas = 4
    color = None
    precio = 100

    def avanzar(self):
        pass

    @staticmethod
    def consultarPrecio():
        return 100

print(Carro.avanzar())