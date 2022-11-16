def increment(x):
    return x+1

def hof(x,funcion):
    return x + funcion(x)

result = hof(2,increment)
#2+(2+1)
print(result)

#ejemplo con lambdas

# increment = lambda x: x+1
# hof2 = lambda x, func : x + func(X)

# result = hof2 (2,increment)
# print(result)