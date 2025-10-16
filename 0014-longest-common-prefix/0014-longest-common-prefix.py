class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for str in strs[1:]:
            while not str.startswith(prefix):
                prefix = prefix[:-1]
            if not prefix:
                return ""
        return prefix
        



        