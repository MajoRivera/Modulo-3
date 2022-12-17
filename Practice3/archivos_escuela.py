import escuela as e

tutores = open("modulo3/archivos_txt/tutores.txt", "a")
estudiantes = open("modulo3/archivos_txt/estudiantes.txt", "a")

for tutor in e.total_tutores:
    tutores.write("{ \n")
    for elemento in tutor:
        tutores.write(f"{str(elemento)} : {str(tutor[elemento])} \n")
        tutores.write("} \n")


for estudiante in e.total_estudiantes:
    estudiantes.write("{ \n")
    for elemento in estudiante:
        estudiantes.write(f"{str(elemento)} : {str(estudiante[elemento])} \n")
        estudiantes.write("} \n")