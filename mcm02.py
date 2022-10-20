#programa que pide n numeros para calcular el mcm de ellos probando git
#realizado por Luis Becerra
#17/10/2022

#solicito la cantidad de numeros a calcular el mcm
cant = int(input("Ingrese la cantidad de números a calcular el mcm: ")) 

#creamos una lista vacia para almacenar los denominadores
denominadores = []

#iteramos para solicitar los denominadores y almacenarlos como enteros en la lista
for i in range(0,cant):
    denominadores.append(int(input("Ingrese el número: ")))

#imprimimos la lista para comprobar que estan bien almacenados
print ("la lista de denominadores es ", *denominadores)

#declaramos el divisor
divisor = 2
residuos = 0

#ciclo para calcular el mcm
while True:
    #recorremos la lista para sacar uno a uno los denominadores y calcular su módulo con respecto al divisor
    for i in denominadores:
        if divisor%i==0:
            residuos = residuos + 0
 
        else:
            residuos = residuos + 1
    #si la variable residuos permaneció en cero entonces ese divisor es el mcm de todos los elementos de la lista
    if residuos == 0:
        mcm = divisor
        break
    #si la bandera residuos se vió afectada fue porque uno de los denominadores arrojó residuo y no es exacta
    residuos = 0  
    #incrementamos el divisor para seguir iterando    
    divisor+=1

#imprimimos el mcm    
print ("el mcm es: ",mcm)