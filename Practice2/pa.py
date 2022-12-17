class Triangulo:
    def __init__(self, lado1, lado2, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.base = base
        self.altura = altura

    def perimetro(self):
        resultado = self.lado1 + self.lado2 + self.base
        print("El perímetro es: ", resultado)

    def area(self):
        resultado = (self.base*self.altura)/2
        print("El área del triángulo es: ", resultado)

triangulo1 = Triangulo(1, 5, 2, 4)
triangulo1.perimetro()
triangulo1.area()