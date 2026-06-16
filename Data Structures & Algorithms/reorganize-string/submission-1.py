class Solution:
    def reorganizeString(self, s: str) -> str:
        map = dict()
        for letter in s: map[letter] = map.get(letter,0) + 1


        pq = []
        for key in map:
            pq.append([0,-1 * map[key],key])
        
        heapq.heapify(pq)
        

        prev,res = None,""

        while pq:
            print(pq)
            priority,count,letter = heapq.heappop(pq)
            print(res)
            if prev == letter: return ""

            prev = letter 

            res += letter

            for i in range(len(pq)):
                if pq[i][0] == 1:
                    pq[i][0] = 0
                    
            
            if count != -1:
                pq.append([1,count+1,letter])
            
            heapq.heapify(pq)
        
        return res




