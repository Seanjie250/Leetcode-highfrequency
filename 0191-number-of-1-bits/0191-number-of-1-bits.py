class Solution:
    def hammingWeight(self, n: int) -> int:
        rst = bin(n)
        count = 0
        rst = list(rst[2:])
        for i in range(len(rst)):
            if rst[i] == '1':
                count += 1
        return count
        