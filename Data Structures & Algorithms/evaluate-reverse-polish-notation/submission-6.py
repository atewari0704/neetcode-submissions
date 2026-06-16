class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for x in tokens:
            if x not in "+ - * /": stack.append(int(x))
            
            else:
                num2,num1 = stack.pop(),stack.pop()
 
                if x =="+":
                    stack.append(num1 + num2)
                elif x == "*":
                    stack.append(num1 * num2)
                elif x == "-":
                    stack.append(num1 - num2)
                else:
                    stack.append(int(num1/num2))

        return stack[0]
        