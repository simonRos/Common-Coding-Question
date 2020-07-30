# Function to print duplicates
def find_dupe(input_array):
    '''Input array of elements, output array of duplicate elements'''
    input_log = {}
    for i in input_array:
        if i not in input_log:
            input_log[i] = 1
        else:
            input_log[i] += 1   
    return [e for e in input_log.keys() if input_log[e] > 1]
        
        
