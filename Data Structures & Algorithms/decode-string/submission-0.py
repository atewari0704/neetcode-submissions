class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        for letter in s:
            if letter == "]":
                # solve the sub problem
                sub = ""
                while stack[-1] != "[":
                    sub = stack.pop() + sub
                stack.pop() #popping off the "["
                
                muliply_by = ""
                while stack and stack[-1].isdigit():
                    muliply_by = stack.pop() + muliply_by
                
                stack.append(int(muliply_by) * sub)
        
            else:
                stack.append(letter)
                
        return "".join(stack)




        