class ListNode:
    def __init__(self, key , val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode(0, 0)
        self.tail = ListNode(0 ,0)
        self.cache = {}
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self , node):
        nxt = node.next
        prv = node.prev
        nxt.prev = prv
        prv.next = nxt

    def add_to_head(self , node):
        nxt = self.head.next
        node.next = nxt
        node.prev = self.head
        self.head.next = node
        nxt.prev = node

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        node = self.cache[key]
        val = node.val
        self.remove(node)
        self.add_to_head(node)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add_to_head(node)
        else:
            while len(self.cache) >= self.capacity:
                tail = self.tail.prev
                key_tail = tail.key
                self.remove(tail)
                del self.cache[key_tail]
            node = ListNode(key , value)
            self.cache[key] = node
            self.add_to_head(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)