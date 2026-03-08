class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_time = [0] * len(nums)
        right_time = [0] * len(nums)
        rst = [0] * len(nums)
        left_time[0] = nums[0]
        right_time[- 1] = nums[-1]
        for i in range(1, len(nums)):
            left_time[i] = nums[i] * left_time[i - 1]
        for i in range(len(nums) - 2 , - 1, - 1):
            right_time[i] = nums[i] * right_time[i + 1]
        
        print(left_time)
        print(right_time)
        rst[0] = right_time[1]
        rst[-1] = left_time[-2]

        for i in range(1 , len(nums) - 1):
            rst[i] = left_time[i - 1] * right_time[i + 1]
        return rst


        


            

        
        