"""
Task06: create a binary tree
Task07: setting root node in constructor
Let's modify the Tree constructor so that it takes an input that initializes the root node. 
Choose between one of two options: 1) the constructor takes a Node object
2) the constructor takes a value, then creates a new Node object using that value.
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
#Option 1
"""
class Tree(object):
    def __init__(self, node):
        self.root = node
    def get_root(self):
        return self.root
"""

#Option2 recommended 
class Tree(object):
    def __init__(self, value):
        self.root = Node (value)
    def get_root(self):
        return self.root
