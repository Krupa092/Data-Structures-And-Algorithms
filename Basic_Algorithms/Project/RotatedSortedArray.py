def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    _len = len(input_list) # internal length function which is size of list 

    right_index,left_index,pivot_number = 0, _len,0


    #while right_index <= left_index:
    while True:
        pivot_number = (right_index + left_index) // 2 #int division
        if input_list[0] < input_list[_len-1] or pivot_number == _len -  1:
            pivot_number = 0
            break
        if input_list[pivot_number - 1] > input_list[pivot_number]:
            break 
        elif  input_list[0] > input_list[pivot_number]:
            left_index = pivot_number
        elif input_list[0] < input_list[pivot_number]:
            right_index = pivot_number
        
        
    if input_list[pivot_number] <= number <= input_list [_len - 1]:
        right_index = pivot_number 
        left_index = _len
    else:
        right_index = 0
        left_index = pivot_number

    while right_index <= left_index:
        pivot_number = (right_index + left_index) // 2
        if input_list[pivot_number] == number:
            return pivot_number
        elif input_list[pivot_number] < number:
            right_index = pivot_number + 1
        else:
            left_index = pivot_number - 1
    return -1
    

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])