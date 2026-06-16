class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = dict()

        for letter in s1: letters[letter] = letters.get(letter,0) + 1

        s2_len = len(s2)

        for l in range(len(s2)):
            if s2[l] in letters:
                temp = letters.copy()
                r = l
                while r < s2_len and s2[r] in temp:
                    temp[s2[r]] -= 1

                    if temp[s2[r]] == 0:
                        del temp[s2[r]]
                    
                    if len(temp) == 0: 
                        return True
                    
                    r += 1
        return False

    

        