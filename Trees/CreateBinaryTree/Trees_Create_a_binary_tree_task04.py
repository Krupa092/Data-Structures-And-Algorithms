"""
Task04: add functions that assign left child and right child
Define a function set_left_child and a function set_right_child. 
Each function takes in a node that it assigns as the left or right child, respectively. 
Note that we can assume that this will replace any existing node if it's already assigned as a left or right child.
Also, define get_left_child and get_right_child functions.
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
        self.value = value
    def get_left_child(self):
        return self.left
    def get_right_child(self):
        return self.right
    def set_left_child(self,node):
        self.left = node
    def set_right_child(self,node):
        self.right = node
        
## check

node0 = Node("apple")
node1 = Node("banana")
node2 = Node("orange")
node0.set_left_child(node1)
node0.set_right_child(node2)

print(f"""
node 0: {node0.value}
node 0 left child: {node0.left.value}
node 0 right child: {node0.right.value}
""")