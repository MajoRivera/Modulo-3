
nombre = input("Nombre: ")
edad = int(input("Edad: "))

if(edad >= 18):
    print(f" {nombre}, tienes {edad} eres mayor de edad")

else:
    print(f" {nombre}, tienes {edad} eres menor de edad") 


pais = input("País: ")
pais_validar = pais.upper()

if(pais_validar == "MEXICO" or pais_validar == "MÉXICO"):
    if(edad >= 18):
        print(f" {nombre}, tienes {edad} eres mayor de edad")
elif(pais_validar == "USA" or pais_validar == "ESTADOS UNIDOS"):
        if(edad >= 21):
            print(f" {nombre}, tienes {edad} eres mayor de edad")
else:
    print(f" {nombre}, tienes {edad} eres mayor de edad")



num1 = int(input("Número: "))

if(num1 % 2 == 0):
    print("El número es par")

else:
    print("El número es impar")


tipo_pizza = input("¿Vegetariana o Normal?: ")
tipo_pizza = tipo_pizza.lower()

if(tipo_pizza == "vegetariana"):
    print("Menú: Ingredientes default: Mozzarella, Tomate. Ingredientes para seleccionar: Pimiento o Tofu")
    ingrediente_v = input("Ingrediente seleccionado: ")
    ingrediente_v = ingrediente_v.lower()
    if(ingrediente_v == "pimiento" or ingrediente_v == "tofu"):
        print(f" Pizza {tipo_pizza}, Ingredientes: mozzarella, tomate y {ingrediente_v}")
elif(tipo_pizza == "normal"):
    print("Menú: Ingredientes default: Mozzarella, Tomate. Ingredientes para seleccionar: Peperoni o Jamón o Salmón")
    ingrediente_v = input("Ingrediente seleccionado: ")
    ingrediente_v = ingrediente_v.lower()
    if(ingrediente_v == "peperoni" or ingrediente_v == "jamon" or ingrediente_v == "salmon"):
        print(f" Pizza {tipo_pizza}, Ingredientes: mozzarella, tomate y {ingrediente_v}")



