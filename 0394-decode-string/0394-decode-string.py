class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        stack = []
        current_string = ""
        current_num = 0
        for ch in s:
            if ch.isdigit():
                current_num = current_num*10 + int(ch)
            elif ch == "[":
                stack.append((current_string,current_num))
                current_string = ""
                current_num = 0
            elif ch == "]":
                previous_string, repeat_count = stack.pop()
                current_string = previous_string + current_string*repeat_count
            else:
                current_string += ch
        return current_string
