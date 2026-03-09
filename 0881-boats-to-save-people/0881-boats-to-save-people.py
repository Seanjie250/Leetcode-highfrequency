class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort(reverse = True)
        left = 0
        right = len(people) - 1
        while left < right:
            if people[left] + people[right] <= limit:
                right -= 1
                print(right)
                
            ans += 1
            left += 1
        if left == right:
            ans += 1
        return ans

            

        