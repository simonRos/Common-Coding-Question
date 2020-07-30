def find_pairs_equal_to_sum(input_array, desired_sum):
    '''input_array and desired sum, output pairs equal to sum'''
    output_pairs = set()
    for left in range(0, len(input_array)):
        right = left + 1
        while right < len(input_array):
            if input_array[left] + input_array[right] == desired_sum:
                output_pairs.add((input_array[left], input_array[right]))
            right += 1
    return list(output_pairs)
