class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        was_letter = False

        for letter in s:
            if letter == "*" and was_letter:
                stack.pop()
                was_letter = False

            else:
                stack.append(letter)
                was_letter = True
        
        return "".join(stack)

            
            


