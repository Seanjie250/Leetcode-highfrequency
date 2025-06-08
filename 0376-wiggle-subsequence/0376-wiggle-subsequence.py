class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 2 and nums[0] != nums[1]:
            return 2
        if len(nums) == 1:
            return 1
        rst = 1
        curdiff,prediff = 0,0
        for i in range(0,len(nums) - 1):
            curdiff = nums[i + 1] - nums[i]
            if (prediff <= 0 and curdiff > 0) or (prediff >= 0 and curdiff < 0):
                rst += 1
                prediff = curdiff
        return rst
            
        

        