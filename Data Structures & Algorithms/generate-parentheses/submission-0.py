class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def BT(openCount,closeCount):
            if openCount == closeCount == n:
                res.append("".join(stack))
            
            #decision: add opening if less than n
            if openCount < n:
                stack.append("(")
                BT(openCount+1,closeCount) # go an make another decision
                stack.pop() # because the stack is shared once you make a decision you also undo it
            
            if closeCount < openCount:
                stack.append(")")
                BT(openCount,closeCount+1) # go an make another decision
                stack.pop()

        BT(0,0)
        return res
            

