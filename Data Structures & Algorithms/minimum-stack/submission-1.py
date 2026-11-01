class MinStack:

    def __init__(self):
        self.stack = []
        self.seen = set()
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val not in self.seen: 
            self.seen.add(val)
        
    def pop(self) -> None:
        del self.stack[-1]
        return None # muss das hin? 
        
    def top(self) -> int:
        val = self.stack[-1]
        return val
        
    def getMin(self) -> int:
        return min(self.seen)

        
