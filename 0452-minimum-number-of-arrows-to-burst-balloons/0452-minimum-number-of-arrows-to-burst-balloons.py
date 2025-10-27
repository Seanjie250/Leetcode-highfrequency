class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key = lambda x:x[0])
        count = 1
        end = points[0][1]
        for start , finish in points[1:]:
            if start <= end:
                end = min(end, finish)
            if start > end:
                count += 1
                end = finish
        return count 