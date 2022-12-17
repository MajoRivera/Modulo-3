class Automovil:
    def __init__(self, num_puertas, num_llantas, aceleracion) -> None:
        self.num_puertas = num_puertas
        self.num_llantas = num_llantas
        self.aceleracion = aceleracion

    def avanzar(self):
        print("El auto está avanzando")

    def frenar(self):
        print("El auto está frenando")

    def acelerar(self):
        print("El auto está acelerando")        

class Carro(Automovil):
    def __init__(self, num_puertas, num_llantas, aceleracion, cilindros, marca, modelo, asientos) -> None:
        super().__init__(num_puertas, num_llantas, aceleracion)
        self.cilindros = cilindros
        self.marca = marca
        self.modelo = modelo
        self.asientos = asientos

    def radio(self):
        print("Se está reproduciendo la radio")    

class Moto(Automovil):
    def __init__(self, num_puertas, num_llantas, aceleracion, marca, modelo, color) -> None:
        super().__init__(num_puertas, num_llantas, aceleracion)
        self.num_puertas = 0
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def caballito(self):
        print("El motociclista está haciendo caballito")    


class Bici(Automovil):
    def __init__(self, num_puertas, num_llantas, aceleracion, marca, tipo) -> None:
        super().__init__(num_puertas, num_llantas, aceleracion)
        self.num_puertas = 0
        self.marca = marca
        self.tipo = tipo

    def andar(self):
        print("La bici está andando")     

class Camioneta(Automovil):
    def __init__(self, num_puertas, num_llantas, aceleracion, cilindros, marca, modelo, asientos) -> None:
        super().__init__(num_puertas, num_llantas, aceleracion)
        self.cilindros = cilindros
        self.marca = marca
        self.modelo = modelo
        self.asientos = asientos

    def aire(self):
        print("El aire acondicionado está prendido")    
    


carro1 = Carro(4, 4, 300, 6, 'Honda', '2001', 3)
carro1.acelerar()
print(f"El carro tiene un total de {carro1.asientos} asientos")
carro1.radio()

moto1 = Moto(4, 4, 200, 'Vespa', '2022', 'Negra')
moto1.frenar()
print(f"La moto tiene un total de {carro1.asientos} asientos")
moto1.caballito()

bici1 = Bici(4, 4, 200, 'Benotto', 'Montaña')
bici1.acelerar()
print(f"La bici tiene un total de {carro1.asientos} asientos")
bici1.andar()

camioneta1 = Camioneta(4, 4, 400, 6, 'BMW', '2023', 7)
camioneta1.acelerar()
print(f"La camioneta tiene un total de {carro1.asientos} asientos")
camioneta1.aire()