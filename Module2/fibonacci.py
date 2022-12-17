
def fibonacci(n): 
    if (n > 2): 
        actual = fibonacci(n-1) + fibonacci(n-2)
    else: 
        actual = 1 
    return actual
posicion = int(input("Dame la posición de la serie de fibonacci: "))
resultado = fibonacci(posicion)
print(f"El valor de la serie en la posicion {posicion} es: {resultado}")
