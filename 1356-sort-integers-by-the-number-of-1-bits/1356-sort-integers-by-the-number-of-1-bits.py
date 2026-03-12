class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def bitsum(x):
            count = 0
            while x:
                count += (x & 1)
                x >>= 1
            return count
        arr.sort(key = lambda x : (bitsum(x) , x))
        return arr