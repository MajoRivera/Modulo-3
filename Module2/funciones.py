# Argumentos arbitrarios, llaves arbitrarias, valores default.
# argumentos == parametros

def funcion(num1, num2, num3, num4, num5):
    suma =  num1+num2+num3+num4+num5
    return suma

def miFuncion(*numeros):
    suma = 0
    for numero in numeros: 
        suma += numero
    print(type(numeros))
    return suma 

print("La suma es: ", miFuncion(8, 4, 5, 7, 9))

def miFuncion2(**diccionario): 
    return diccionario['var1']
    
print("El numero del diccionario es: ", miFuncion2(var1 = 8, var2 = 16, num3 = 9))

def miFuncion3(num1, num2=1): 
    return num1*num2
print("La multiplicación es: ", miFuncion3(8, 9))