#programa que pide n numeros para calcular el mcm de ellos
#realizado por Luis Becerra
#17/10/2022

a=int(input("Ingrese el primer número: "))
b=int(input("Ingrese el segundo número: "))

i=2

while True:
    if(i%a==0 and i%b==0):
        mcm=i
        break
    i+=1
print(mcm)