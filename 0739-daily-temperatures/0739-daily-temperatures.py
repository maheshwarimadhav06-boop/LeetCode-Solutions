class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # n = len(temperatures)
        # answer = []
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if (temperatures[j]>temperatures[i]):
        #             answer.append(j-i)
        #             break
        #     else:
        #         answer.append(0)
        # return answer

        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                answer[prev] = i - prev
            stack.append(i)
        return answer
