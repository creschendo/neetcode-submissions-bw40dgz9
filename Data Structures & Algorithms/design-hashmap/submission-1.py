class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.chain = [ListNode(0, 0) for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        bucket = self.chain[key % len(self.chain)]

        while bucket.next:
            if bucket.next.key == key:
                bucket.next.val = value
                return
            bucket = bucket.next
        
        bucket.next = ListNode(key, value)

    def get(self, key: int) -> int:
        bucket = self.chain[key % len(self.chain)]

        while bucket.next:
            if bucket.next.key == key:
                return bucket.next.val
            bucket = bucket.next
        
        return -1

    def remove(self, key: int) -> None:
        bucket = self.chain[key % len(self.chain)]

        while bucket.next:
            if bucket.next.key == key:
                bucket.next = bucket.next.next
                return
            bucket = bucket.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)