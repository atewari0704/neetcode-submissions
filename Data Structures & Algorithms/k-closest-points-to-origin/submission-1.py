import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_dist(point):
            x,y = point
            return math.sqrt(x**2 + y**2)


        #default is a min heapq where the smallest is the highest priority
        distances = []
        length = 0 

        for i, point in enumerate(points):
            dist = -1 * get_dist(point)
            heapq.heappush(distances,(dist,i))
            length += 1

            if length > k:
                heapq.heappop(distances)
                length -= 1
        
        res = []

        while k > 0:
            val,i = heapq.heappop(distances)
            res.append(points[i])
            k -= 1

        return res

 


        # for point in points:

        