""" 
Task03: add functions to set and get the value of the node 
Add functions get_value and set_value
"""
class Node:
    #Define constructor function
    def __init__(self, value = None ): #because the default value of "value" is None
        #assign variables, because it is tree structure 
        self.value = value  
        self.left = None 
        self.right = None
    def get_value(self):
        return self.value
    def set_value(self,value):
        return self.value == value

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
