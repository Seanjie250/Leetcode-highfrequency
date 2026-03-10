class MyHashMap:

    def __init__(self):
        self.capacity = 1000
        self.hashmap = [[] for _ in range(self.capacity)]
        
    def gethashkey(self , key):
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        key_ = self.gethashkey(key)
        for pair in self.hashmap[key_]:
            if pair[0] == key:
                pair[1] = value
                return
        self.hashmap[key_].append([key , value])

    def get(self, key: int) -> int:
        key_ = self.gethashkey(key)
        for pair in self.hashmap[key_]:
            if pair[0] == key:
                return pair[1]
        return -1
        
    def remove(self, key: int) -> None:
        key_ = self.gethashkey(key)
        for idx , pair in enumerate(self.hashmap[key_]):
            if pair[0] == key:
                self.hashmap[key_].pop(idx)
                break
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)