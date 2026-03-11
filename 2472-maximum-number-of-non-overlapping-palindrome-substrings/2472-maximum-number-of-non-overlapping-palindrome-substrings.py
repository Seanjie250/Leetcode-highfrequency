class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:

        def findPalindromes(s, rst):

            for i in range(len(s)):
                left, right = i, i
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if right - left + 1 == k or right - left + 1 == k + 1:
                        rst.append([left, right])
                    left -= 1
                    right += 1

            for i in range(len(s)):
                left, right = i, i + 1
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if right - left + 1 == k or right - left + 1 == k + 1:
                        rst.append([left, right])
                    left -= 1
                    right += 1

            return rst

        rst = findPalindromes(s, [])

        if not rst:
            return 0

        rst.sort(key=lambda x: x[1])   # 按 end 排序

        ans = 0
        endpoint = -1

        for start, end in rst:
            if start > endpoint:
                ans += 1
                endpoint = end

        return ans
