import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_dist(point):
            x,y = point
            return math.sqrt(x**2 + y**2)


        #default is a min heapq where the smallest is the highest priority
        distances = []

        for i, point in enumerate(points):
            dist = get_dist(point)
            heapq.heappush(distances,(dist,i))
        
        res = []

        while k > 0:
            val,i = heapq.heappop(distances)
            res.append(points[i])
            k -= 1

        return res

 


        # for point in points:

        