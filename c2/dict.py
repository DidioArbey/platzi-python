import random

dict = {}
for i in range(1,5):
    dict[i] = i*2
print(dict)
#comprensetions

dict_2 = {i:i*2 for i in range(1,5)}
print(dict_2)

countries = ['col','mex','bol','pe']
population ={}
for country in countries:
    population[country] = random.randint(1,100)
print(population)

population2 = {country:random.randint(1,100) for country in countries}
print(population2)

names = ['didio','daniel', 'luis']
ages = [27,25,34]

print(list(zip(names,ages)))

newDict = {name:age for (name,age) in zip(names,ages)}
print(newDict)



