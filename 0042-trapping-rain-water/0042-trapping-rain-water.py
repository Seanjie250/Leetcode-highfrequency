class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        rst = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                mid = stack.pop()
                if stack:
                    h = min(height[i] , height[stack[-1]]) - height[mid]
                    rst += h * (i - stack[-1] - 1)
            
            stack.append(i)
        return rst
            
        