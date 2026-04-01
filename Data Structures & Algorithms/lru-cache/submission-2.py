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
        next = self.left.next
        self.left.next = node
        node.next = next
        node.prev = self.left
        next.prev = node

    # Removes a node in general
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    # Removes and re inserst a node, moving it to front
    # and returning value if it exists
    # Instantly returns -1 if key doesn't exist
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache.get(key)
            self.remove(node)
            self.insert(node)
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
        if key in self.cache:
            self.remove(self.cache.get(key))
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            toRemove = self.right.prev
            self.remove(toRemove)
            del self.cache[toRemove.key]

        
