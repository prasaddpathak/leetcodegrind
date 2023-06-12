class MinStack:

    def __init__(self):
        self.stack = []
        self.heap = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.heap, val)
        
    def pop(self) -> None:
        # if not self.stack: return None
        print(self.stack)
        print(self.heap)
        print('---------')
        self.stack.pop()
        self.heap = self.stack.copy()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # if not self.heap: return -1
        return heapq.nsmallest(1,self.heap)[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()