from cheap_bst import *
import random

example = []
example.append([1,2,3,4,5,6,7,6,5,3,2,4,6,9])
example.append([9.0,8.3,5.5,6,7,7,5,3,3.4,3.5,3.33,9.1,6.10,11,34])
rands = []
for i in range(24):
    rands.append(round(random.random(),2))
example.append(rands)
                 
##for e in example:
##    my_ll = BST()
##    for f in e:
##        my_ll.insert(f)
##    my_ll.print_tiered(True)
##    print("------")

for i in range(100):
    new_rands = []
    for j in range(40):
        new_rands.append(round(random.random(),2))
    ll = BST()
    for e in new_rands:
        ll.insert(e)
    ll.print_tiered()
    print('--------')
