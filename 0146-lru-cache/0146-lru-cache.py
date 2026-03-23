class ListNode:
    def __init__(self , key , val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode(-1 , -1)
        self.tail = ListNode(-1 , -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
        self.capacity = capacity
    def remove(self , node):
        nxt = node.next
        prv = node.prev
        prv.next = nxt
        nxt.prev = prv
    def add_to_head(self, node):
        nxt = self.head.next
        node.next = nxt
        node.prev = self.head
        self.head.next = node
        node.prev = self.head
        nxt.prev = node
    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        node = self.cache[key]
        value = node.val
        self.remove(node)
        self.add_to_head(node)
        return value
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add_to_head(node)
        else:
            node = ListNode(key , value)
            self.add_to_head(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                tail_node = self.tail.prev
                tail_key = tail_node.key
                self.remove(tail_node)
                del self.cache[tail_key]

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)