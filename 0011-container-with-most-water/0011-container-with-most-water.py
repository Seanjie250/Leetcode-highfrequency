class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxm = float('-inf')
        left , right = 0 , len(height) - 1
        while left < right:
            maxm = max(maxm , (min(height[left] , height[right]) * (right - left)))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxm
        