class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_list,s2_list = [0] * 26,[0] * 26
        matches = 0

        for char in s1:
            idx = ord(char) - ord("a")
            s1_list[idx] +=  1

        for i in range(0,len(s1)):
            idx = ord(s2[i]) - ord("a")
            s2_list[idx] += 1
        
        for i in range(26):
            if s1_list[i] == s2_list[i]: 
                matches += 1
        
        if matches == 26: return True

        l = 0
        #sliding window logic
        for r in range(len(s1),len(s2)):
            idx = ord(s2[r]) - ord("a")
            s2_list[idx] = s2_list[idx] + 1

            #adjust matches
            if s1_list[idx] == s2_list[idx]: matches += 1

            if s1_list[idx] + 1 == s2_list[idx]: matches -= 1

            # Left pointer updates below
            idx = ord(s2[l]) - ord("a")
            s2_list[idx] -= 1

            #adjust matches
            if s1_list[idx] == s2_list[idx]: matches += 1

            if s1_list[idx] - 1 == s2_list[idx]: matches -= 1

            l += 1

            if matches == 26: return True
        

        return False
        

        














        # letter_count = dict()

        # for l in s1: letter_count[l] = letter_count.get(l,0) + 1
        
        # i = 0 

        # while i < len(s2):
        #     if s2[i] in letter_count:
        #         j = i
        #         erased = set()

        #         while j < len(s2) and s2[j] in letter_count:
        #             letter_count[s2[j]] = letter_count[s2[j]] - 1

        #             if letter_count[s2[j]] == 0:
        #                 del letter_count[s2[j]]
        #                 erased.add(s2[j])
                    
        #             j += 1
                
        #         if not letter_count: return True
        #         if j >= len(s2): return False

        #         start_again = j

        #         while i != j:
        #             if s2[i] == s2[j] and s2[j] in erased:
        #                 start_again = i
        #             letter_count[s2[i]] = letter_count.get(s2[i],0) + 1
        #             i += 1
                
        #         i = start_again
                    
        #     i += 1
        
        # return False


        # while i < len(s2):
        #     if s2[i] in letter_count:
        #         temp = letter_count.copy()
        #         j = i

        #         while j < len(s2) and s2[j] in temp:
        #             temp[s2[j]] = temp[s2[j]] - 1

        #             if temp[s2[j]] == 0:
        #                 del temp[s2[j]]
                    
        #             j += 1
                
        #         if not temp: return True

        #         # i = j # jump forward
            
        #     i += 1
        
        # return False


        