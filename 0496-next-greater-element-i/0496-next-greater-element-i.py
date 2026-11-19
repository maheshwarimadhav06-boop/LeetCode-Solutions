class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = len(nums1)
        m = len(nums2)
        stack = []
        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j]:
                    found = False
                    if j == m-1:
                        stack.append(-1)
                    else:
                        for k in range(j+1,m):
                            if nums2[k] > nums2[j]:
                                stack.append(nums2[k])
                                found = True
                                break
                        if not found:
                            stack.append(-1)
                    break
        return stack
        
        