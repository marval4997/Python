# condicion = True

# while condicion:
#     print("ciclo while")
# else:
#     print("fin del ciclo")

contador =10

while contador>=0:
    print(contador)
    contador-=1
else:
    print("fin del ciclo")

#CICLO FOR

cadena= "hola"

for letra in cadena:
    print(letra)
else:
    print("fin del ciclo for")

#break continue

pais= "Canada"

for a in pais:
    if a =="a":
        print(a)
        break
else:
    print("fin del ciclo")