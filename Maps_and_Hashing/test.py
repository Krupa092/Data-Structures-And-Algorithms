
class Node: #LinkedList Node 
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.capacity= capacity
        self.head = Node(key=0,value=0)
        self.tail = Node(key=0,value=0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dict = dict() # empty dictionary to store keys and values 
        self.num_elements = 0

    def get(self, key): # get the value of key 
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.dict:
            return -1 #dict is empty, returning -1
        else:
            node = self.dict[key]
            self.remove_cache(node)
            self.add_cache(node)
            return node.value
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key not in self.dict:
            node = Node(key, value)
            self.dict[key] = node
            self.add_cache(node)
            self.num_elements += 1
        else:
            node = self.dict[key]
            node.value = value
            self.remove_cache(node)
            self.add_cache(node)
        if(self.num_elements > self.capacity):
            key_to_delete = self.tail.prev
            self.remove_cache(key_to_delete)
            self.dict.pop(key_to_delete.key)
            self.num_elements -= 1
        
    def add_cache(self,node):
        #Add recent cache
        temp = self.head.next #storing in temp variable
        self.head.next = node  
        node.prev = self.head
        node.next = temp
        temp.prev = node
        
    def remove_cache(self,node):
        #Delete cache
        #previoue_node = node.prev
        #next_node = node.next
        node.prev.next =node.next
        node.next.prev = node.prev
        """
        previoue_node.next =next_node
        next_node.prev = previoue_node
        """


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache


our_cache.set(5, 5) 
our_cache.set(6, 6)
print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

