#operadores en Python
a = 4
b = 6

resultado = a==b
print(f'Resultado ==: {resultado}')

resultado = a!=b
print(f'Resultado !=: {resultado}')

resultado= a > b
print(f'Resultado >: {resultado}')

resultado= a >= b
print(f'Resultado >=: {resultado}')

resultado= a < b
print(f'Resultado <: {resultado}')

resultado= a <= b
print(f'Resultado >=: {resultado}')

#ejercicio numero par e impar

numero=int(input("ingresa un numero: "))



if numero%2 ==0:
    print("El numero:",numero,"es un numero par")
else:
    print("El numero",numero,"es un numero impar")

#ejercicio preguntar la edad del usuario y determinar si es mayor de edad o no

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print(f'La persona con edad {edad} es un adulto')
else:
    print(f'La persona con edad {edad} no es un adulto')