# Recursión 
# una función que se llama a sí misma 
# se debe tener cuidado porque fácilmente se puede escribir una recursión que nunca termine o una que exceda la memoria de nuestro procesador 
# La recursividad se utiliza cuando quieres trabajar sobre el mismo resultado que te da la función con las instrucciones de la función. 

# 1. Sumar los números naturales hasta N (se lo damos nosotros) de forma recursiva.
# 2. Factorial de un número.


# 5
# result = 5 + tri_recursion(4)
# 4
# result = 9 + tri_recursion(3)

# --->
# N = 8 7 6 5 4 3 2 1 0 
# resultado = 0 1 3 5 9 14 ... 
# <--- 

'''
def N= 8: 
    def: 
        def N= 1: 
            def N= 0: 
                return 0
            return 1+0
        return
    return

'''
'''
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\n Ejemplo de recursión")
tri_recursion(6)'''

def suma(N): 
    if(N > 0): 
        resultado = N + suma(N-1)
    else: 
        resultado = 0 
    return resultado
print("La suma recursiva es: ", suma(10))

##### Factorial de un número 
# 10*9*8*...*1
# x!
# 5! 

def factorial(num): 
    if(num > 1): 
        resultado = num * factorial(num-1)
    else: 
        resultado = 1
    return resultado

numero = int(input("Dame un número: "))
factorial_res = factorial(numero)
print(f"El factorial de tu número es {factorial_res}")

# 3. Calcular el valor de la posición fibonacci usando recursividad. 
# 7 - el valor de la posición 7 de la serie de fibonacci 
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
def fibonacci(n):  
    if (n > 2): 
        actual = fibonacci(n-1) + fibonacci(n-2)
    else: 
        actual = 1 
    return actual
posicion = int(input("Dame la posición de la serie de fibonacci: "))
resultado = fibonacci(posicion)
print(f"El valor de la serie en la posicion {posicion} es: {resultado}")



