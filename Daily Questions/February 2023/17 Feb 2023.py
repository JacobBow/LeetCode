#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Root value stays the same
        #Right and left trees are swapped
        if not root:
            return None
        
        #Swap the first level of nodes, then call on the new left and right nodes
        #   and swap the subtree left and right nodes (Go level by level)
        #Can be done recurively similar to the form of traversing the tree
        #In Python the "," operator allows for one-lined swapping of values
        #root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        #Manually swap the values (Runs quicker then "," opertor but uses more memory)
        node = root.left
        root.left = root.right
        root.right = node

        #Ex. [4,2,7,1,3,6,9]
        #In Ex. provided: With root 4, after swapped 2 & 7 (with 7 now on the left)
        #   We will make 7 our new root and swap 6 & 9. Then we return to 4 being our
        #   Root and go to the next recursion and pass 2 as the new root and swap 1 & 3
        self.invertTree(root.left)
        self.invertTree(root.right)

        #Return the tree
        return root
        
        
# @lc code=end

