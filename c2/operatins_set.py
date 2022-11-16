set_a = {'col','mex','bol'}
set_b = {'pe','bol'}

#Union con metodo
set_c = set_a.union(set_b)
print(set_c)
# Union con operador  |
print(set_a | set_b)

#inresection con metodo
set_d = set_a.intersection(set_b)
print(set_d)
#inresection con operador &
print(set_a & set_b)

#Diference con metodo
set_c = set_a.difference(set_b)
print(set_c)
#Diference con operador -
print(set_a - set_b)

#symetric diference con metodo
set_c = set_a.symmetric_difference(set_b)
print(set_c)
#symetric diference con operador ^
print(set_a ^ set_b)