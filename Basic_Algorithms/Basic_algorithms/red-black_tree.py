class Node(object):
    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color
        
    def __repr__(self):
        print_color = 'R' if self.color == 'red' else 'B'
        return '%d%s' % (self.value, print_color)

def grandparent(node):
    if node.parent == None:
        return None
    return node.parent.parent

# Helper for finding the node's parent's sibling
def pibling(node):
    p = node.parent
    gp = grandparent(node)
    if gp == None:
        return None
    if p == gp.left:
        return gp.right
    if p == gp.right:
        return gp.left

class RedBlackTree(object):
    def __init__(self, root):
        self.root = Node(root, None, 'red')
        
    def __iter__(self):
        yield from self.root.__iter__()
        
    def insert(self, new_val):
        new_node = self.insert_helper(self.root, new_val)
        self.rebalance(new_node)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                return self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val, current, 'red')
                return current.right
        else:
            if current.left:
                return self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val, current, 'red')
                return current.left

    """
    Rotations
    At this point we are only making a BST, with extra attributes. 
    To make this a red-black tree, we need to add the extra sauce that makes red-black trees awesome.
    We will sketch out some more code for rebalancing the tree based on the case, and fill them in one at a time.

    First, we need to change our insert_helper to return the node that was inserted so we can interrogate it when rebalancing.
    """
    """
    Case 1
    We have just inserted the root node
    If we're enforcing that the root must be black, we change its color. 
    We are not enforcing this, so we are all done! Four to go.
    """
    """
    Case 2
    We inserted under a black parent node
    Thinking through this, we can observe the following: We inserted a red node beneath a black node. 
    The new children (the NULL nodes) are black by definition, and our red node replaced a black NULL node. 
    So the number of black nodes for any paths from parents is unchanged. Nothing to do in this case, either.
    """
    """
    Case 3
    The parent and its sibling of the newly inserted node are both red
    Okay, we're done with free cases. In this specific case, we can flip the color of the parent and its sibling. 
    We know they're both red in this case, which means the grandparent is black. 
    It will also need to flip. At that point we will have a freshly painted red node at the grandparent. 
    At that point, we need to do the same evaluation! If the grandparent turns red, and its sibling is also red, that's case 3 again. 
    Guess what that means! Time for more recursion.
    We will define the grandparent and pibling (a parent's sibling) methods later, for now let's focus on the core logic.
    """
    """
    Case 4
    The newly inserted node has a red parent, but that parent has a black sibling
    These last cases get more interesting. The criteria above actually govern case 4 and 5. 
    What separates them is if the newly inserted node is on the inside or the outside of the sub tree. 
    We define inside and outside like this:
    inside
        EITHER
            the new node is a left child of its parent, but its parent is a right child, or
            the new node is a right child of its parent, but its parent is a left child
    outside
            the opposite of inside, the new node and its parent are on the same side of the grandparent
    Case 4 is to handle the inside scenario. In this case, we need to rotate. 
    As we will see, this will not finish balancing the tree, but will now qualify for Case 5.
    We rotate against the inside-ness of the new node. If the new node qualifies for case 4, it needs to move into its parent's spot. 
    If it's on the right of the parent, that's a rotate left. If it's on the left of the parent, that's a rotate right.
    """
    def rebalance(self, node):    
        # Case 1
        if node.parent == None:
            return
        
        # Case 2
        if node.parent.color == 'black':
            return
        
        # Case 3
        if pibling(node) and pibling(node).color == 'red':
            pibling(node).color = 'black'
            node.parent.color = 'black'
            grandparent(node).color = 'red'
            return self.rebalance(grandparent(node))
        
        gp = grandparent(node)        
        # Small change, if there is no grandparent, cases 4 and 5
        # won't apply
        if gp == None:
            return
        
        # Case 4
        if gp.left and node == gp.left.right:
            self.rotate_left(node.parent)
            node = node.left
        elif gp.right and node == gp.right.left:
            self.rotate_right(node.parent)
            node = node.right

        # Case 5
        p = node.parent
        gp = p.parent
        if node == p.left:
            self.rotate_right(gp)
        else:
            self.rotate_left(gp)
        p.color = 'black'
        gp.color = 'red'

    def rotate_left(self, node):
        # Save off the parent of the sub-tree we're rotating
        p = node.parent

        node_moving_up = node.right
        # After 'node' moves up, the right child will now be a left child
        node.right = node_moving_up.left

        # 'node' moves down, to being a left child
        node_moving_up.left = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        # 'node' may have been the root
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p

    def rotate_right(self, node):
        p = node.parent

        node_moving_up = node.left
        node.left = node_moving_up.right

        node_moving_up.right = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p
def print_tree(node, level=0):
    print('   ' * (level - 1) + '+--' * (level > 0) + '%s' % node)
    if node.left:
        print_tree(node.left, level + 1)
    if node.right:
        print_tree(node.right, level + 1)
    
tree = RedBlackTree(9)
tree.insert(6)
tree.insert(19)

print_tree(tree.root)

tree.insert(13)
print_tree(tree.root)

tree.insert(16)
print_tree(tree.root)

"""
Further Exercises
To continue exploring our red-black tree implementation, you might try the following.

Observe that our current implementation will add duplicates of the same value. 
Is that desirable? How would you expect that to behave? Change the implementation to mark how many times the same value has been inserted.
Implement search and see how it remains logarithmic for large data sets
Tinker with the rotations and early escapes to see how they break (use print_tree)
Consider adding deletion or sketching out how it should work
"""