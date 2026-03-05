class ListNode:
    def __init__(self , key , val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode(0 , 0)
        self.tail = ListNode(0 , 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
        self.capacity = capacity
    def remove_node(self , node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    def add_to_head(self,node):
        next_node = self.head.next
        node.next = next_node
        next_node.prev = node
        self.head.next = node
        node.prev = self.head
    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        node = self.cache[key]
        val = node.val
        self.remove_node(node)
        self.add_to_head(node)
        return val
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove_node(node)
            self.add_to_head(node)
        else:
            node = ListNode(key , value)
            if len(self.cache) >= self.capacity:
                tail_node = self.tail.prev
                self.remove_node(tail_node)
                del self.cache[tail_node.key]
            self.cache[key] = node
            self.add_to_head(node)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)