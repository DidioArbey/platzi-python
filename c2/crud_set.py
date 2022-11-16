set_contries ={'colombia','bolivia','mexico'}
#tamaño
size = len (set_contries)
print(size)
#preguntar si algo esta dentro del conjunto
print('colombia'in set_contries)
#add agregar un nuevo elemento en el conjunto
set_contries.add('peru')
print(set_contries)

#update actualizar el conjunto
set_contries.update({'argentina','ecuador','bolivia'})
print(set_contries)

#remove

set_contries.remove('ecuador')
print(set_contries)
#parea evitar que al momento de usar un remove y no exista y de error se usa el metodo discard
set_contries.discard('brasil')
print(set_contries)

#clear limpiar el conjunto
set_contries.clear()
print(set_contries)



