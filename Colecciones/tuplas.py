#tuplas las tuplas nu puden ser midificadas

frutas = ('naranja', 'platano', 'guayaba')

print(len(frutas))
print(frutas[0])

frutasLista= list(frutas)

frutasLista[0]="pera"

frutas= tuple(frutasLista)

print(frutas)