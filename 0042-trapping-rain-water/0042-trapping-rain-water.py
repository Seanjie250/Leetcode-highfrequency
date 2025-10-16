class Solution:
    def trap(self, height: List[int]) -> int:
        rst = 0
        stack = [0]
        for i in range(1,len(height)):
            if height[i] == height[stack[-1]]:
                stack.pop()
                stack.append(i)
            elif height[i] < height[stack[-1]]:
                stack.append(i)
            else:
                while stack and height[i] > height[stack[-1]]:
                    mid = stack.pop()
                    if stack:

                        h = min(height[i],height[stack[-1]]) - height[mid]
                        w = i - stack[-1] - 1
                        rst += h*w
                stack.append(i)
        return rst

        