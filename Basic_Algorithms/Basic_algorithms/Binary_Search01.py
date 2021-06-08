def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration
   
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
   
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    start_Index = 0
    end_Index = len(array)-1
    
    while start_Index <= end_Index:
        mid_Index = (start_Index + end_Index)//2 #division
        mid_Element =array[mid_Index]
        if target == mid_Element:
            return mid_Index
        elif target < mid_Element:
            end_Index = mid_Index-1
        else:
            start_Index = mid_Index+1
    return -1

def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)