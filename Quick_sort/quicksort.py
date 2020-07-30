def quicksort(arr):
    '''Returns sorted array using quicksort'''
    left = []
    right = []
    pivot = []
    if len(arr) <= 1:
        #base case
        return arr
    else:
        for i in arr:
            if i < arr[0]:
                left.append(i)
            elif i > arr[0]:
                right.append(i)
            else:
                pivot.append(i)
        return quicksort(left) + pivot + quicksort(right)
