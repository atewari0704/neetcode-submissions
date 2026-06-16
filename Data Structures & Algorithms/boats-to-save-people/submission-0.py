class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort people

        # two pointers
        # check if l + r <= limit if yes count += 1 and l+=1 and r-=1 
        # if l + r >= limit count += 1 and r -= 1 (priortizing right)

        people.sort()
        l,r = 0,len(people)-1
        count = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1

            r -= 1
            count += 1
        
        return count
        