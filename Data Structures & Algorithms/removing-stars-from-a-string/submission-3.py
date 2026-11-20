class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for letter in s:
            if s == "*":
                stack.pop()
            else:
                stack.append(s)
        
        return "".join(stack)

            
            


