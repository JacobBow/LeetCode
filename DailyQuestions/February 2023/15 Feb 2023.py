#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#

# @lc code=start
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        #Use map to iterate through num and make each value a string
        #Then use .join with '' as the delimeter then re-cast to an int to add k value
        new_int = int(''.join(map(str, num))) + k

        #Cast back into a str so we can use map() to iterate through the characters, make them ints, and put them in a list
        new_str = str(new_int)
        res = list(map(int, new_str))

        return res
        
        
# @lc code=end

