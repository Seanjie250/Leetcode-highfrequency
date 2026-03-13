class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = [-1] * len(nums2)
        stack = [0]
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                next_greater[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(i)

        print(next_greater)
        rst = []
        for num in nums1:
            index = nums2.index(num)
            rst.append(next_greater[index])
        return rst


                    


        
        