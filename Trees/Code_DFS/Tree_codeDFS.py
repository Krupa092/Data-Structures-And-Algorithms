"""
Traversing a tree means "visiting" all the nodes in the tree once. 
Unlike an array or linked list, there's more than one way to walk through a tree, starting from the root node.
Traversing a tree is helpful for printing out all the values stored in the tree, 
as well as searching for a value in a tree, inserting into or deleting values from the tree. 
There's depth first search and breadth first search.
"""
#Pre-Order-Traversal
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None 
        self.right = None 
    def set_value(self,value):
        self.value = value
    def get_value(self):
        return self.value 
    def set_left_child(self,left):
        self.left = left
    def set_right_child(self,right):
        self.right = right
    def get_left_child(self):
        return self.left
    def get_right_child(self):
        return self.right
    def has_left_child(self):
        return self.left != None
    def has_right_child(self):
        return self.right != None 
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"  
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root

# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))
class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
    
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"
# check Stack
stack = Stack()
stack.push("apple")
stack.push("banana")
stack.push("cherry")
stack.push("dates")
print(stack.pop()) 
print("\n")
print(stack)

visit_order = list()
stack = Stack()

# start at the root node, visit it and then add it to the stack
node = tree.get_root()
stack.push(node)

print(f"""
visit_order {visit_order} 
stack:
{stack}
""")
# visit apple
visit_order.append(node.get_value())
print(f"""visit order {visit_order}
{stack}
""")
# check if apple has a left child
print(f"{node} has left child? {node.has_left_child()}")

# since apple has a left child (banana)
# we'll visit banana and add it to the stack
if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

print(f"""
visit_order {visit_order} 
stack:
{stack}
""")
# visit banana
print(f"visit {node}")
visit_order.append(node.get_value())
print(f"""visit_order {visit_order}""")

# check if banana has a left child
print(f"{node} has left child? {node.has_left_child()}")

# since banana has a left child "dates"
# we'll visit "dates" and add it to the stack
if node.has_left_child():
    node = node.get_left_child()    
    stack.push(node)
    
print(f"""
visit_order {visit_order} 
stack:
{stack}
""")
# visit dates
visit_order.append(node.get_value())
print(f"visit order {visit_order}")
# check if "dates" has a left child
print(f"{node} has left child? {node.has_left_child()}")
# since dates doesn't have a left child, we'll check if it has a right child
print(f"{node} has right child? {node.has_right_child()}")
# since "dates" is a leaf node (has no children), we can start to retrace our steps
# in other words, we can pop it off the stack.
print(stack.pop())
print(stack)
# now we'll set the node to the new top of the stack, which is banana
node = stack.top()
print(node)
# we already checked for banana's left child, so we'll check for its right child
print(f"{node} has right child? {node.has_right_child()}")
# banana doesn't have a right child, so we're also done tracking it.
# so we can pop banana off the stack
print(f"pop {stack.pop()} off stack")
print(f"""
stack
{stack}
""")
# now we'll track the new top of the stack, which is apple
node = stack.top()
print(node)
# we've already checked if apple has a left child; we'll check if it has a right child
print(f"{node} has right child? {node.has_right_child()}")
# since it has a right child (cherry), 
# we'll visit cherry and add it to the stack.
if node.has_right_child():
    node = node.get_right_child()
    stack.push(node)
    
print(f"""
visit_order {visit_order} 
stack
{stack}
""")
    
# visit cherry
print(f"visit {node}")
visit_order.append(node.get_value())
print(f"""visit_order: {visit_order}""")
# Now we'll check if cherry has a left child
print(f"{node} has left child? {node.has_left_child()}")
# it doesn't, so we'll check if it has a right child
print(f"{node} has right child? {node.has_right_child()}")
# since cherry has neither left nor right child nodes,
# we are done tracking it, and can pop it off the stack
print(f"pop {stack.pop()} off the stack")
print(f"""
visit_order {visit_order} 
stack
{stack}
""")