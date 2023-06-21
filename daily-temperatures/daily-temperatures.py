class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = [] # [temp, index]
        for i, day in enumerate(temperatures):
            while stack and day > stack[-1][0]:
                dayT, dayIndex = stack.pop()
                res[dayIndex] = i-dayIndex
            stack.append([day, i])

        return res
