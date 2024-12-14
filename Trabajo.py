x=int(input("Ingrese un numero"))
Suma=0
for i in range(1,x,1):
    if(x%i==0):
        Suma= Suma + i

if(Suma==x):
        print(f"El numero {x} ingresado  es perfecto")
else:
        print(f"El numero ingresado no es perfecto")
    