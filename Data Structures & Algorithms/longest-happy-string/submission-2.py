class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        pq = [(-a,"a"),(-b,"b"),(-c,"c")]
        heapq.heapify(pq)
        res = ""
        jail = None 

        while pq:
            count,letter = heapq.heappop(pq)
            if count == 0:  continue 

            count += 1
            res += letter

            if jail:
                heapq.heappush(pq, (jail) )
                jail = None
            
            if len(res) >= 2 and res[-1] == res[-2]:
                jail = (count,letter)
            
            elif count < 0:
                heapq.heappush(pq, (count,letter) )
        
        return res


        