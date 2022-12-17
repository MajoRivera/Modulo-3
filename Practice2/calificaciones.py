class Alumno:
    def __init__(self, nombre, parcial1, parcial2, parcial3):
        self.nombre = nombre
        self.parcial1 = parcial1
        self.parcial2 = parcial2
        self.parcial3 = parcial3
        

    def promedio(self):
        prom = (self.parcial1 + self.parcial2 + self.parcial3) / 3
        print(f"El primedio de {self.nombre} es: ", prom)

    def aprobacion(self):
        prom = (self.parcial1 + self.parcial2 + self.parcial3) / 3
        if(prom >= 5.5):
            print("Aprobado")
        else:
            print("Reprobado")


alumno1 = Alumno("Sam", 4.0, 5.5, 6.5)
alumno1.promedio()
alumno1.aprobacion()