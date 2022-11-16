# numbers =[]
# for element in range(1,11):
#     numbers.append(element*2)
# print(numbers)

# numbersV2=[element * 2 for element in range(1,11)]
# print(numbersV2)

numbersV3 =[]
for i in range(1,11):
    if i % 2 ==0:
        numbersV3.append(i*2)
print(numbersV3)

numbersV4=[i * 2 for i in range(1,11) if i %2 ==0]
print(numbersV4)
