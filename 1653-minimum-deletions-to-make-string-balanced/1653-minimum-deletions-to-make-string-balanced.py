class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = 0
        rst = 0
        for ch in s:
            if ch == 'b':
                count += 1
            elif count:
                count -= 1
                rst += 1
        return rst

#greedy 
        