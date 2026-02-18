class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = set(nums)
        ans = 0
        while len(l) != 0:
            cur = l.pop()
            length = 1
            left_cur = cur - 1
            right_cur = cur + 1
            while left_cur in l or right_cur in l:
                if left_cur in l:
                    length += 1
                    l.remove(left_cur)
                    left_cur -= 1
                if right_cur in l:
                    length += 1
                    l.remove(right_cur)
                    right_cur += 1
            ans = max(ans , length)

                
        return ans
        