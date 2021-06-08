"""Heapsort
A heapsort is an in-place sorting algorithm that treats an array like a binary tree and moves the largest values to the end of the heap until the full array is sorted.

The main steps in a heapsort are:

Convert the array into a maxheap (a complete binary tree with decreasing values)
Swap the top element with the last element in the array (putting it in it's correct final position)
Repeat with arr[:len(arr)-1] (all but the sorted elements)"""   

 #code a heapsort function that takes an array (or Python list) and performs a heapsort on it. You will have to complete the heapify

def heapify(arr, n, i):
    # Using i as the index of the current node, find the 2 child nodes (if the array were a binary tree)
    # and find the largest value.   If one of the children is larger swap the values and recurse into that subree
    
    # consider current index as largest
    largest_index = i 
    left_node = 2 * i + 1     
    right_node = 2 * i + 2     
  
    # compare with left child
    if left_node < n and arr[i] < arr[left_node]: 
        largest_index = left_node
  
    # compare with right child
    if right_node < n and arr[largest_index] < arr[right_node]: 
        largest_index = right_node
  
    # if either of left / right child is the largest node
    if largest_index != i: 
        arr[i], arr[largest_index] = arr[largest_index], arr[i] 
    
        heapify(arr, n, largest_index) 
        
def heapsort(arr):
    # First convert the array into a maxheap by calling heapify on each node, starting from the end   
    # now that you have a maxheap, you can swap the first element (largest) to the end (final position)
    # and make the array minus the last element into maxheap again.  Continue to do this until the whole
    # array is sorted
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 

def test_function(test_case):
    heapsort(test_case[0])
    if test_case[0] == test_case[1]:
        print("Pass")
    else:
        print("False")

arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
test_case = [arr, solution]
test_function(test_case)

arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
test_case = [arr, solution]
test_function(test_case)

arr = [99]
solution = [99]
test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 2, 5, 12, 21, 0]
solution = [0, 0, 1, 2, 5, 12, 21]
test_case = [arr, solution]
test_function(test_case)
