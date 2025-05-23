# Last updated: 5/23/2025, 10:37:17 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        root_val = max(nums)
        root = TreeNode(root_val)
        seperate = nums.index(root_val)

        leftnums = nums[:seperate]
        rightnums = nums[seperate + 1:]

        root.left = self.constructMaximumBinaryTree(leftnums)
        root.right = self.constructMaximumBinaryTree(rightnums)

        return root