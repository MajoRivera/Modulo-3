import os

#Creación de arcvhivo:
# w - Se sobreescribe el archivo
file1 = open('practice3/archivos_txt/archivo1,txt', 'w')
file1.write("Hola")
file1.write("Adios")
#Cierra el archivo (para no tener problemas después con el uso)
file.close()
# a - Se agrega archivo
file2 = open('practice3/archivos_txt/archivo2,txt', 'a')
file2.write("Hola")
# r - para leer archivo
file3 = open('practice3/archivos_txt/archivo1.txt', 'r')
