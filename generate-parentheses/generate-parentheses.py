class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        stack = []

        def backtract(openC, closeC):

            if openC == closeC == n:
                res.append("".join(stack))
                return
            
            if openC < n:
                stack.append('(')
                backtract(openC+1, closeC)
                stack.pop()

            if closeC < openC:
                stack.append(')')
                backtract(openC, closeC+1)
                stack.pop()

        backtract(0,0)
        return res