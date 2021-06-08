"""Task 02: add a constructor that takes the value as a parameter 
"""
# Create a Node class 
class Node:
    #Define constructor function
    def __init__(self, value = None ): #because the default value of "value" is None
        #assign variables, because it is tree structure 
        self.value = value  
        self.left = None 
        self.right = None

#Test Functions
node0 = Node()
print(f"""
value: {node0.value}
left: {node0.left}
right: {node0.right}
""")

#adding value to test function
node1=Node("apple")
print(f"""
value: {node1.value}
left: {node1.left}
right: {node1.right}
""")
