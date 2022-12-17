# Uso de if, elif, else 
# elif: si las condiciones anteriores no fueron ciertas, entonces trata con la siguiente condición. 
# else procesa lo que no fue procesado por las condiciones anteriores. 
# 



# 

num1, num2 = 4, 8
'''
if (num1 == num2):
    print("los números son iguales") 
elif (num2 > num1): 
    print("el segundo es mayor que el primero")
elif (num1 < num2): 
    print("el primero es menor que el segundo")
else:
    print("el segundo número es el mayor")'''

#Lo que nos regresa el % es el residuo de la división 
if(num1%2==0): #Si divides un número entre 2 y te da 0 de residuo, entonces es un número par
    if(num2%2==0): 
        if(num1==num2): 
            print("Los números son iguales y pares")
        else: 
            print("Los números son pares pero diferentes")



### EJERCICIOS ### 

# 1. Programa que pida nombre y edad y le diga al usuario '_nombre_ eres mayor de edad' en caso de que tenga mínimo 18 años, 
# de lo contrario decir '_nombre_ eres menor de edad'
'''
nombre = input("Dame tu nombre: ")
edad = int(input("Dame tu edad: "))

if (edad >= 18): 
    print(f"{nombre} tienes {edad} años y eres mayor de edad")
else: 
    print(f"{nombre} tienes {edad} años y eres menor de edad")
'''

# 2. Igual que el anterior pero también pedir país, si es México seguir las condiciones anteriores, si es USA basarse en la edad de 21 años. 
# .upper() .lower()
'''
pais = input("Dame tu país: ")
pais_validar = pais.upper()

if(pais_validar == "MEXICO" or pais_validar == "MÉXICO"): 
    if (edad >= 18): 
        print(f"{nombre} tienes {edad} años y eres mayor de edad")
    else: 
        print(f"{nombre} tienes {edad} años y eres menor de edad")
elif(pais_validar == "USA"): 
    if (edad >= 21): 
        print(f"{nombre} tienes {edad} años y eres mayor de edad")
    else: 
        print(f"{nombre} tienes {edad} años y eres menor de edad")'''


# 3. Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

num = int(input("Dame un número: "))
if(num % 2 == 0): 
    print("Tu número es par")
else: 
    print("Tu número es impar")

'''
4. La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.   
'''

# 1. preguntar si es vegetariana o no. 
# 2. si es vegetariana mostrar pimiento y tofu 
# 3. si no es vegetariana mostrar peperoni, jamon y salmon 
# 4. Mostrar el tipo de pizza, mostrar ingredientes default: mozzarella y tomate + el elegido 

tipo_pizza = input("Escribe si tu pizza es vegetariana o no vegetariana: ")
tipo_pizza = tipo_pizza.upper()

if (tipo_pizza == "VEGETARIANA"): 
    print("******* MENÚ INGREDIENTES ********")
    print("1. Pimiento")
    print("2. Tofu")
    ingrediente = input("Elige un ingrediente para tu pizza: ")
    print(f"tu pizza es vegetariana y sus ingredientes son mozzarela, tomate y {ingrediente}")
    
else: 
    print("******* MENÚ INGREDIENTES ********")
    print("1. ¨Peperoni")
    print("2. Salmón")
    print("3. Jamóm")
    ingrediente = input("Elige un ingrediente para tu pizza (escribe el número): ")
    if (ingrediente == "1"): 
        print("tu pizza es no vegetariana y sus ingredientes son mozzarela, tomate y peperoni")
    elif (ingrediente == "2"): 
        print("tu pizza es no vegetariana y sus ingredientes son mozzarela, tomate y salmon")
    else: 
        print("tu pizza es no vegetariana y sus ingredientes son mozzarela, tomate y jamon")