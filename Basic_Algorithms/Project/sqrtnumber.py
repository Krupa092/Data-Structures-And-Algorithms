def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    #if number is null or nagative
    if number is None:
        return None
    if number <0:
        return -1
    lower = 0
    higher = number
    while lower <= higher: 
        middle = (lower+higher)//2 # int division
        if ((middle * middle)<= number) and ((middle + 1)*(middle + 1) > number):
            return middle
        elif (middle * middle < number):
            lower = middle + 1 
        else:
            higher = middle - 1 

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")