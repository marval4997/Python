def miFuncion(nombre):
    print('saludos desde mi fucnion',nombre)

miFuncion('Margarito')

def suma(n1=0,n2=0):#valores por defecto 
    operacion=n1+n2
    return operacion

resultado=suma()#se inicializan los valores por defecto
resultado2=suma(2,8)#toma los valores enviados

print(resultado)
print(resultado2)

#ARGUMRNTOS VARIABLES

def listarNombres(*nombres):#los datos se manejan como una tupla
    for nombre in nombres:
        print(nombre)

listarNombres('margarito','juan','maria')   

""" 
crear una función para sumar los valores recibidos de tipo numérico
con argumentos variables y regresando la suma de los argumentos
"""

def argsVariables(*args):
    total=0
    for arg in args:
        total +=arg

    return total
    
args=argsVariables(1,2,3,4,5)
print(args)    

"""
crear una funcion que reciba argumentos variables y regrese la multiplicacion de estos argumentos
"""

def multiplicadionArgs(*args):
    total=0
    for arg in args:
        if total==0:
            total=arg
        else:
            total*=arg

    return total


multiplicacion=multiplicadionArgs(1,2,3)
print(multiplicacion)

"""
funcion para listar terminos de un diccionario
"""

def terminosDiccionario(**datos):
    for key , valor in datos.items():
        print(key,valor)

diccionario={
    'nombre':'juan',
    'apellido':'alvares',
    'edad':10
}

terminosDiccionario(nombre='juan', apellido='alvares', edad=20)

#///////////////////
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres=['Juan', 'Karla']     
print(desplegarNombres(nombres))   

"""
funcion que calcule el factorial de un numero
"""

def factorial(numero):
    resultado=1
    while numero>=1:
        resultado *=numero
        numero -=1
    return resultado

resultado=factorial(5)
print(resultado)    

def factorialRecursivo(numero):
    if numero ==1:
        return 1
    else:
        return numero*factorialRecursivo(numero-1)
    
print(factorialRecursivo(5))    

"""
imprimir valores de manera recursiva
"""
def recursividad(n):

    if n>=1:
        print(n)
        recursividad(n-1)   


recursividad(5)

"""
funcion que realice el calculo de impuestos y retorne el valor con el impuesto
"""
def impuestos(porcentaje, precio):
    impuesto=((precio*porcentaje)/100)+precio
    return impuesto

print(impuestos(16,1000))

"""
funcion para convertir grados Celsius a Fahrenheit i viceversa 
"""
def Celsius_Fahrenheit(c):
    Fahrenheit= (c*1.8)+32
    return Fahrenheit

def Fahrenheit_Celsius(f):
    celsius=(f-32)/1.8
    return celsius

print(Celsius_Fahrenheit(20))
print(Fahrenheit_Celsius(30))
print(9/5)