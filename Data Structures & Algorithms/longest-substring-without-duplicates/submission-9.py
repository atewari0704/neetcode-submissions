class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,res = 0, 0
        visited,hashmap = set(), dict()
        
        for r in range(len(s)):
            if s[r] in visited:
                new_l = hashmap.get(s[r]) + 1

                while l != new_l:
                    visited.remove(s[l])
                    del hashmap[s[l]]
                    l += 1

            
            visited.add(s[r])
            hashmap[s[r]] = r
            sub_len = (r-l)+1
            res = max(sub_len,res)
        
        return res
        
