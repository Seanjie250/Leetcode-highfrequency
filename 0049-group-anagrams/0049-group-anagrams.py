from collections import Counter
class Solution:
    def check_anagrams(self,s,t):
        if len(s) != len(t):
            return False
        key_s = ''.join(sorted(s))
        key_t = ''.join(sorted(t))
        return True if key_s == key_t else False
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1 or len(strs) == 0:
            return [strs]
        ans = []
        while strs:
            rst = [strs[0]]
            for i in range(1,len(strs)):
                if self.check_anagrams(strs[0],strs[i]):
                    rst.append(strs[i])
            ans.append(rst)
            strs = [s for s in strs if s not in rst]
        return ans

        