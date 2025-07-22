
"""
Given a list of heterogenous elements. write a python script to remove all the non int values from the list.
"""
"""
?My Approach:
    !It's Wrong:
    1. check for type of each element
    2. if its not int then remove it
    !Reason:
        @When you remove item from original list, indexing of the list will mismatched and loop gets confused
    *Dont use built-in keywords such as list, sum, etc
"""

def remove_non_int(list):
    for x in list:
        if type(x) != int:
            list.remove(x)

    return list

list = ['one', 2, 3, 'four', True, 8, [1, 2], {1, 2}]

result = remove_non_int(list)

"""
?The correct way:
    1. create a new empty list.
    2. Add only the elements you want to keep.
"""

def remove_non_integer(num_list):
    int_only = []
    for x in num_list:
        if type(x) is int:
            int_only.append(x)
    return int_only

num_list = ['one', 2, 3, 'four', True, 8, [1, 2], {1, 2}]
result = remove_non_integer(num_list)
print(result)
