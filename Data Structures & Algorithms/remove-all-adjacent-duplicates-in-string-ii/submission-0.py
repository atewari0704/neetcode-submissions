class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [ [s[0],1] ] #(letter,count)

        for i in range(1,len(s)):
            letter = s[i]
            # append (letter,count)

            if stack and letter == stack[-1][0]:
                stack[-1][1] = stack[-1][1] + 1

                if stack[-1][1] == k:
                    stack.pop()
            
            else:
                stack.append( [letter,1] )

        res = ""
        
        for letter, count in stack:
            res += letter * count

        return res



        