class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = strs[0]
        while len(string) > 0:
            for str_ in strs[1:]:
                if not str_.startswith(string):
                    string = string[:-1]
                    break
            else:
                return string
        return ""
             
        