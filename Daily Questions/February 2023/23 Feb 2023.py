#
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#

# @lc code=start
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #Numbers of Projects
        n = len(profits)
        #Create pairs and sort ascendingly so we can easily progress
        projects = list(zip(capital, profits))
        projects.sort()
        #We want to store jobs in a priority queue
        queue = []
        #Pointer going to next unavaliable job
        pointer = 0
        #For the time we can still complete projects
        for i in range(k):
            #Make sure pointer isn't out of bounds, our capital is <= than our avaliable projects capital
            while pointer < n and projects[pointer][0] <= w:
                #Push to the heap the negated profits (Will put the highest value first)
                heappush(queue, -projects[pointer][1])
                pointer += 1
            if not queue:
                break
            #Remove first negated element (Highest value) and add to our capital
            w += -heappop(queue)

        return w
        
# @lc code=end

