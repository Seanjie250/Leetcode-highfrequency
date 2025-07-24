class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums + nums
        rst = [-1] * len(nums)
        stack = [0]
        for i in  range(1,len(nums)):
            if nums[i] <= nums[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums[i] > nums[stack[-1]]:
                    rst[stack[-1]] = nums[i]
                    stack.pop()
            stack.append(i)
        return rst[:n]