"""
Write a python script to calculate average of elements of a list
"""
"""
?My Approach:
    1. Calculate sum of all intigers
    2. find length of list and devide the sum by length
"""

def average(list):
    length = len(list)
    sum = 0

    for x in list:
        sum += x

    result = sum/length
    return result

list = [0,1,2,3,4,5]
result = average(list)
print(result)