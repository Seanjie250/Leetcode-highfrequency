class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rst = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                r = i - j
                rst[j] = r
            stack.append(i)
            
        return rst
            




        