class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxm = float('-inf')
        left , right = 0 , len(height) - 1
        while left < right:
            width = right - left
            maxm = max(maxm , width * min(height[left] , height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxm

        