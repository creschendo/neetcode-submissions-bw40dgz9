class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.chain = [ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        bucket = self.chain[key % len(self.chain)]
        while bucket.next:
            if bucket.next.key == key:
                return
            bucket = bucket.next
        bucket.next = ListNode(key)
        
    def remove(self, key: int) -> None:
        bucket = self.chain[key % len(self.chain)]
        while bucket.next:
            if bucket.next.key == key:
                bucket.next = bucket.next.next
                return 
            bucket = bucket.next
        

    def contains(self, key: int) -> bool:
        bucket = self.chain[key % len(self.chain)]
        while bucket.next:
            if bucket.next.key == key:
                return True
            bucket = bucket.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)