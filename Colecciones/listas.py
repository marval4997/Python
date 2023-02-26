nombres= ['margarito', 'juan', 'rodolfo', 'maria']

##acceder a los elementos de una lista
print(nombres)
print(nombres[0])

#acceder de manera inversa a los elementos de una listas

print(nombres[-1])

#rangos 
print(nombres[0:2])#sin incluir el indice 2
#ir del inicio de la lista sin icluirlo
print(nombres[:3])

#desde el indice indicado asta el final
print(nombres[1:])
#modificando indices
nombres[2]="ivone"

print(nombres)

for nombre in nombres:
    print(nombre)

#preguntar el largo de la lista
print(len(nombres))

#aggregar mas elemetos a la lista

nombres.append('denis')
print(nombres)

#insertar en un idice proporcionado
nombres.insert(0,'jesus')
print(nombres)

#eliminar un elemento
nombres.remove('juan')
print(nombres)
#eliminar el ultimo elemto de la lista
nombres.pop()
print(nombres)
#eliminar en un indice indicado
del nombres[0]
print(nombres)
#eliminar todos los elementos de la lista
nombres.clear()

#EJERCICIOS CON RANGOS range()
print("## EJERCICIO 1")
for i in range(10):
    if i%3 ==0:
        print(i)
else:
    print("fin del ciclo")        
    

print("## EJERCICIO 2")

for j in range(2,6):
    print(j)
else:
    print("Fin del ciclo")

print("## EJERCICIO 3")

for k in range(3,10,2):
    print(k)
else:
    print("fin del ciclo")  
