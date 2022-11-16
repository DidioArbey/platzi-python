#modelo convencional
numbers = [1,2,3,4]
numbersV2 = []
for i in numbers:
    numbersV2.append(i*2)

print(numbers)
print(numbersV2)

#utilizando map

numbersV3 = list(map(lambda i: i*2 ,numbers))
print(numbersV3)

#cuando se usa map para operar se presenta la anomalia de que toma el tamaño del elemento mas pequeño

numero1 =[1,2,3,4,5]
numero2 =[6,7,8,9]
numero3 = list(map(lambda x,y:x+y,numero1,numero2))
print(numero1)
print(numero2)
print(numero3)