##Ejercicio 1
numero = int(input("Ingrese su numero: "))
rango = int(input("ingrese el rango de inicial: "))
rango_fin = int(input("Ingrese rango limite: "))
resultado = 1
for i  in range (rango, rango_fin + 1 ,1):
    if rango > 0:
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    else:
        print("no se puede hacerlo con nuermoes negativos")    







##Ejercicio :3 fivonacci

x = 0
y = 1
z = 0
num =int(input("Ingrese numero maximo :"))
print(x)
print(y)

for i in range(2,num,1) :
    z = x + y
    print(z)
    x = y
    y = z
    
    suma =  y + z + x - 1
print ("La suma de los resultado es  :",suma)
