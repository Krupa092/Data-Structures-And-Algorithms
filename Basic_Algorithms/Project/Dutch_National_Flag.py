"""
Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. 
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. 
For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.
"""
def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list == None:
        return None
    if input_list == []:
        return ("List is empty")
    i = 0 
    j = 0
    middle_point = 1
    l = len(input_list)-1
    while j <= l:
        if input_list[j] < middle_point:
            temp = input_list[i]
            input_list[i] = input_list[j]
            input_list[j] = temp
            i = i+1
            j = j+1
        elif input_list[j] > middle_point:
            temp = input_list[j]
            input_list[j] = input_list[l]
            input_list[l] = temp
            l = l-1
        else:
            j = j + 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([]) #fail, list is empty 
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]) #pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]) #pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) #pass