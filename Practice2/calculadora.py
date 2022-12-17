class Calculadora:


        def suma(self):
                suma = num1 + num2
                print("La suma es: ", suma)


        def resta(self):    
                resta = num1 - num2
                print("La resta es: ", resta)


        def multiplicacion(self):    
                multiplicacion = num1 * num2
                print("La resta es: ", multiplicacion)


        def division(self):    
                division = num1 / num2
                print("La resta es: ", division)


num1 = float(input("Ingresa el primer número:"))
num2 = float(input("Ingresa el segundo número:"))

resultado_final = Calculadora()

operacion = input("¿Qué operación deseas realizar?")
operacion = operacion.upper()


if(operacion == "SUMA"):
    print(resultado_final.suma())

if(operacion == "RESTA"):
    print(resultado_final.resta())    

if(operacion == "MULTIPLICACION" or operacion == "MULTIPLICACIÓN"):
    print(resultado_final.multiplicacion())

if(operacion == "DIVISION" or operacion == "DIVISIÓN"):
    print(resultado_final.division())    

else:
    print("Operación no reconocida, intenta con 'SUMA', 'RESTA', 'MULTIPLICACIÓN' o 'DIVISIÓN'")     