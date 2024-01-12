liczby=[1,2,3,4,5]
liczby1=[]
for i in liczby:

    print(liczby1.append(i**2))


x=([i**2 for i in liczby])
print(x)

y=list(map(lambda x : x**2,liczby))
print(y)

z=list(filter(lambda x: x%2==0,liczby))
print(z)


h= {i: i**2 for i in liczby}
print(h)

import numpy as np
numbers_array = np.array(liczby)
squared_numbers = numbers_array + 1
print(liczby)
print(numbers_array)
print(squared_numbers)