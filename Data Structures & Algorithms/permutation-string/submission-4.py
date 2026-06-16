class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letter_count = dict()

        for l in s1:
            letter_count[l] = letter_count.get(l,0) + 1
        
        i = 0 

        while i < len(s2):
            if s2[i] in letter_count:
                temp = letter_count.copy()
                j = i

                while j < len(s2) and s2[j] in temp:
                    temp[s2[j]] = temp[s2[j]] - 1

                    if temp[s2[j]] == 0:
                        del temp[s2[j]]
                    
                    j += 1
                
                if not temp: return True

                # i = j # jump forward
            
            i += 1
        
        return False


        