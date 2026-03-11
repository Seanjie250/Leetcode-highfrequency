class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left , right = 0 , len(people) - 1
        ans = 0
        people = sorted(people)
        while left < right:
            if people[left] + people[right] <= limit:
                left += 1
            ans += 1
            right -= 1
        if left == right:
            ans += 1
        return ans
                
                
        