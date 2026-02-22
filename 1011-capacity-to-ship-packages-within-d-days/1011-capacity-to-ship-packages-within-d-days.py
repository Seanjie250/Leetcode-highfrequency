class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights) 
        right = sum(weights)
        def if_ok(workload , days):
            prefix_sum = 0
            time = 1
            for weight in weights:
                if prefix_sum + weight <= workload:
                    prefix_sum += weight
                else:
                    time += 1
                    prefix_sum = weight
                    if time > days:
                        return False
            return True
    
        while left <= right:
            mid = (left + right) // 2
            if if_ok(mid, days):
                right = mid - 1
            else:
                left = mid + 1
        return left

                
        