class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "[": "]", "{": "}"}
        opening = set(['(', '[', '{'])
        stack = []
        for p in s:
            if p in opening:
                stack.append(p)
            elif stack and p == pairs[stack[-1]]:
                stack.pop()
            else : 
                return False
        return stack == []
