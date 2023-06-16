class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: 
            return int(tokens[0])
        stack = []
        for s in tokens:
            if s in ('+', '-', '*', '/'):
                if len(stack) > 1:
                    l1 = stack.pop() 
                    l2 = stack.pop()
                    stack.append(int(eval(str(l2) + str(s) + str(l1))))
            else:
                stack.append(s)

        return stack[0]