class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def calculate_slope(p1 , p2):
            v1 , h1 = p1
            v2 , h2 = p2

            delta = v2 - v1

            if delta == 0:
                return inf
            
            else:
                slope = (h2 - h1) / (v2 - v1)
            return slope
        if len(points) == 1:
            return 1
        
        ans = 1

        for i , pi in enumerate(points):
            slopes = defaultdict(int)
            for j in points[i + 1: ]:
                slope = calculate_slope(pi , j)
                slopes[slope] += 1
                ans = max(slopes[slope] , ans)
        
        return ans + 1

    


