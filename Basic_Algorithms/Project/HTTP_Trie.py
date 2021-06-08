# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self): # initial 
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = '/' #Router URL path '/'
        self.next = {} 
        self.driver = None 

    def insert(self,paths,router): #insert method
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        _current = self.next
        _paths = paths.split('/')
        for path in _paths:
            _current.insert(RouteTrieNode(path))
            _current = _current.next[path]
        _current.handler = driver

    def find(self,paths,driver): #find method 
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if paths == '/':
            return self.driver
        _paths = paths.split('/') # for spliting the path from "/"

        for path in _paths:
            _current = self
            for sub_path in path:
                _current = _current.next
                _current = _current[sub_path]
            driver = _current.driver
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, value=""):
        # Initialize the node with children as before, plus a handler
        self.value = value
        self.next = {}
        self.driver = None
    def insert(self,next_path,driver = None):
        # Insert the node as before
        self.next[next_path] = self.next.get(next_path, RouteTrieNode(next_path))
        self.next[next_path].driver = driver
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self,root_driver,not_found_driver):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = '/'
        self.driver = root_driver
        self.next = {}
        self.not_found = not_found_driver

    def add_handler(self, path, path_driver):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if path == self.root:
            self.driver = path_driver
        else:
            _paths = self.split_path(path)
            _current = self.next
            var = 1
            for sub_path in _paths:
                if not sub_path:
                    continue
                if var:
                    var = 0
                    _current[sub_path] = _current.get(sub_path, RouteTrieNode(sub_path))
                    _current = _current[sub_path]
                else:
                    _current.insert(sub_path, path_driver)
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == '/':
            return self.driver
        _paths = self.split_path(path)
        _current = self

        for sub_path in _paths:
            if sub_path:
                if sub_path in _current.next:
                    _current = _current.next
                    _current = _current[sub_path]
                else:
                    return self.not_found

        driver = _current.driver
        if driver:
            return driver
        else:
            return None

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.split('/')

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one