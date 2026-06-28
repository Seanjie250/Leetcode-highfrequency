class ListNode:
    def __init__(self , key , val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode(-1 , -1)
        self.tail = ListNode(-1 , -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = {}
        self.capacity_all = capacity
    def remove(self , node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    def add_to_head(self ,node):
        nxt_node = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next = nxt_node
        nxt_node.prev = node
    def get(self, key: int) -> int:
        if not key in self.capacity:
            return -1
        node = self.capacity[key]
        val = node.val
        self.remove(node)
        self.add_to_head(node)
        return val
    def put(self, key: int, value: int) -> None:
        if key in self.capacity:
            node = self.capacity[key]
            node.val = value
            self.remove(node)
            self.add_to_head(node)
        else:
            node = ListNode(key , value)
            self.add_to_head(node)
            self.capacity[key] = node
            if len(self.capacity) > self.capacity_all:
                tail_node = self.tail.prev
                tail_node_key = tail_node.key
                self.remove(tail_node)
                del self.capacity[tail_node_key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)