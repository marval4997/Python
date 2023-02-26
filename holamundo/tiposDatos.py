#tipos de datos
#Tipo int
x=10
#print(type(x))
#Tipo float
x=14.5
#print(type(x))
#Tipo String
x="Hola Mundo"
#print(type(x))
#Tipo bool
x=False
#print(type(x))

x: str="hola mundo" # (: str,int) es una pista pero la bariable pude cambiat su tipo de dato
y= False
#print(type(x))#type() muestra el tipo de dato de la variable
#print(type(y))

#MANEJO DE CADENAS

miGrupoFavorito= "Los cadetes de linares"
comentario="el mejor grupo"

print("Mi grupo favorito es:",miGrupoFavorito,comentario)#concatenacion de cadenas
print("Mi grupo favorito es: " + miGrupoFavorito)#concatenación de cadenas 


numero1="10"
numero2="2"


print ("concatenación ",numero1+numero2)
print("suma: ", int(numero1)+int(numero2))


#TIPO BOOL(BOOLEAN)
miVariable=True
print(miVariable)

miVariable= 7>6
print(miVariable)

if miVariable:
    print("el resutado fue verdadero")

else:
    print("el resultado fue falso")
    
#FUNCIÓN INPUT PARA PROCESAR LA ENTRADA DEL USUARIO
#resultado = input("ingresa un mensaj: ")#input() entrada des datos por medio de consola
#print("valor ingresado:",resultado)
print("Fin del programa")

#suma de dos valores solicitados al usuario
#int1=int(input("ingresa el primer numero: "))
#int2=int(input("ingresa el segundo numero: "))

#suma=int1+int2
#print("El resutado de la suma es: ", suma)
print("fin del programa")

#EJERCICIO CALIFICA TU DIA DEL 1 AL 10
print("CALIFICA TU DIA DL 1 AL 10")
numero=int(input("calificación de tu dia: "))

if numero <=10:
    print("tu dia estuvo de ", numero)
else:
    print("ingresa un numero entre 1 y 10")


print("Fin del programa")

#EJERCICIO SE SOLICITA INCLUIR LA SIGUIENTE INFORMACION ACERCA DE UN LIBRO
#TITULO
#AUTOR
print("INFORMACION DEL LIBRO")
titulo=input("Titulo del libro: ")
autor=input("Autor del libro: ")

print(titulo,"fue escrito por:",autor)
