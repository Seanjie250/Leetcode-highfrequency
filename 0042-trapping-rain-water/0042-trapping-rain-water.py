class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        area = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                    mid = stack.pop()
                    if not stack:
                        break
                    h = min(height[stack[-1]] , height[i])
                    area += (h - height[mid]) * (i - stack[-1] - 1)
            stack.append(i)
        return area
        

            
        