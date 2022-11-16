# sum =0
# for x in range(1,11):
#     sum +=x
# print(sum)

#funciones con return

def sum_wirh_range(min:int,max:int):
    """_summary_

    Args:
        min (int): numero inicial del rango a iterar
        max (int): numero hasta el cual se quiere iterar el rango
    """
    sum=0
    for x in range(min,max):
        sum+=x
    return sum

result = sum_wirh_range(1, 10)
print(result)

