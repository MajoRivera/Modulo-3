#python es un lenguaje orientado a objetos y casi todo es un objeto en python con sus atributos y métodos 
'''
La programación orientada a objetos (POO) es un paradigma de programación en el que podemos pensar en problemas complejos como objetos.

Un paradigma es una teoría que proporciona la base para resolver problemas.

Así que cuando hablamos de POO, nos referimos a un conjunto de conceptos y patrones que utilizamos para resolver problemas con objetos.

Un objeto en Python es una colección única de datos (atributos) y comportamiento (métodos). Puedes pensar en los objetos como cosas reales que te rodean.
piensa en que los atributos siempre son sustantivos y los métodos siempre son verbos. 

métodos - cosas que hacen - funciones 
atributos - caracteristicas - variables

clase Automovil 
    tiene llantas
    tiene puertas 
    tiene volante 

    Avanza 
    Acelera 
    Frena 
    Pita 

'''

class MyClass:
  x = 5

# Objeto o instancia de la clase 
variable_clase = MyClass()
objeto = MyClass()

print("El atributo de la clase es: ", objeto.x)

class Person:
  def __init__(self, name1, age1):
    self.name = name1
    self.age = age1

persona1 = Person("John", 36)
persona2 = Person("Vane", 21)


print("Nombre de la persona 1 ", persona1.name)
print("Edad de la persona 2 ", persona2.age)

#Para eliminar el atributo de un objeto 
del persona1.age
print("No se eliminó en persona 2 ", persona2.age)

#Para eliminar un objeto
del persona1
#print(persona1)


### CLASE CON UN MÉTODO
class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person2("Morita", 21)
p1.myfunc()

# 1. Crea una clase rectángulo con su base, altura y que calcule el perímetro y el área 

class Rectangulo: 
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perimetro(self):
        resultado = (2*self.altura)+(2*self.base)
        print("El perimetro es ", resultado)
    def area(self): 
        resultado = self.base*self.altura
        print("El área del rectángulo es ", resultado)

# 2. Crea una clase triángulo con su base, altura, lado1, lado2 y que calcule el perímetro y el área
class Triangulo: 
    def __init__(self, base, altura, lado1, lado2):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
    def perimetro(self):
        resultado = self.lado1+self.base+self.lado2
        print("El perimetro es ", resultado)
    def area(self): 
        resultado = (self.base*self.altura)/2
        print("El área del triangulo es ", resultado)

triangulo1 = Triangulo(3, 4, 2, 2)
triangulo1.perimetro()
triangulo1.area()

# 3. Crea una clase alumno que pida su nombre y la calificación de los tres parciales. Crear métodos que devuelvan el promedio y digan si ha pasado la materia o no
# tomando en cuenta que el mínimo aprobatorio es 6, pero a partir de .5 decimales se redondea la calificación. 

class Alumno: 
    def __init__(self, parcial1, parcial2, parcial3, nombre):
       self.parcial1 = parcial1
       self.parcial2 = parcial2
       self.parcial3 = parcial3
       self.nombre = nombre
    def promedio(self): 
        promedio = (self.parcial1 + self.parcial2 + self.parcial3)/3
        if (promedio >= 5.5): 
            print(f"{self.nombre} tu promedio fue {promedio} y fue una calificación aprobatoria")
        else: 
            print(f"{self.nombre} tu promedio fue {promedio} y fue una calificación no aprobatoria")

alumno = Alumno(5, 4, 7, 'Morita')
alumno.promedio()

# 4. Crea una clase calculadora que pida dos numeros y tenga los métodos necesarios para calcular suma, resta, multiplicación y división. hacer uso de condiciones para 
# preguntar al usuario si quiere sumar, restar, multiplicar o dividir los números 

