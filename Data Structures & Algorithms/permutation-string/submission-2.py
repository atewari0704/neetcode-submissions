class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1
        
        matches = 0 
        for i in range(26):
            if s1Count[i] == s2Count[i]: matches += 1
        

        #if matches = 26 then the current windows are the same

        #slide the window
        l=0
        for r in range(len(s1),len(s2)):
            if matches == 26: return True

            #r is automatically increasing
            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1

            #the  number of matches could increase 
            if s1Count[index] == s2Count[index]: matches += 1

            elif s2Count[index] == s1Count[index] + 1:
                matches -= 1
            
            # L += 1
            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1

            if s1Count[index] == s2Count[index]: matches += 1

            elif s2Count[index] == s1Count[index] - 1:
                matches -= 1
            
            l += 1

        return matches == 26
        





           

            # L+=1 R+=1 






        # letters = dict()

        # for letter in s1: letters[letter] = letters.get(letter,0) + 1

        # s2_len = len(s2)

        # for l in range(len(s2)):
        #     if s2[l] in letters:
        #         temp = letters.copy()
        #         r = l
        #         while r < s2_len and s2[r] in temp:
        #             temp[s2[r]] -= 1

        #             if temp[s2[r]] == 0:
        #                 del temp[s2[r]]
                    
        #             if len(temp) == 0: 
        #                 return True
                    
        #             r += 1
        # return False

    

        