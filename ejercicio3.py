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