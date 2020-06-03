# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children plus a handler
        self.children = {}
        self.handler = None
        
    def insert(self, handler):
        # Insert the node
        if handler not in self.children:
            self.children[handler] = RouteTrieNode()
        else:
            pass
        
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for i in path:
            current_node.insert(i)
            current_node = current_node.children[i]
            
        current_node.handler = handler
        

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        
        for i in path:
            if i not in current_node.children:
                return None
            current_node = current_node.children[i]
        return current_node.handler

# The Router class will wrap the Trie and handler 
class Router:
    def __init__(self, handler, not_found_handler="not found handler"):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routes = RouteTrie()
        self.routes.insert("/", handler)
        self.not_found = not_found_handler
        
    def add_handler(self, route, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        paths = self.split_path(route)
        self.routes.insert(paths, handler)

    def lookup(self, route):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        paths = self.split_path(route)
        return self.routes.find(paths) or self.not_found


    def split_path(self, route):
        # you need to split the path into parts for 
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        if len(route) == 1:
            return ["/"]
        else:
            return route.strip("/").split("/")

### TESTS ###

# create the router and add a route
# router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router = Router("root handler") 
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print("'/' uses the", router.lookup("/")) # should print 'root handler'
print("'/home' uses the", router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print("'/home/about' uses the", router.lookup("/home/about")) # should print 'about handler'
print("'/home/about' uses the", router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print("'/home/about/me' uses the", router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one