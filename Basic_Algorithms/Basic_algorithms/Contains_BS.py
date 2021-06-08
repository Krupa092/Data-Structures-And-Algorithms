def recursive_binary_search(target, source):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center 
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:])
    else:
        return recursive_binary_search(target, source[:center])

def contains(target, source):
    return recursive_binary_search(target, source) is not None

letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters)) ## True
print(contains('b', letters)) ## False
"""
def contains1(target,source):
    if len(source) == 0:
        return False
    center = (len(source)-1)//2
    if source[center] == target:
        return center
    elif source[center] < target:
        return contains1(target,source[center+1:])
    else:
        return contains1(target,source[:center])
    
letters1 = ['a', 'c', 'd', 'f', 'g']
print(contains1('a', letters1)) ## True
print(contains1('b', letters1)) ## False
"""