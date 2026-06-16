class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = ["(","{","["]

        for b in s:
            if b in opening_brackets:
                stack.append(b)

            else:
                if not stack: return False

                last_opening = stack.pop()

                if b == "}" and last_opening != "{": return False

                elif b == ")" and last_opening != "(": return False

                elif b == "]" and last_opening != "[": return False

        if not stack: return True # all the opening should be pooped if matched with close

        return False