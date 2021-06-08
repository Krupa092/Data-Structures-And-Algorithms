def use_while_find_fact():
    # number to find the factorial of
    number = 6 
    # start with our product equal to one
    product = 1
    # track the current number being multiplied
    current = 1
    # write your while loop here
    while current <= number:
        product *=current 
        # multiply the product so far by the current number
        current+=1
        # increment current with each iteration until it reaches number
    # print the factorial of number
    print("The factorial of nummber {} is {}" .format(number,product))

def use_for_find_fact():
    number=6 
    product=1
    for num in range(2, number + 1):
        product *= num

def while_loop():
    #Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num. 
    # Use break_num as the variable that you'll change each time through the loop. 
    # For simplicity, assume that end_num is always larger than start_num and count_by is always positive.
    start_num = 2#provide some start number
    end_num = 11#provide some end number that you stop when you hit
    count_by = 2#provide some number to count by 
    # write a while loop that uses break_num as the ongoing number to 
    #   check against end_num
    break_num = start_num
    while break_num < end_num:
        break_num += count_by
        print(break_num)

def count_by_check():
    start_num =1 #provide some start number
    end_num =20 #provide some end number that you stop when you hit
    count_by =2 #provide some number to count by 

    # write a condition to check that end_num is larger than start_num before looping
    # write a while loop that uses break_num as the ongoing number to 
    #   check against end_num
    result = start_num
    if start_num > end_num:
        print("Oops! Looks like your start value is greater than the end value. Please try again.")
    else:
        for result in range(start_num,end_num,count_by):
            result+=count_by
            print(result)

def Nearest_Square():
    #Write a while loop that finds the largest square number less than an integerlimit and stores it in a variable nearest_square.
    #A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.
    #For example, if limit is 40, your code should set the nearest_square to 36.
    limit = 40
    # write your while loop here
    num = 0
    while (num+1)**2 < limit:
        num += 1
    nearest_square = num**2
    print(nearest_square)

def loop_to_use():
    # Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together.
    num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
    count_odd = 0
    list_sum = 0
    i = 0
    len_num_list = len(num_list)

    while (count_odd < 5) and (i < len_num_list): 
        if num_list[i] % 2 != 0:
            list_sum += num_list[i]
            count_odd += 1
        i += 1
    print ("The numbers of odd numbers added are: {}".format(count_odd))
    print ("The sum of the odd numbers added is: {}".format(list_sum))