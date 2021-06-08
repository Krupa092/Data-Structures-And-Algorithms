## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_char = False
        self.children = {}
        self.result = set()
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        if self.children:
            for char, node in self.children.items():
                if node.is_char:
                    result.append(suffix + char)
                node.suffixes(suffix + char)
        return list(result)
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
                
            current_node = current_node.children[char]

        current_node.is_char = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node
"""
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_char = False
        self.children = {}
        self.result = set()
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.root = TrieNode()
"""  
    

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='')
