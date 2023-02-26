#set
#coleccion si orden y sin indices, no soporta elementos duplicados

planetas = {'marte', 'jupiter','venus'}
print(planetas)
#largo del set
print(len(planetas))
# revisar si un elemeto esta presente
print('marte' in planetas)
#agregar elemetos a un set
planetas.add('tierra')
planetas.add('tierra')
print(planetas)
#elimminar elementos
planetas.remove('tierra')
print(planetas)
planetas.discard('jupiters')
#limpiar el set
planetas.clear()
print(planetas)