class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        maxm = 0
        for num , counts in counter.items():
            if counts > maxm:
                maxm = counts
                ans = num
        return ans 

        