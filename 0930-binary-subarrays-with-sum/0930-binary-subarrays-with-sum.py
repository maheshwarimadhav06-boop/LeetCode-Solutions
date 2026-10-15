class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        freq_goal = {0:1}
        prefix = 0
        count = 0
        for num in nums:
            prefix += num
            needed = prefix - goal
            count += freq_goal.get(needed,0)
            freq_goal[prefix] = freq_goal.get(prefix,0) + 1
        return count
        