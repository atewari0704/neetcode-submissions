class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            enter,pro = tasks[i]
            tasks[i] = [enter,pro,i]

        tasks.sort(key = lambda task:task[0])

        res,min_heap = [],[] # the priority is the processing time
        i,time = 0,tasks[0][0] # the time the first task can start

        while min_heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(min_heap,tasks[i][1:])
                i += 1
            
            if min_heap:
                pro,idx = heapq.heappop(min_heap)
                time += pro
                res.append(idx)
            else:
                time = tasks[i][0]
        
        return res





















        # map = defaultdict(list)

        # for i,val in enumerate(tasks):
        #     enter,process = val
        #     map[enter].append([process,i])

        # max_time = max(map.keys())
        # pq,res= [],[]
        # heapq.heapify(pq)

        # time,pause= min(map.keys())-1, None

        # while time < max_time:
        #     time += 1

        #     if map.get(time,None) == None: continue

        #     for task in map.get(time,[]):
        #         heapq.heappush(pq,task)
            
        #     if (not pause or time >= pause) and pq:
        #         pro_time,idx = heapq.heappop(pq)
        #         pause = time + pro_time
        #         res.append(idx)
        
        # while pq:
        #     pro_time,idx = heapq.heappop(pq)
        #     res.append(idx)
        
        # return res
            





        