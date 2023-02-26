#diccionarios
diccionario={
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}

print(diccionario)

#largo
print(len(diccionario))
#acceder a un elemento (key)
print(diccionario['IDE'])
print(diccionario.get('OOP'))

#modificar elementos
diccionario['IDE']='integrated development environment'
print(diccionario)

for key, valor in diccionario.items():#regresa la llave y el valor
    print(key, valor)

for key in diccionario.keys():#regresa la llave
    print(key)

for valor in diccionario.values():#regresa el valor
    print(valor)

#comprovar exixtencia de un elemento
print('IDE' in diccionario)

#agregar elemntos
diccionario['PK']='Primary Key'
print(diccionario)

#remover elementos
diccionario.pop('IDE')
print(diccionario)

#limpiar el diccionario
diccionario.clear()
print(diccionario)

#eliminar la variable
del(diccionario)

print(diccionario)