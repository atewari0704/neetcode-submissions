class MinStack:
    def __init__(self):
        self.stack = []
        self.cur_min = [] 
        self.min = float("inf")
 
    def push(self, val: int) -> None:
        self.stack.append(val)

        self.min = min(self.min,val)
        
        self.cur_min.append(self.min)
        

    def pop(self) -> None:
        self.stack.pop()
        self.cur_min.pop()

        if not self.cur_min:
            self.min =  float("inf") 
        else:
            self.min = self.cur_min[-1]

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min
        
