class ListNode:
    def __init__(self , key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode(0 , 0)
        self.tail = ListNode(0 , 0)
        self.capacity = capacity
        self.cache = {}
        self.head.next = self.tail
        self.tail.prev = self.head
    def add_to_head(self , node):
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node
    def remove(self , node):
        prev = node.prev
        nxt = node.next
        prev.next= nxt
        nxt.prev = prev
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
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
            if len(self.cache) == self.capacity:
                delete = self.tail.prev 
                key_ = delete.key
                self.remove(delete)
                del self.cache[key_]
            node = ListNode(key ,value)
            self.add_to_head(node)
            self.cache[key] = (node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)