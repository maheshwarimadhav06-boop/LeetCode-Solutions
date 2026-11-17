class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack_s = []
        for ch in s:
            if ch == "#":
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(ch)
        stack_t = []
        for ch in t:
            if ch == "#":
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(ch)
        return stack_s == stack_t
            