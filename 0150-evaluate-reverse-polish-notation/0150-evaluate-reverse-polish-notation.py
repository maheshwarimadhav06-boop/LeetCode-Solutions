class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for num in tokens:
            if num == "+":
                a = stack.pop()
                b = stack.pop()
                add = a + b
                stack.append(add)
            elif num == "-":
                a = stack.pop()
                b = stack.pop()
                sub = b - a
                stack.append(sub)
            elif num == "*":
                a = stack.pop()
                b = stack.pop()
                mul = b * a
                stack.append(mul)  
            elif num == "/":
                a = stack.pop()
                b = stack.pop()
                div = int(float(b)/a)
                stack.append(div)
            else:
                stack.append(int(num))
        return stack[-1]

        