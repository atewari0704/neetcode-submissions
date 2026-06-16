class Solution:
    def countSubstrings(self, s: str) -> int:
        def check_outward(l,r):
            count = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            
            return count

        count = 0

        for i in range(len(s)):
            #check odd palindrome
            count += check_outward(i,i)
            
            #even palindroms
            count += check_outward(i,i+1)
            
        
        return count

            



