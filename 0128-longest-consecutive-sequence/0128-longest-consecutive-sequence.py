class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = set(nums)
        print(l)
        ans = 0
        while len(l) != 0:
            cur = l.pop()
            print(cur)
            length = 1
            l_l = cur - 1
            r_l = cur + 1
            while l_l in l or r_l in l:
                if l_l in l:
                    length += 1
                    l.remove(l_l)
                    l_l -= 1
                if r_l in l:
                    length += 1
                    l.remove(r_l)
                    r_l += 1
            ans = max(ans , length)
        return ans

        