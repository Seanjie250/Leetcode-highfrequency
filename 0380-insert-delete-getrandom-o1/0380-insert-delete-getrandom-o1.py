class RandomizedSet:

    def __init__(self):
        self.data = []
        self.pos = {}
    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        self.pos[val] = len(self.data)
        self.data.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        
        idx = self.pos[val]
        last = self.data[-1]
        self.data[idx] = last
        self.pos[last] = idx
        self.data.pop()
        return True

        

    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()