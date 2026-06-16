class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)

        for cur,pre in prerequisites:
            prereq[cur].append(pre)
        
        res = []
        visited,cur_visit = set(),set()

        def dfs(num):
            if num in visited: return True
            if num in cur_visit: return False

            cur_visit.add(num)

            for pre in prereq[num]:
                if not dfs(pre): return False
            
            cur_visit.remove(num)
                
            res.append(num)
            visited.add(num)
            return True

        for num in range(numCourses):
            if not dfs(num):
                return []
        
        return res