def fibonacci(N):
    if(N > 2):
        fibonacci = fibonacci(N-1) + fibonacci(N-2)
    else:
        resultado = -1
    return resultado
print("Serie de Fibonacci: ", fibonacci(5))