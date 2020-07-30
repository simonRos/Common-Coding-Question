import random
from quicksort import quicksort

example = []
#already sorted
example.append([-10,-5,-1.1,2,3,4.4,5,6,11])
#not sorted
example.append([5,6,-10,-1.1,2,11,4.4,3,-5])
#backwards
example.append([11,6,5,4.4,3,2,-1.1,-5,-10])
#with duplicates
#note that 7 == 7.0 so they are sorted arbitrarily relative to each other.
example.append([0.1,0.1,-5,-5,7,7.0,7,7,7,7.0,8,10,9])
#random numbers
rands = []
for x in range(10):
    rands.append(round(random.random(),2))
example.append(rands)

for e in example:
    print(quicksort(e))
