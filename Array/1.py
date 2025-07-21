"""
Given an array with some intiger type values. write a python script to sort an array values?
"""

"""
?My Approach:
    1. find the smallest value
    2. append it to empty array
    3. remove that smallest value from original array
    *now smallest value is removed means new smallest value is greater than previous one.
    return sorted array
"""

def sort_array(array):
    original_array = array.copy()
    sorted_array = []

    # Loop untill original_array get empty
    while original_array:
        smallest_value = original_array[0]

        for x in original_array:
            if x < smallest_value:
                smallest_value = x

        sorted_array.append(smallest_value)
        original_array.remove(smallest_value)

    return sorted_array

array = [ 75,8,9,64,1,23 ]

print(sort_array(array))