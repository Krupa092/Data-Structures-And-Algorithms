"""
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. 
Return these two numbers. You can assume that all array elements are in the range [0, 9]. 
The number of digits in both the numbers cannot differ by more than 1. 
You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. 
Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.
"""
def merge_sort(i):
    if len(i) <= 1:
        return i

    middle_point = len(i) // 2 #int division 
    left_point = i[:middle_point] #list of numbers before mid point 
    right_point = i[middle_point:] #list of numbers after mid point 

    #recursion 
    left_point = merge_sort(left_point) 
    right_point = merge_sort(right_point)

    return merging(left_point, right_point)

def merging(left_point,right_point):
    index_left = 0
    index_right = 0
    merged_list = [] #empty list declaration for 
    while index_left < len(left_point) and index_right < len(right_point):
        if left_point[index_left] > right_point[index_right]:
            merged_list.append(right_point[index_right])
            index_right +=1
        else:
            merged_list.append(left_point[index_left])
            index_left += 1
    
    merged_list += left_point[index_left:]
    merged_list += right_point[index_right:]

    return merged_list

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0 or input_list == None:
        return -1
    if len(input_list) == 1:
        return input_list[0]

    input_list = merge_sort(input_list)
    input_list.reverse()
    num_ans1 = ""
    num_ans2 = ""

    for j in range (len(input_list)):
        if j % 2 == 0:
            num_ans1 += str(input_list[j])
        if j % 2 == 1:
            num_ans2 += str(input_list[j])

    return  int(num_ans1),int(num_ans2)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function ([[4, 6, 2, 5, 9, 8], [964, 852]])
    