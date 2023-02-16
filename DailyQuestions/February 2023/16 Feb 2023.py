#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        #This program keeps track of how many times the tree is traversed on the left or right
        #Ex. Input: root = [3,9,20,null,null,15,7] Output: 3
        #With 3 as the root we only go left of the root once to 9 making the depth 2 on the left side
        #But on the right we go twice making the depth 3 (3->20->15/7)
        #Ex. When we are at 9 and try to go right we hit a None and return 0
        #   But when at 20 and we go left or right we increment out variable for the depth added bc value is not None
        #The tree traversal would be
        #   3->9->None->9->None->9->(End of left tree) 3->20->15->None->15->None->15->20->7->None->7->None
        leftTree = self.maxDepth(root.left)
        rightTree = self.maxDepth(root.right)
        
        #Add 1 for the initial root depth
        return max(leftTree, rightTree) + 1
        
# @lc code=end

