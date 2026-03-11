class MyHashMap:

    def __init__(self):
        self.capacity = 1000000
        self.hash = [[-1] for _ in range(self.capacity)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.capacity
        self.hash[hash_key][0] = value

    def get(self, key: int) -> int:
        hash_key = key % self.capacity
        return self.hash[hash_key][0]

    def remove(self, key: int) -> None:
        hash_key = key % self.capacity
        self.hash[hash_key][0] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)