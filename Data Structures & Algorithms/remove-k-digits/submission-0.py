class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        pass

        # recursive solution where we reframe the question as 
        # keeping len(n) - k ints remaining

        stack = []

        for c in num:
            while k and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
        
        stack = stack[:len(stack)-k]
        res = "".join(stack)
        return str(int(res)) if res else "0"

