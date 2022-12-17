#Tipos de datos: int, string, float, boolean, double, longint
#int - número entero
#string - cadena de texto
#float - número con punto flotante / decimal
#boolean - valor verdadero o falso
#double - número con punto decimal (más preciso que float)
#longint - número entero con mayor rango (puede tener más valores que el int)

variable_flotante = 2.0
verdadero = True
cadena = 'Hola Mundo'
entero = 3
print(variable_flotante)
print(type(variable_flotante))
print(verdadero)
print(cadena)
print(type(entero))

suma = variable_flotante + entero
print(suma)
print(cadena*entero)

#Operadores aritméticos:
# +, -, *, /, **, //, %

suma = variable_flotante + entero
print(suma)
resta = variable_flotante - entero
print(resta)
multiplicacion = variable_flotante * entero
print(multiplicacion)
division = variable_flotante / entero
print(division)
potencia = variable_flotante ** entero #(2.0^3)
print(potencia)
division_truncada = variable_flotante // entero #(Quita la parte decimal y deja la parte entera)
print(division_truncada)
modulo = entero % variable_flotante #(Te devuelve el residuo de la división)
print("Modulo:", modulo)
print(f"Suma: {suma}, Resta: {resta}")
print("Suma:", suma, "Resta:", resta)

#Operadores lógicos and (&&), not (!), or (||)

# and && - Sólo regresa verdadero cuando ambas sentencias son verdaderas.
# or || - Regresa verdadero cuando cualquiera de las sentencias sea verdadera.
# not ! - Invierte el valor de la sentencia.

#Breakpoint - Debug

variable1 = True
variable2 = False 

if(variable1 and variable2):
    print("Falso con and")

if(variable1 or variable2):
    print("Verdadero con or")

if(variable1 and not variable2):
    print("Verdadero con and y not")

#Operadores de asignación
# =, +=, -=, *=, /=

a = 5
print(a)
a += 7
print(a)

#Operadores de comparación
# ==, !=, >, <, >=, <=

a, b, c = 1, 2, 1

if a == c:
    print("a y c son iguales")

if a != b:
    print("a y b son diferentes")

if a < b:
    print("a es menor que b") 

if a <= c:
    print("a es menor o igual que c")

#Operadores de pertenecia
# in, not in
# Sirven para buscar valores dentro de un arreglo

lista_numeros = [1,2,3,4]  
buscando1 = 4
buscando2 = 5

if buscando1 in lista_numeros:
    print("El número:", buscando1, "está en la lista")

if buscando2 in lista_numeros:
    print("El número:", buscando2, "está en la lista")

if buscando2 not in lista_numeros:
    print("El número:", buscando2, "no está en la lista")

#Operadores de identidad
#Para ver si 2 objetos no tuplabes son iguales

# is, is not

tupla_numeros1 = (0,1,2,3,4,5)
tupla_numeros2 = (0,1,2,3,4,5)
tupla_numeros3 = (0,1,2,3,4,6)
lista5 = [1,2,3,4]
lista6 = [1,2,3,4]
hola = "Hola"
mundo = "Mundo"

if tupla_numeros1 is tupla_numeros2:
    print("Las tulpas son iguales")

if tupla_numeros1 is not tupla_numeros3:
    print("Las tuplas no son iguales")

if hola is not mundo:
    print(f"{hola} {mundo}")

# Funciones
# funciones sin parámetro y sin retorno
# funciones con parámetro y sin retorno
# funciones sin parámetro y con retorno
# funciones con parámetro y con retorno

a, b = 5, 10 # variables globales

print(a, " ", b)

#sin parámetros y sin retorno
def primera_funcion():
    a, b = 7, 15
    print(a, " ", b)

def segunda_funcion(num1, num2):
    suma = num1 + num2
    division = num1 / num2
    print(suma)
    print(division)

def tercera_funcion():
    a, b = 7, 20
    multiplicacion = a*b
    return (multiplicacion, a, b)

def cuarta_funcion(num1, num2):
    potencia = num1**num2
    return potencia

primera_funcion()
#print(a, " ", b)

segunda_funcion(num1 = 17, num2 = 5)

resultado, a1, b1 = tercera_funcion()
print(resultado, a1, b1)

potencia = cuarta_funcion(2, 8)
print("El resultado de la potencia es", potencia)

# Listas Tuplas Diccionarios
#Las posiciones se empiezan a contar de 0, 1, 2, 3, 4...

lista1 = [10, 9 , 7, 10]
lista2 = [1, "perro", 2.5, "casa", True]
lista4 = []
print(lista1)
print(lista2)
#Para agragar objetos o valores a la lista se utiliza .append()
lista2.append(lista1)
print(lista2)

#Para copiar una lista
lista3 = lista2.copy()
print(lista3)

#lista4.append(lista1)
#print(lista4)

#DEvuelve la posición de cierto valor
lista4 = lista1.copy()
print(lista4.index(7))

print("Primer número:", lista1[0])
print("Tercer número:", lista1[lista1.index(7)])
print("Penúltimo número", lista1[-2])

lista4.sort()
print(lista4)
lista2.reverse()
print(lista2)
lista4.reverse()
print(lista4)

lista4.insert(1, 8)
print(lista4)
valor_quitado = lista4.pop(1)
print(valor_quitado)
print(lista4)

print("Número de aplicaciones:", lista4.count(10))

#Diccionarios

diccionario = {"mascotas": ['perro', 'gato', 'pez'], "calificaciones:": lista4, 1: 'majo'}
print(diccionario)
print(diccionario["mascotas"])
print(diccionario["calificaciones:"])
print(diccionario[1])

usuario = {"username": 'marira', 'password': '1234'}
password = '1975'

if usuario['password'] is password:
    print("Tienes acceso")

else: 
    print("Contraseña equivocada")


nombre = input("Introduce tu usename: ")
pswd = input("Introduce tu contraseña: ")

id_1 = {"username": "marira1", "password": "1234"}

if (id_1["username"] == nombre) and (id_1["password"] == pswd):
    print("Tienes acceso")

else:
    print("Usuario o Contraseña equivocada")

tupla5 = (1,3,2,3,4)
print(tupla5.count(3))

#Ciclos for

for i in  range(0, 10, 1):
    print("Valor de i 1:", i)

for i in range(0, 10, 2):
    print("Valor de i 2:", i)    

for i in range(10):
    a += 1
    print("Valor de a:", a)

for element in lista1:
    print(element)
    suma += element
    print("La suma de todos los elementos de la lista es:", suma)
    print("")

for i in range(len(lista5)):
    print(i, "", lista5[i])






