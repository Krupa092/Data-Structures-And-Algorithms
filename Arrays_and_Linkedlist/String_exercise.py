# Common string methods
str1 = "Krupa Dave"

#Changing Case
#krupadave
print(str1.lower())
#KRUPADAVE
print(str1.upper())

#Slicing
print(str1[1:6]) 		# rupa
print(str1[:6])			# Krupa. A blank index means "all from that end starting from beginning"
print(str1[1:])			# rupa Dave

#Strip
str2 = "    KrupaDave    "
print(str2.strip()) #remove white spaces

#Replace/Substitute a charecter in the string 
print(str1.replace('K','N')) #Nrupa Dave

# Cocatnation
str3 = "Welcome"
print(str3 +" " +str1)
marks = 100
print(str3 + " You have scored a perfect " + format(marks)) # format() method converts the argument as a formatted string 
#Welcome You have scored a perfect 100

#Split in to sub strings
print(str1.split(" ")) #['Krupa', 'Dave']

#Sorting
print(sorted(str3)) #['W', 'c', 'e', 'e', 'l', 'm', 'o']

#EXCERCISE 1
def string_reverser(our_string):
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """

    # New empty string for us to build on
    new_string = ""

    # Iterate over old string
    for i in range(len(our_string)):
        # Grab the charecter from the back of the string and add them to the new string
        a=len(our_string)
        b=(a-1)-i
        c=our_string[b]
        new_string += our_string[(len(our_string)-1)-i]
        

    # Return our solution
    return new_string
# Test Cases
print (string_reverser('water'))
print (string_reverser('Practicing string manipulation!'))
print (string_reverser('The house code is: 2343'))


print ("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")

#EXERCISE 2
#Anagram Checker
#"rat" is an anagram of "art"
#"alert" is an anagram of "alter"
#"Slot machines" is an anagram of "Cash lost in me"
def anagram_checker(str1, str2):
    
    """
    Check if the input strings are anagrams

    Args:
       str1(string),str2(string): Strings to be checked if they are anagrams
    Returns:
       bool: If strings are anagrams or not
    """

    # Clean strings and convert to lower case
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Compare the length of both strings
    if len(str1) == len(str2):
        # Sort each string and compare
        if sorted(str1) == sorted(str2):
            return True

    return False


print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")
print ("Pass" if (anagram_checker('rat','art')) else "Fail")

#EXERCISE 3
def word_flipper(our_string):
    
    """
    Flip the individual words in a sentence

    Args:
       our_string(string): Strings to have individual words flip
    Returns:
       string: String with words flipped
    """

    word_list = our_string.split(" ")

    for idx in range(len(word_list)):
        word_list[idx] = word_list[idx][::-1]

    return " ".join(word_list)

print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")

def hamming_distance(str1, str2):
    
    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """

    if len(str1) == len(str2):
        count = 0

        for char in range(len(str1)):
            if str1[char] != str2[char]:
                count+=1

        return count

    return None
print ("Pass" if (10 == hamming_distance('ACTTGACCGGG','GATCCGGTACA')) else "Fail")
print ("Pass" if  (1 == hamming_distance('shove','stove')) else "Fail")
print ("Pass" if  (None == hamming_distance('Slot machines', 'Cash lost in me')) else "Fail")
print ("Pass" if  (9 == hamming_distance('A gentleman','Elegant men')) else "Fail")
print ("Pass" if  (2 == hamming_distance('0101010100011101','0101010100010001')) else "Fail")
