class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        to_check = set()
        adj = defaultdict(list)

        def dfs(course,checked):
            if course in checked:
                print(course)
                return False
            
            checked.add(course)

            for pre in adj[course]:
                if not dfs(pre,checked):
                    print(course)
                    return False
            
            checked.remove(course)
            
            return True

        for course, pre in prerequisites:
            to_check.add(course)
            adj[course].append(pre)
        
        for course in to_check:
            if not dfs(course,set()):
                return False
        
        return True 
       