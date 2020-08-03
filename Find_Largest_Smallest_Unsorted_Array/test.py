from find_min_max import *

example = []
#basic
example.append([1,2,3,4,5,6,7,8,9])
#int, double, & negativ
example.append([9.3,9, 4.5, 5, 5, 5, 5.0, 3, 67, 0, -12.3])
#trick question 1
example.append([0,0,0,0,0,0,0,0,0])
#trick question 2
example.append([1,1,1,1,1,1])
#empty array
example.append([])

for e in example:
    print("Small: " + str(find_smallest(e)))
    print("Large: " + str(find_largest(e)))
    print("Both: " + str(find_both(e)) + '\n')
