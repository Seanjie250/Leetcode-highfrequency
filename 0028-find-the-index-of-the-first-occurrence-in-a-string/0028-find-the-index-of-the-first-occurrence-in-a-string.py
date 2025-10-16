class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        rst = 0
        for i in range(len(haystack)):
            if haystack.startswith(needle):
                return rst
            else:
                haystack = haystack[1:]
                rst += 1
        return -1
        