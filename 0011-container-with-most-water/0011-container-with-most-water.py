class Solution:
    def calculate_area(self, height, i, j):
        return (j - i) * min(height[i], height[j])

    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0

        while i < j:
            # calculate current area
            area = self.calculate_area(height, i, j)
            max_area = max(max_area, area)

            # move the smaller line inward
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area
