#Esto es una suma 
verdad = False
a = 'a'
b = 5324532  
print(a*5)

#Operadores aritméticos 
# +, -, *, /, **, //, %
c = 1 
d = 1.5 

# Nombres de variables con significado! 
suma1 = c+d
suma2 = c+d+1
sumA1 = c+d+2
resta = c-d
multiplicacion = c*d
division = c/d
exponte = c**d
division_truncada = d//c 
residuo = c%d
print(f'La suma es {suma1}, la suma más 1 es {suma2}, la resta es {resta}, suma diferente {sumA1}, la multiplicación {multiplicacion}')
print(f'La division es {division}, el exponente es {exponte}, division truncada {division_truncada}, residuo de divicio c y d {residuo}')

#Operadores lógicos and, not, or
verdad = True
falso = False

if verdad and falso: 
    print("Sentencia and de verdadero y falso")

if verdad and not falso: 
    print("Sentencia and de verdadero y no falso")

if verdad or falso: 
    print("Sentencia and de verdadero o falso")

# Operadores de asignación 
a = 3
a += 4 
print(a)
a -= 5 
print(a)
a *= 5
print(a)

# Operadores de comparación 
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

#Operadores de pertenencia
# in, not in 

lista_numeros = [0,1,3,4,5]

if a in lista_numeros: 
    print(f"{a} está en la lista")
if b in lista_numeros: 
    print(f"{b} está en la lista")
elif b not in lista_numeros: 
    print(f"{b} no está en la lista")

#Operadores de identidad 
# is, #is not  

tupla_numeros = (0,1,3,4,5)
tupla_numeros2 = (0,1,3,4,5)
tupla_numeros3 = (0,1,3,4,6)
hola = "hola"
mundo = "mundo"

if tupla_numeros is tupla_numeros2: 
    print("Las tuplas son iguales")
if tupla_numeros is not tupla_numeros3: 
    print("Las tuplas no son iguales")

if hola is not mundo: 
    print(f"{hola} {mundo}")

print("hola ", mundo)










# Variables gloables 
# Funciones 
# Listas, tuplas, diccionarios 
#Funcion sin parametros y sin retorno 
def primera_funcion():     
    nuevo = 9
    print(a, b)    

#Funciones con parametros y sin retorno 
# Las variables originales no las modifica en lo demás del programa
def segunda_funcion(a, b):
    a += 1 
    b -= 1 
    print(a, b)
    print(a + b)

a, b = 10, 2.5
#Funciones sin parametros y con retorno
def tercera_funcion(): 
    a, b = 10, 2.5
    a += 1
    b -= 1     
    return a, b 

#Funcion con parametros y con retorno
def cuarta_funcion(a, b):
    a *= b
    b += 78 
    c = a+b    
    return a, b, c

primera_funcion()
segunda_funcion(a, b)
print(a, b)

a, b = tercera_funcion()
a1, b1 = tercera_funcion()
print(f"Valor de a {a}, valor de b {b}, valor de {a1}, valor de {b1}")
a, b, suma = cuarta_funcion(a, b)
print(f"Valor de a {a}, valor de b {b}, valor de la suma {suma}")

# listas, tuplas, diccionarios 
lista = [1, 'perro', 4.5, 'casa']
lista_str = ['z', 'g', 'b', 'u', 'a']

tupla = (1, 'perro', 4.5, 'casa')
print(lista)
lista.append(4.5)
print(lista)
print(lista.count(4.5))
lista_str.sort()
print(lista_str)
lista_str.reverse()
print(lista_str)

matriz = [[1,2,3], [1,2,3], [1,2,3], 'matriz', 9]
print(matriz)
matriz.reverse()
print(matriz)

#lista 1 indices son nodos, lo que haya en el índice es el valor 

#username = input("Dame tu nombre de usuario: ")
#password = input("Escribe una contraseña: ")

#diccionario = {'numeros': [1, 2, 3], 'usuario': {'username': username, 'password': password}}

#print(diccionario['usuario'])

for i in range(0, 10, 2): 
    print(i)

for i in range(10): 
    a += 1 
    print(a)

for elemnent in matriz: 
    print(elemnent)
print("")

for i in range(len(matriz)): 
    print(i, ' ', matriz[i])

    
