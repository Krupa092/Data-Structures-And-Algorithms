class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 
    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1 
            node = node.next
        return size

def union(llist_1, llist_2):
    # Your Solution Here
    Node_list = set() #declaring set to store unique elements 
    Node1_value = llist_1.head
    while Node1_value is not None:
        Node_list.add(Node1_value.value)
        Node1_value = Node1_value.next

    Node2_value = llist_2.head
    while Node2_value is not None:
        Node_list.add(Node2_value.value)
        Node2_value = Node2_value.next

    Union_list = LinkedList()
    for element in Node_list:
        Union_list.append(element)
    if Union_list.head is None:
        print("There is no Union element in the list")
    return (Union_list)

    
def intersection(llist_1, llist_2):
    # Your Solution Here
    Node1_list = set() #declaring set for list1
    Node2_list = set() #decalring set for list2 

    Node1_value = llist_1.head
    while Node1_value is not None:
        Node1_list.add(Node1_value.value)
        Node1_value = Node1_value.next

    Node2_value = llist_2.head
    while Node2_value is not None:
        Node2_list.add(Node2_value.value)
        Node2_value = Node2_value.next
    
    Intersection_List = LinkedList()
    for element in Node2_list:
        if element in Node1_list:
            Intersection_List.append(element)
    if Intersection_List.head is None:
        print("There is no intersection element in the list")
    return Intersection_List
 

# Test case 1

linked_list_1 = LinkedList()

linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
print("****************UNION LIST SET 1****************")
print (union(linked_list_1,linked_list_2))
print("****************INTERSECTION LIST SET 1****************")
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i) 

for i in element_2:
    linked_list_4.append(i)
print("****************UNION LIST SET 2****************")
print (union(linked_list_3,linked_list_4))
print("****************INTERSECTION LIST SET 2****************")
print (intersection(linked_list_3,linked_list_4))

# Test case 3

linked_list_1 = LinkedList()

linked_list_2 = LinkedList()

element_1 = []
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
print("****************UNION LIST SET 1****************")
print (union(linked_list_1,linked_list_2))
print("****************INTERSECTION LIST SET 1****************")
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i) 

for i in element_2:
    linked_list_4.append(i)
print("****************UNION LIST SET 2****************")
print (union(linked_list_3,linked_list_4))
print("****************INTERSECTION LIST SET 2****************")
print (intersection(linked_list_3,linked_list_4))

