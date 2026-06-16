class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0 # the index of t we current

        for char in s:
            if char == t[i]:
                i += 1
            
            if i >= len(t):
                return 0
        
        return len(t) - i
        

