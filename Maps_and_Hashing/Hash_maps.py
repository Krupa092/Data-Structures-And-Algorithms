# Hash Map: 
"""
The Problem Scenario
In a class of students, store heights for each student.

The problem in itself is very simple. 
We have the data of heights of each student. 
We want to store it so that next time someone asks for height of a student, 
we can easily return the value. But how can we store these heights?
"""
class HashMap:
    def __init__(self, initial_size = 10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 37     # a prime numbers
        self.num_entries = 0 
    def put (self,key,value):
        pass
    def get (self,key):
        pass
    def size(self):
        return self.num_entries
    #Returns the Bucket_index
    def get_bucket_index(self, key):
        return self.get_hash_code(key)  # The returned hash code will be the bucket_index
    # Returns the hash code
    def get_hash_code(self,key):
        key = str(key)
        num_buckets = len(self.bucket_array) 
        # represents (self.p^0) which is 1
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets 
        return hash_code
        
hash_map = HashMap()

hash_map = HashMap()

bucket_index = hash_map.get_bucket_index("one")
print(bucket_index)

bucket_index = hash_map.get_bucket_index("neo")
print(bucket_index)                                  # Collision might occur

"""
bucket_index = hash_map.get_bucket_index("Krupa")
print(bucket_index)

bucket_index = hash_map.get_bucket_index("Pakru")
print(bucket_index)

def Hash_function(String):
    hash_code = 0
    for character in String:
        hash_code += ord(character)
    return hash_code

hash_code_1 = Hash_function("Krupa")
print(hash_code_1)
"""