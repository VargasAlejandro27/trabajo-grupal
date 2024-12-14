### EJERCICIO 2: NÚMEROS PRIMOS EN UN RANGO 
inicio = int(input("Ingrese el inicio"))
final= int(input("Ingrese el final"))
for i in range(inicio,final + 1,1):
    esPrimo=True
    for j in range(2,i,1):
        if (i%j==0):
            esPrimo=False
            break
    if(esPrimo):
        print(i)  




        

                
    
    