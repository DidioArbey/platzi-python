#parametros por defecto y multiples return

def find_volume (length=1, width=1,depth=1):
    return length * width * depth

result = find_volume(width=10)

print(result)

def funciontupla ( val1=1,val2=1,val3=1):
    return val1+val2+val3, val1*val2*val2,'este es el ultimo valor'

res = funciontupla (val2=3)
print(res[2])