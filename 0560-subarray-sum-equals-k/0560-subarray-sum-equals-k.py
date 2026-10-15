class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_freq = {0:1}
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num
            needed = prefix_sum - k

            count += prefix_freq.get(needed, 0)
            prefix_freq[prefix_sum] = prefix_freq.get(prefix_sum, 0) + 1
        return count