class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        n = len(nums1)
        m = len(nums2)
        result = []
        for i in range(n):
            for j in range(m):
                if (nums1[i] == nums2[j]):
                    for k in range(j+1,m):
                        if (nums2[j] < nums2[k]):
                            result.append(nums2[k])
                            break
                    else:
                        result.append(-1)
        return result