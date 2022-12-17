
#Python es un lenguaje interpretado, ejecuta y compila al mismo tiempo.   
#Tipos de datos - int, string, float, boolean, double, longint
#int(numero entero)
#string(Cadena de texto)
#float(Número con punto floatante/decimal)
#boolean (Valor verdadero o falso)
#double (Numero con punto decimal)
#longint(numero entero con mayor rango)

variable_flotante = 1.5
verdadero = True
cadena = 'hola mundo'
entero = 1
print(variable_flotante)
print(type(variable_flotante))
print(verdadero)
print(cadena)
print(type(entero))

 
print(cadena*entero)

#Operadores aritméticos 
# +, -, *, /, **, //, %
suma = variable_flotante + entero
print(suma)
resta = variable_flotante - entero
print(resta)
multiplicacion = variable_flotante * entero
print(multiplicacion)
division = variable_flotante / entero
print(division)
potencia = variable_flotante ** entero
print(potencia)
division_truncada = variable_flotante // entero
print(division_truncada)
modulo_division = entero % variable_flotante
print("modulo_division", modulo_division)
print(f"La suma es {suma}, la resta es {resta}, la multiplicacion es {multiplicacion}")
print("La suma es ", suma, " la resta es ", resta, " la multiplicacion es ", multiplicacion)


#Operadores lógicos and, not, or
#  || && ! 
# 2 variables - verdadero o falso
# and - sólo regresa verdadero cuando las dos sentencias son verdaderas 
# or - nos regresa verdadero cuando cualquiera de las sentencias sea verdadera 
# not - Invierte el valor de tu sentencia 
variable1 = True
variable2 = False

if(variable1 and variable2): 
    print("Verdadero con and")

if(variable1 or variable2): 
    print("Verdadero con or")

if(variable1 and not variable2): 
    print("Verdadero con and y not")

# Operadores de asignación 
# =, +=, -=, *=, /= 
a = 5 
print(a)
a *= 7
print(a)

# Operadores de comparación 
# ==, !=, >, <, >=, <= 
a, b, c = 1, 2, 1

if a == c: 
    print("a y c son iguales")
if a != b: 
    print("a y b son diferentes")
#Estrictamente menor o mayor 
if a < b: 
    print("a es menor que b")

#Menor o igual a la otra variable
if a <= c: 
    print("a es menor o igual que c")

#Operadores de pertenencia
# in, not in 

lista_numeros = [1,2,3,4]
buscando = 4
buscando2 = 5

if buscando in lista_numeros: 
    print("El numero está en la lista", buscando)

if buscando2 in lista_numeros: 
    print("El numeor está en la lista")

if buscando2 not in lista_numeros: 
    print("El numero no está en la lista")

#Operadores de identidad 
# is, #is not  

tupla_numeros = (0,1,3,4,5)
tupla_numeros2 = (0,1,3,4,5)
tupla_numeros3 = (0,1,3,4,6)
lista1 = [1,2,3,4]
lista2 = [1,2,3,4]
hola = "hola"
mundo = "mundo"

if tupla_numeros is tupla_numeros2: 
    print("Las tuplas son iguales")
if tupla_numeros is not tupla_numeros3: 
    print("Las tuplas no son iguales")

if hola is not mundo: 
    print(f"{hola} {mundo}")

# FUNCIONES
# funciones sin parametro y sin retorno 
# funciones con parametro y sin retorno 
# funciones sin parametro y con retorno 
# funciones con parametro y con retorno

a, b = 5, 10 #variables globales 

print(a," ", b)
#sin parametros y sin retorno 
def primera_funcion():
    a, b = 7, 15
    print(a," ", b)

def segunda_funcion(num1, num2):
    division = num1 / num2
    print(division)

def tercera_funcion(): 
    a, b = 7, 20
    multiplicacion = a*b
    return (multiplicacion, a, b) 

def cuarta_funcion(num1, num2): 
    potencia = num1**num2
    return potencia

primera_funcion()
segunda_funcion(num1 = 17, num2 = 5)
resultado, a1, b1 = tercera_funcion()
print(resultado, a1, b1)
potencia = cuarta_funcion(2, 8)
print("El resultado de la potencia es ", potencia)


# LISTAS TUPLAS DICCIONARIOS 
# Las posiciciones se empiezan a contar de 0, ejemplo: 0, 1, 2, 3, 4 
lista4 = []


lista_calificaciones = [10, 9, 7, 10]



lista2 = [1, "perro", 2.5, "casa", True]
print(lista_calificaciones)
print(lista2)
#para agregar objetos o valores a la lista se utiliza .append()
lista2.append(lista_calificaciones)
print(lista2)
#Para copiar una lista 
lista3 = lista2.copy()
print(lista3)
#Devuelve la posicion de cierto valor
lista4 = lista_calificaciones.copy()
print(lista4.index(7))

#para acceder a valores de una lista se utiliza el indice 
print("Primera calificacion: ", lista_calificaciones[0])
print("Tercera calificacion: ", lista_calificaciones[lista_calificaciones.index(7)])
print("La penultima calificacion es: ", lista_calificaciones[-2])
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
print("Numero de apariciones: ", lista4.count(9))

#Diccionarios 
diccionario1 = {'mascotas': ['perro', 'gato', 'pez'], 'calificaciones': lista4, 1: 'vanessa'}
print(diccionario1)
print(diccionario1["mascotas"])
print(diccionario1["calificaciones"])
print(diccionario1[1])

nombre = input("Introduce tu username: ")
pswd = input("Introduce tu contraseña: ")

usuario = {'username': 'lomlomm', 'password': '1234'}

if (usuario['username'] == nombre) and (usuario['password'] == pswd):
    print("Tienes acceso")
else: 
    print("Contraseña equivocada")

tupla1 = (1,3,2,3,4)
print(tupla1.count(3))


#CICLOS FOR  
for i in range(0, 10, 2): 
    print("Valor de i", i)

for a in range(10):  
    print("Valor de a ", a)

suma = 0
for elemnent in lista_calificaciones:
    suma += elemnent
    print("La suma de todos los elementos de la lista es ", suma)
    

print("")

for i, elemnent in enumerate(lista2):
    print(f"El elemento {elemnent} está en la posición {i}")


for i in range(len(lista1)): 
    print(i, ' ', lista1[i])









