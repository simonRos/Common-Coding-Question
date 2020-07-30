from functools import wraps

def no_empty_arrays(func):
    '''Prevents function from being fed an empty array'''
    @wraps(func)
    def inner(*args, **kwargs):
        if type(*args) != list or len(*args) == 0:
            return None
        else:
            return func(*args, **kwargs)
    return inner


@no_empty_arrays
def find_largest(input_array):
    '''return largest element of array without using max()'''
    largest = input_array[0]
    for i in input_array:
        if i > largest:
            largest = i
    return largest


@no_empty_arrays
def find_smallest(input_array):
    '''return smallest element of array without using min()'''
    smallest = input_array[0]
    for i in input_array:
        if i < smallest:
            smallest = i
    return smallest


@no_empty_arrays
def find_both(input_array):
    '''return largest and smallest element of array without using min() or max()'''
    largest, smallest = input_array[0], input_array[0]
    for i in input_array:
        if i > largest:
            largest = i
        elif i < smallest:
            smallest = i
    return (smallest, largest)
