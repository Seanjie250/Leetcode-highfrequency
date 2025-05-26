# Last updated: 5/26/2025, 2:15:54 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        left_nums = nums[:mid]
        right_nums = nums[mid + 1 :]


        root.left = self.sortedArrayToBST(left_nums)
        root.right = self.sortedArrayToBST(right_nums)

        return root

        



        


                


            






        