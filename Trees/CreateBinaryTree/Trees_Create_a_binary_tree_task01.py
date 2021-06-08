"""
Task 01: build a node
on a piece of paper, draw a tree.
Define a node, what are the three things you'd expect in a node?
Define class called Node, and define a constructor that takes no arguments, and sets the three instance variables to None.
Note: coding from a blank cell (or blank piece of paper) is good practice for interviews!
"""
# Create a Node class 
class Node:
    #Define constructor function
    def __init__(self):
        #assign variables, because it is tree structure 
        self.value = None 
        self.left = None 
        self.right = None
#Test Function
node0 = Node()
print(f"""
value: {node0.value}
left: {node0.left}
right: {node0.right}
""")


