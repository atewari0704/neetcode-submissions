import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_heap = [-1 * cnt for cnt in count.values()]
        heapq.heapify(max_heap) # done inplace

        q = deque([])

        time = 0

        while max_heap or q:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1 # the new count now that the frequency for this letter has changed
                if cnt < 0:
                    reenter = time + n # can only re enter when after the given time
                    q.append((cnt,reenter))

            # is anything elgible to reeneter
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0]) 
        
        return time

       