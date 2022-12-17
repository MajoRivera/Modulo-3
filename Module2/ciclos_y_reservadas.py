# Ciclo while, break, continue, while-else, for-else 
# while ejecuta una serie de instrucciones mientras que la condición sea cierta 
# break detiene al ciclo incluso cuando la condición es cierta
# continue detiene la iteración actual y se va a la siguiente
# while-else ejecuta una serie de instrucciones cuando la condición ya no es verdadera 

a, b = 9, 1
'''
while(a > b):
    if (a == 4): 
        a -= 1
        continue
    print(a)
    a -= 1 
else: 
    print(a)
    print("El ciclo terminó")'''


    


'''
while(a > b): 
    print("A es mayor que B")
    a -= 2
else: 
    print("A ya no es mayor que B")
'''

palabra = "Curso Python"

for letra in palabra: 
    print(letra)
else: 
    print("Se acabó la frase")
