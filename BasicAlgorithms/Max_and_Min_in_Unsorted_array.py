def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return
    result = [-float('inf'), float('inf')]
    for _int in ints:
        if _int > result[0]:
            result[0] = _int
        if _int < result[1]:
            result[1] = _int
    return (result[1], result[0])

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")