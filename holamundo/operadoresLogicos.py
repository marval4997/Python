#OPERADORES LOGICOS

a=False
b=False

resultado = a and b #necesita que los dos valores sean verdaderos
print(resultado)

resultado= a or b #necesita que almenos un valor sea verdadero 
print(resultado)

resultado =not a #not niega el valor
print(resultado)

#ejercicio valores dentro dl rango
a=int(input("Ingresa un valor entre 1 y 5: "))

if a>=0 and a<=5:
    print(f'el numero {a} se encuentra dentro del rango 1-5')
else:
    print(f'el numero {a} se encuentra fuera del rango 1-5')

#EJERCICIO DETERMINAR SI LA EDAD DE UN PERSONA ESTA ENTRE 20 Y 30

edad = int(input("Ingresa tu edad: "))

if (edad>= 20 and edad <30)or(edad>=30 and edad <40):
    print(f'Tu edad {edad} esta entre los 20s y 30s')
else:
    print(f'Tu edad {edad} no esta entre los 20s y 30s')

#DETERMINAR EL NUMERO MAYOR DE DOS NUMEROS

int1=int(input("Ingresa el numero 1: "))
int2=int(input("Ingresa el numero 2: "))

if int1 > int2:
    print(f'El numero mayor ente {int1} y {int2} es {int1}')
elif int2 > int1:
    print(f'El numero mayor ente {int1} y {int2} es {int2}')
else:
    print("Los numero son iguales")

#ejrcico tienda de libro
#SIMPLIFICACION DEL IF OPERADOR TERNARIO

condicion = True

if condicion:
    print("condicion verdadera")
else:
    print("condicion falsa")

print("condicion verdadera") if condicion else print("condicion falsa")
