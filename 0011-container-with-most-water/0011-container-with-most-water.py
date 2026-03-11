class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0 , len(height) - 1
        maxm = min(height[left] , height[right]) * (right - left)
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            area = min(height[left] , height[right]) * (right - left)
            maxm = max(maxm , area)
        return maxm
        