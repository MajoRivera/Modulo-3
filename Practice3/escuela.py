class Persona:
    def __init__(self, nombre, apellido, edad) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def datos(self):
        print(f"Datos generales de la persona: {self.nombre} {self.apellido}, {self.edad} años")         

class Tutor(Persona):
    def __init__(self, nombre, apellido, edad, nombre_hijo, ocupacion) -> None:
        super().__init__(nombre, apellido, edad)
        self.nombre_hijo = nombre_hijo
        self.ocupacion = ocupacion       

class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, nombre_padre, calificacion, grupo, faltas) -> None:
        super().__init__(nombre, apellido, edad)
        self.nombre_padre = nombre_padre
        self.calificacion = calificacion
        self.grupo = grupo
        self.faltas = faltas
        #self.aprobo = aprobo

    def aprobatoriio_cal(self):
        if(self.calificacion >= 6):
            print("Aprobado")
        else:
            print("Reprobado")

    def aprobatorio_faltas(self):
        if(self.faltas > 10):
            print("Reprobado")
        else:
            print("Aprobado")


tutor1 = Tutor('Alan', 'Rodríguez', 32, 'Ray', 'Ingeniero')
tutor1.datos()
print(f"Datos del Tutor: Nombre del hijo: {tutor1.nombre_hijo}, Ocupación: {tutor1.ocupacion}")  

estudiante1 = Estudiante('Sam', 'Triulzi', 27, 'Iván', 9, 'B', 11)
estudiante1.datos()
print(f"Datos del Estudiante: Nombre del padre: {estudiante1.nombre_padre}, Calificación: {estudiante1.calificacion}, Grupo: {estudiante1.grupo}, Faltas: {estudiante1.faltas}") 
estudiante1.aprobatoriio_cal()
estudiante1.aprobatorio_faltas()

total_tutores = []
total_tutores.append(tutor1.__dict__)

total_estudiantes = []
total_estudiantes.append(estudiante1.__dict__)

