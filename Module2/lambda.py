# Función lambda 
# lambda es una pequeña función anónima que se conforma de una cantidad de argumentos n y estrictamente una sola expresión.
# la expresión se ejecuta y se retorna el resultado, por lo que se debe atrapar en una varible 

x = lambda a : a + 10
print("La suma de 10+5 es ", x(5))

x_multiplicacion = lambda a, b : a * b
print("La multiplicación de 5*6 es: ", x_multiplicacion(5, 6))

resultado = lambda a, b, c, d: (a+b)-(c+d)


print("El resultado es ", resultado(4, 5, 1, 2))
print("El resultado es ", resultado(6, 7, 8, 9))



