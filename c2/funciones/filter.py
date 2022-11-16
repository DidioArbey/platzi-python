numbers = [1,2,3,4,5,6,7,8,9,10]
pares = list(filter(lambda x: x % 2 ==0,numbers))
impares = list(filter(lambda x:x%2 != 0,numbers))
print(pares)
print(impares)