class Allocator:
    def __init__(self, n: int):
        self.id = [0] * n
        self.capacity = n
        
    def allocate(self, size: int, mID: int) -> int:
        count = 0
        for i in range(self.capacity):
            if self.id[i] != 0:
                count = 0
            else:
                count += 1
                if count == size:
                    self.id[i - count + 1 : i + 1] = [mID] * count
                    return i - count + 1
        return -1

        

    def freeMemory(self, mID: int) -> int:
        count = 0
        for i in range(self.capacity):
            if self.id[i] == mID:
                count += 1
                self.id[i] = 0
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)