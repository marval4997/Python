#OPERADORES ARITMÉTICOS
operadorA=3
operadorB=2
suma= operadorA + operadorB
print('Resultado suma', suma)
print(f'Resultado suma: {suma}')

resta= operadorA-operadorB
print(f'Resultado resta: {resta}')

multiplicasion= operadorA*operadorB
print(f'Resultado multiplicacion: {multiplicasion}')

divicion= operadorA/operadorB
print(f'Resultado divicion: {divicion}')

divicion= operadorA//operadorB
print(f'Resultado divicion: {divicion}')

modulo= operadorA%operadorB
print(f'Resultado del residuo de la divicion (modulo): {modulo}')

exponenete= operadorA**operadorB
print(f'Resultado de exponente: {exponenete}')

#EJERCICIO CALCULAR EL AREA Y EL PERÍMETRO DE UN RECTÁNGULO

print("calular area y perimetro de un rectangulo")
alto=int(input("alto del rectangulo: "))
ancho= int(input("ancho del rectangulo: "))

area= alto*ancho
perimetro = (alto+ ancho)*2

print("Area:",area)
print("Perimetro:",perimetro)

