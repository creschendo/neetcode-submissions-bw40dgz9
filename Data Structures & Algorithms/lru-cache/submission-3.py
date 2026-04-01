class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    # cap: capacity
    # cache: map of keys to nodes
    # left: entry point, most recent node
    # right: exit point, least recent node
    #   - left and right are buffered by 1 dummy node on each 
    #     side for easy removal and insertion
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    # Inserts a node on the left
    def insert(self, node):
        # Store the current first node
        next = self.left.next

        # Set left to new node
        self.left.next = node

        # Set new node next and prev
        node.next = next
        node.prev = self.left

        # Set previous first node's prev to new node
        next.prev = node

    # Removes a node in general
    def remove(self, node):
        # Store previous and next of node to remove
        prev, next = node.prev, node.next

        # Splice prev and next together
        prev.next = next
        next.prev = prev

    # Removes and re inserst a node, moving it to front
    # and returning value if it exists
    # Instantly returns -1 if key doesn't exist
    def get(self, key: int) -> int:
        # Key in cache
        if key in self.cache:
            # Retrieve node 
            node = self.cache.get(key)

            # Remove and insert, which moves it to the front
            self.remove(node)
            self.insert(node)

            # Return value
            return node.val
        return -1

    # Adds a new key value pair or updates an existing one
    # New case:
    #   - Create new hashmap mapping
    #   - insert new node into list
    #   - If capacity is exceeded, remove a node from the
    #     right, along with its mapping
    # Existing case:
    #   - First removes the node and remakes a new one, 
    #     effectively updating the key and moving to front
    def put(self, key: int, value: int) -> None:
        # Key already exists, so remove it from list
        if key in self.cache:
            self.remove(self.cache.get(key))

        # Update hashmap with new node mapping
        self.cache[key] = Node(key, value)

        # Add new node to front of list
        self.insert(self.cache[key])

        # If capacity reached, remove LRU from list and hashmap
        if len(self.cache) > self.cap:
            toRemove = self.right.prev
            self.remove(toRemove)
            del self.cache[toRemove.key]

        
