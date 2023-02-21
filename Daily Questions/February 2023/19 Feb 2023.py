#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Base case, no root
        if not root:
            return []

        #We could store the values in a queue as we traverse, pop them and then append them
        queue = Deque([root])
        result = []
        left_to_right = True

        while queue:
            #Holds values for each level we go to
            level_value = []
            for i in range(len(queue)):
                #We want to get the first item in our queue
                node = queue.popleft()

                #Determines zigzaging, if we are left -> right we normal append, else we insert to the front of the queue
                #This ensures proper placement, we always get the left value first but if we are going right -> left
                #   then the .insert(0, node.val) will put the right value at the front of the list
                if left_to_right:
                    level_value.append(node.val)
                else:
                    level_value.insert(0, node.val)

                #If there is a value to the left or right of the node lets get that value in the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            #After we finish going through that level lets append the results to our list
            result.append(level_value)
            #This will alternate True/False value so we know when to zigzag
            left_to_right = not left_to_right

        return result
        
# @lc code=end

