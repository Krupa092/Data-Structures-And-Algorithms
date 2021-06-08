"""
The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.
While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. 
If, however, the entry is not found, it is known as a cache miss.
When designing a cache, we also place an upper bound on the size of the cache. 
If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. 
After removing an element, we use the put() operation to insert the new element. 
The remove operation should also be fast.
For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. 
An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. 
For the current problem, consider both get and set operations as an use operation.
Your job is to use an appropriate data structure(s) to implement the cache.
In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. 
If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.
For the current problem, you can consider the size of cache = 5.
"""
class Node:
    def __init__(self,key,value): # initiating Node
        self.value = value 
        self.prev = None 
        self.next = None 
        self.key = key

class LinkedList:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self,node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node
    
    def remove(self,node):
        previous_node = node.prev
        next_node = node.next()
        previous_node.next = next_node
        next_node.prev = previous_node

class LRU_Cache:
    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.dict = dict()
        self.cache = None
        self.num_elements = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.key is None:
            return -1
        else:
            node = self.dict[key]
            LinkedList.remove(node)

        
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key not in self.dict:
            node = Node(key, value)
            self.dict[key] = node
            LinkedList.add(node)
            self.num_elements += 1
        else:
            node = self.dict[key]
            node.value = value
            self.L.remove(node)
            self.L.add(node)

        if(self.num_elements > self.capacity):
            to_remove = self.L.tail.prev
            self.L.remove(to_remove)
            self.L.dict[to_remove.key]
            self.num_elements -= 1
node = Node(1,2)
LinkedList()


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
