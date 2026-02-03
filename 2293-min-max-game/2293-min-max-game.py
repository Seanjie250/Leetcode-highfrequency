class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        newnums = []
        isMax = False
        while len(nums) != 1:
            for i in range(0, len(nums) - 1 , 2):
                if not isMax:
                    newnums.append(min(nums[i] , nums[i + 1]))
                    isMax = True
                else:
                    newnums.append(max(nums[i] , nums[i + 1]))
                    isMax = False
            nums = newnums
            newnums = []
        return nums[0]
        