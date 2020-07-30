from find_pairs_equal_to_sum import find_pairs_equal_to_sum

options = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sums = [2,3,4,5,9,10,15,20]

for s in sums:
    print(str(s) + ': ' + str(find_pairs_equal_to_sum(options,s)))
