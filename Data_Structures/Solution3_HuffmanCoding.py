import heapq
from collections import defaultdict
import operator
import sys

class NodeTree(object):
    def __init__(self, value, weight, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
        self.weight = weight
    def __lt__(self, node): # Given Iteration condition 
        return self.weight < node.weight
def get_frequency(string): # To get frequency of every charecters
    frequency = dict() # generating dictionary to store key(letters) and value(frequency) 
    for letter in string:
        if not letter in frequency:
            frequency[letter] = 0 #generate new key
        frequency[letter] += 1 #updating frequency 
    sorted_frequency = sorted(frequency.items(), key=operator.itemgetter(1)) 
    # print("Frequency AFTER sorting : ", sorted_frequency)
    for i in range(len(sorted_frequency)):
        value = sorted_frequency[i][0]
        weight = sorted_frequency[i][1]
        # print("VALUE: ",value, "WEIGHT: ", weight)
        sorted_frequency[i] = NodeTree(value, weight)
    # print("Sorted frecuency node tree objects: ", sorted_frequency)
    return sorted_frequency
def build_tree(data): #building tree to encode and decode the file
    heap = get_frequency(data)
    heapq.heapify(heap) # converting tree in to heap datastructure 
    while len(heap) != 1:
        new_node = NodeTree(None,None)
        left = heapq.heappop(heap) 
        new_node.left  = left
        right = heapq.heappop(heap)
        new_node.right  = right
        new_node.weight = left.weight + right.weight
        heapq.heappush(heap, new_node)
    return heap
def create_Huffcode_table(root): #Table generating to assign 0s and 1s to the left and right node respectively
    code = {}
    def getCode(hNode, currentCode=""):
        if (hNode == None):
            return
        if (hNode.left == None and hNode.right == None):
            code[hNode.value] = currentCode
        getCode(hNode.left, currentCode + "0") #get 0s to left node 
        getCode(hNode.right, currentCode + "1") #get 1s to right node 
    getCode(root[0])
    return code
def huffman_encode(data): 
    if(len(get_frequency(data))) == 1:
      return "0"*len(data)
    huff_code = ""
    root = build_tree(data)
    table = create_Huffcode_table(root)
    for item in data: #iterating words in the file 
       huff_code += table[item]
    return huff_code
def huffman_decode(bit_string, root):
    if (len(get_frequency(bit_string))) == 1:
        return len(bit_string) * str(root.value)
    decode = ""
    n = len(bit_string)
    count = 0
    while count < n:
        current = root[0]
        while current.left != None and current.right != None:
            if bit_string[count] == "0":
                current = current.left
            else:
                current = current.right
            count += 1
        decode += current.value
    return decode
def huffman_encoding(data):
    return huffman_encode(data), build_tree(data)
def huffman_decoding(data, tree):
    return huffman_decode(data, tree)

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
#***************************************************************************************************
    Huffman_Coding_Text = ("In computer science and information theory, "
    "a Huffman code is a particular type of optimal prefix code that is commonly used for lossless data compression."
    "The process of finding or using such a code proceeds by means of Huffman coding, an algorithm developed by David A."
    "Huffman while he was a Sc.D. student at MIT, and published in the 1952 paper (A Method for the Construction of Minimum-Redundancy Codes)."
    "The output from Huffman's algorithm can be viewed as a variable-length code table for encoding a source symbol (such as a character in a file)."
    "The algorithm derives this table from the estimated probability or frequency of occurrence (weight) for each possible value of the source symbol." 
    "As in other entropy encoding methods, more common symbols are generally represented using fewer bits than less common symbols."
    "Huffman's method can be efficiently implemented, finding a code in time linear to the number of input weights if these weights are sorted."
    "However, although optimal among methods encoding symbols separately, Huffman coding is not always optimal among all compression methods - "
    "it is replaced with arithmetic coding or asymmetric numeral systems if better compression ratio is required." )

    print ("The size of the data is: {}\n".format(sys.getsizeof(Huffman_Coding_Text)))
    print ("The content of the data is: {}\n".format(Huffman_Coding_Text))

    encoded_data, tree = huffman_encoding(Huffman_Coding_Text)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
#**************************************************************************************************
    repeating = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print ("The size of the data is: {}\n".format(sys.getsizeof(repeating)))
    print ("The content of the data is: {}\n".format(repeating))

    encoded_data, tree = huffman_encoding(repeating)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))