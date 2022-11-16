items = [
    {
        'producto':'ender3',
        'precio': 890
    },
    {
        'producto':'PLA',
        'precio':75
    },
    {
        'producto':'ABS',
        'precio':100
    }
]

precio = list(map(lambda item: item['precio'], items ))
print(precio)

#agregar un atributo al dicionario y calcular su valor
#declarar funcion para crear el nuevo item
def agregar_impuesto (item):
    item['impuesto'] = item['precio']*.19
    return item
#agregar el nuevo item al diccionario
nuevo_item = list(map(agregar_impuesto,items))
print(nuevo_item)
print(items)
