class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val,self.min_stack[-1]))
        
    def pop(self) -> None:
        del self.stack[-1]
        del self.min_stack[-1]
        
    def top(self) -> int:
        val = self.stack[-1]
        return val
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        

        
