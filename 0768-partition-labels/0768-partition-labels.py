class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_appear = {}
        for i,char in enumerate(s):
            last_appear[char] = i
        
        rst = []
        end = 0
        start = 0
        for i,char in enumerate(s):
            end = max(end,last_appear[char])
            if i == end:
                rst.append(end - start + 1)
                start = i + 1
        return rst

            
            


