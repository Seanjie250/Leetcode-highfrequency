class MyHashMap:

    def __init__(self):
        self.capacity = 1000
        self.hash = [[] for _ in range(self.capacity)]
    def put(self, key: int, value: int) -> None:
        hash_key = key % self.capacity
        for pair in self.hash[hash_key]:
            if pair[0] == key:
                pair[1] = value
                return
        self.hash[hash_key].append([key , value])
    def get(self, key: int) -> int:
        hash_key = key % self.capacity
        for pair in self.hash[hash_key]:
            if pair[0] == key:
                return pair[1]
        return -1
    def remove(self, key: int) -> None:
        hash_key = key % self.capacity
        for index , pair in enumerate(self.hash[hash_key]):
            if pair[0] == key:
                self.hash[hash_key].pop(index)
        return 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)