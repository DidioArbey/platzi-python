import sys
print(sys.path)

import re
text ='Minumero de telefono 3167996375, el codigo del pais es el 57, mi numero de la suete es el 99'
result = re.findall ('[0-9]+',text)
print(result)

import time
timesa = time.time()
local = time.localtime()
result = time.asctime(local)
print(result)

import collections
numbers = [1,1,2,2,3,3,4,5,6]
counter = collections.Counter(numbers)
print(counter)