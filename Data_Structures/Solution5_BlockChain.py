import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
        
def str_datetime():
    return datetime.utcnow() # return timestemp  

class Block_Chain:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def append(self, timestamp, data):
        if self.head is None:
            self.head = Block(timestamp, data, 0)
            self.tail = self.head #Move the element 
        else:
            tail_data = self.tail
            self.tail = Block(timestamp, data, 0)
            self.previous_hash = tail_data

#*****************************Test Case***************************
# Building Blocks
Zero = Block(str_datetime(),"0th Block", 0)
One = Block(str_datetime(),"1st Block", Zero)
Two = Block(str_datetime(),"2nd Block", One)
Three = Block(str_datetime(),"3rd Block", Two)

print("*********************************")
print("0th Block data: ",Zero.data)
print("0th Block hash: ",Zero.hash)
print("0th Block time: ",Zero.timestamp)

print("*********************************")
print("1st Block data: ",One.data)
print("1st Block hash: ",One.hash)
print("1st Block time: ",One.timestamp)

print("*********************************")
print("2nd Block data: ",Two.data)
print("2nd Block hash: ",Two.hash)
print("2nd Block time: ",Two.timestamp)

print("*********************************")
print("3rd Block data: ",Three.data)
print("3rd Block hash: ",Three.hash)
print("3rd Block time: ",Three.timestamp)

# Appending Blocks using Block Chain
Block_Chain = Block_Chain()
Block_Chain.append(str_datetime(),"Next Block")

print("*********************************")
print("Tail Data: ",Block_Chain.tail.data)
print("Tail Data hash: ",Block_Chain.tail.hash)
print("Tail Data time: ",Block_Chain.tail.timestamp)

#*****************************Test Case***************************
# Building Empty Block
Zero = Block(str_datetime(),"", 0)
One = Block(str_datetime(),"1st Block", Zero)

print("*********************************")
print("0th Block data: ",Zero.data)
print("0th Block hash: ",Zero.hash)
print("0th Block time: ",Zero.timestamp)
