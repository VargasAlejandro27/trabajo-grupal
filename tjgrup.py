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
