class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        rst = 0
        n = len(height)
        for i in range(n):
            cur = height[i]
            while stack and height[stack[-1]] < cur:
                temp = stack.pop()
                if stack:
                    h = min(height[stack[-1]] , cur)
                    rst += (h - height[temp]) * (i - stack[-1] - 1)
            stack.append(i)
        return rst

                

        