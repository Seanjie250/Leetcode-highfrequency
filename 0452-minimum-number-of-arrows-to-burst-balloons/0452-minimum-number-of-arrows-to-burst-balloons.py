class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort balloons by their end coordinate
        points.sort(key=lambda x: x[1])

        arrows = 1
        end = points[0][1]

        for start, finish in points[1:]:
            # If the next balloon starts after the last arrow's end → need new arrow
            if start > end:
                arrows += 1
                end = finish  # place new arrow at this balloon's end
            # Else, they overlap → same arrow bursts both

        return arrows
