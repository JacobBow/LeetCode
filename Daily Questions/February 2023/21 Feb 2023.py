#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
from collections import deque


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #Create our empty dictionary
        num_dict = {}

        #Add key & val to dictionary, if the value becomes 2 remove from dictionary
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
            if num_dict[num] == 2:
                num_dict.pop(num)
        
        #We are now left with the only single element in the list
        #Get the only key in the dictionary, cast to a list and access the first index then return result
        res = list(num_dict.keys())[0]
        return res

        '''for key, value in num_dict.items():
            if value == 1:
                return key'''
        
        
# @lc code=end

