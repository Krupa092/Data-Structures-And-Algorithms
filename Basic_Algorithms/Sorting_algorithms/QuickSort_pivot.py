"""
QuickSort
Like MergeSort, QuickSort is a divide-and-conquer algorithm. 
We need to pick a pivot, then sort both sublists that are created on either side of the pivot. 
Similar to the video, we'll follow the convention of picking the last element as the pivot.

Start with our unordered list of items:
"""
items = [8, 3, 1, 7, 0, 10, 2]
pivot_index = len(items) - 1
pivot_value = items[pivot_index]
"""
We can use len to grab the pivot value, but in order to sort in-place we'll also want the index of the pivot.
Because we plan on sorting in-place, we want to iterate through the items to the left of our pivot (left_items). 
When they're larger than pivot_value though, we will not increment our position through left_items, but instead change pivot_index. 
We'll know we're done with this pass when pivot_index and left_items index are equal.
"""
left_index = 0

while (pivot_index != left_index):
    
    item = items[left_index]
    
    if item <= pivot_value:
        left_index += 1
        continue
    
    # Place the item before the pivot at left_index
    items[left_index] = items[pivot_index - 1]
    # Shift pivot one to the left
    items[pivot_index - 1] = pivot_value
    # Place item at pivot's previous location
    items[pivot_index] = item
    # Update pivot_index
    pivot_index -= 1

print(items)
        