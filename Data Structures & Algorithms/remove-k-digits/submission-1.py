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

        first_non_zero_i = 0

        for i,c in enumerate(stack):
            if c != "0":
                first_non_zero_i = i
                break

        res = "".join(stack[first_non_zero_i:])

        return str(int(res)) if res else "0"

