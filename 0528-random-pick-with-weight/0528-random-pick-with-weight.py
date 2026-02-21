class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        sum_ = sum(w)
        for i in range(len(w)):
            self.w[i] = self.w[i] / sum_

        for i in range(1, len(w)):
            self.w[i] += self.w[i - 1]
        
        print(self.w[-1])
        
        

    def pickIndex(self) -> int:
        val = random.uniform(0 , 1)
        flag = 1
        index = -1
        while flag:
            index += 1
            if val <= self.w[index]:
                flag = 0
        return index
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()