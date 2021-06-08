""" 
Task05: check if left or right child exist
Define functions has_left_child, has_right_child, so that they return true if the node has left child, or right child respectively.
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
    def has_left_child(self):
        return self.left != None 
        """another way 
        if self.left != None:
            return True 
        else:
            return False
        """
    def has_right_child(self):
        return self.right != None 
        """another way 
        if self.left != None:
            return True 
        else:
            return False
        """
## check

node0 = Node("apple")
node1 = Node("banana")
node2 = Node("orange")

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")

print("adding left and right children")
node0.set_left_child(node1)
node0.set_right_child(node2)

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")