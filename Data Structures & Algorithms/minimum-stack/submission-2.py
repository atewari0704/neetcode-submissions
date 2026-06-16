import heapq

class MinStack:
    def __init__(self):
        self.stack = []
        self.prev_min = []
        self.min = float("inf")
        self.min_idx = 0
        self.idx = 0 # this is essentially the current idx

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.prev_min.append(self.min_idx)

        if val < self.min:
            self.min_idx = self.idx #the new min idx is the cur idx
            self.min = val
        
        self.idx += 1 # the actual count increases

    def pop(self) -> None:
        self.stack.pop()
        self.idx -= 1 
        prev_min_idx = self.prev_min.pop()

        if not self.stack:
            self.min = float("inf")

        if prev_min_idx != self.min_idx:
            self.min_idx = prev_min_idx # now that the top is popped off it is possible the min changed
            self.min = self.stack[self.min_idx]

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min
        
