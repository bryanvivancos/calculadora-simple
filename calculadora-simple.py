#calculadora-simple 
n1 = float(input("ingrese un primer numero: "))
n2 = float(input("ingrese un segundo numero: ")) 

operacion = int(input("""Que operacion desea realizar:
1. Suma
2. Resta
3. Multiplicacion
4. Division
Ingrese el numero de la operacion: """))


while True: 
    if operacion == 1:
        resultado = n1+n2
        print(f"El resultado es: {resultado}")
        break
    elif operacion == 2:
        resultado = n1-n2
        print(f"El resultado es: {resultado}")
        break
    elif operacion == 3:
        resultado = n1*n2
        print(f"El resultado es: {resultado}")
        break
    elif operacion == 4:
        resultado = n1/n2
        print(f"El resultado es: {resultado}")
        break
    else:
        print(input("Ingrese numero valido: "))


