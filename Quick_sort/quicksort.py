def quicksort(arr):
    '''Returns sorted array using quicksort'''
    left = [] #less than pivot
    right = [] #greater than pivot
    pivot = []
    if len(arr) <= 1:
        #base case - we can't sort an array of size 0
        return arr
    else:
        for i in arr:
            if i < arr[0]:
                left.append(i)
            elif i > arr[0]:
                right.append(i)
            else:
                pivot.append(i)
        #recurse - we don't sort pivot because a homogenous list is sorted
        return quicksort(left) + pivot + quicksort(right)
