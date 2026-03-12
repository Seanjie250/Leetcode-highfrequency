class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        minm , maxm = 0 , 2**n 
        for i in range(minm , maxm):
            sting = format(i , f'0{n}b')
            if sting not in nums:
                return sting
        