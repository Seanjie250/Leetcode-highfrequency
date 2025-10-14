class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = dict()
        n = len(nums)
        k = 0
        for num in nums:
            count[num] = count.get(num,0) + 1
            if count[num] <= 2:
                nums[k] = num
                k += 1
        return k            

            

        
            
        