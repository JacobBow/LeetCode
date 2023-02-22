#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #Has form for binary search because we have a lower and upper bound, with our mid being the capacity
        #https://www.youtube.com/watch?v=ER_oLmdc-nw
        #Low is the minimum weight capacity and high is the highest capacity
        low = max(weights)
        high = sum(weights)
        #Base case if days given 1
        result = high

        def check(capacity):
            day = 1
            curr_capacity = capacity

            for weight in weights:
                if curr_capacity - weight < 0:
                    curr_capacity = capacity
                    day += 1
                curr_capacity -= weight
            return day <= days

        
        while low <= high:
            #Find the mid value, // is floor division which rounds down to whole number
            mid = (low + high) // 2

            if check(mid):
                result = min(result, mid)
                high = mid - 1
            else:
                low = mid + 1


        return result
# @lc code=end

