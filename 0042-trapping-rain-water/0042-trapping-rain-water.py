class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        rst = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                mid = stack.pop()
                if stack:
                    h = min(height[stack[-1]] , height[i])
                    rst += (h - height[mid]) * (i - stack[-1] - 1)
            stack.append(i)
        return rst
        