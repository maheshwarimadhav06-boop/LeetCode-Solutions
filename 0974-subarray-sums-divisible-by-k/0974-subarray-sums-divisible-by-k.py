class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # n = len(nums)
        # count = 0
        # for i in range(n):
        #     subarray_sum = 0
        #     for j in range(i,n):
        #         subarray_sum += nums[j]
        #         if subarray_sum % k == 0:
        #             count += 1
        # return count

        prefix_freq = {0:1}
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            count += prefix_freq.get(remainder,0)
            prefix_freq[remainder] = prefix_freq.get(remainder,0) + 1
        return count