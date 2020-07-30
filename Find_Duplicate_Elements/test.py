from find_dupe import find_dupe

example = []
example.append([1, 22, 2, 2, 3, 4, 5, 3])
example.append([1, 2, 3, 10, 'hello', 8.33, 7, 8.33, 'hi', '2', 1, 0, 'hi'])
#What is interesting about this third example is that
#True == 1
#False == 0
example.append([1, False, True, 0])

for ex in example:
    print(find_dupe(ex))
