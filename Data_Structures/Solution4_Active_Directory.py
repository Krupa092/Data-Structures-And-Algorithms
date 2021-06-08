"""
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. 
We can construct this hierarchy as such. Where User is represented by str representing their ids.
"""
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users() or user == group.get_name: return True  
    else: 
        for group_data in group.get_groups(): 
            return is_user_in_group(user, group_data) # Recurse to go in to the groups of the groups
    return False

# *********************Test Case1************************** 
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
#Testing Statements 
print("***********************First Test Case***********************")  
print("is sub_child group has sub_child_user?", is_user_in_group("sub_child_user", sub_child))#True
print("is child group has sub_child_user?",is_user_in_group("sub_child_user", child))#True
print("is parent group has sub_child_user?",is_user_in_group("sub_child_user", parent))#True
print("is sub_child group has parent?",is_user_in_group("parent", sub_child)) # False 
print("is sub_child group has sub_child_user?", is_user_in_group("", sub_child))#When leaving empty (False)

# *********************Test Case2************************** 
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user1 = "sub_child_user1"
sub_child.add_user(sub_child_user1)
sub_child_user2 = "sub_child_user2"
sub_child.add_user(sub_child_user2)
sub_child_user3 = "sub_child_user3"
sub_child.add_user(sub_child_user3)
sub_child_user4 = "sub_child_user4"
sub_child.add_user(sub_child_user4)

child.add_group(sub_child)
parent.add_group(child)
#Testing Statements 
print("***********************Second Test Case***********************")  
print("is sub_child group has sub_child_user?", is_user_in_group("sub_child_user1", sub_child))#True
print("is child group has sub_child_user?",is_user_in_group("sub_child_user5", child))#False
print("is parent group has sub_child_user?",is_user_in_group("sub_child_user4", parent))#True
print("is sub_child group has parent?",is_user_in_group("parent", sub_child)) # False 
print("is sub_child group has sub_child_user?", is_user_in_group("4", sub_child))#When leaving empty (False)

# *********************Test Case3************************** 
parent = Group("parent")
child1 = Group("child1")
child2 = Group("child2")
sub_child1 = Group("subchild1")
sub_child2 = Group("subchild2")
sub_child3 = Group("subchild3")

sub_child_user1 = "sub_child_user1"
sub_child1.add_user(sub_child_user1)
sub_child_user2 = "sub_child_user2"
sub_child2.add_user(sub_child_user2)
sub_child_user3 = "sub_child_user3"
sub_child1.add_user(sub_child_user3)
sub_child_user4 = "sub_child_user4"
sub_child1.add_user(sub_child_user4)

child1.add_group(sub_child1)
child1.add_group(sub_child2)
child2.add_group(sub_child3)

parent.add_group(child1)
parent.add_group(child2)
#Testing Statements 
print("***********************Third Test Case***********************")  
print("is sub_child1 group has sub_child_user1?", is_user_in_group("sub_child_user4", sub_child1))#True
print("is sub_child2 group has sub_child_user3?", is_user_in_group("sub_child_user3", sub_child2))#False
print("is parent group has sub_child_user3?", is_user_in_group("sub_child_user3", parent))#True