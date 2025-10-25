class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        map_ps , map_sp = {} , {}
        if len(s) != len(pattern):
            return False
        for c1,c2 in zip(pattern,s):
            if c1 in map_ps and map_ps[c1] != c2:
                return False
            if c2 in map_sp and map_sp[c2] != c1:
                return False
            map_ps[c1] = c2
            map_sp[c2] = c1
        return True

        