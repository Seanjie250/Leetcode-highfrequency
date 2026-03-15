class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                mid = stack.pop()
                if stack:
                    h = (min(height[i] , height[stack[-1]]) - height[mid])
                    ans += (i - stack[-1] - 1) * h
            stack.append(i)
        return ans
        