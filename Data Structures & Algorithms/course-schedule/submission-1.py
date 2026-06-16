class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = dict()

        for target,prereq in prerequisites:
            if target not in adj:
                adj[target] = []
            if prereq not in adj:
                adj[prereq] = []
            adj[target].append(prereq)
        

        for course in adj:
            stack = [(course,set())]

            while stack:
                cur,visited = stack.pop()
                print(cur,visited)

                if cur in visited:
                    return False

                visited.add(cur)

                for prereq in adj[cur]:
                    print("intially: ", (prereq,visited))
                    stack.append((prereq,visited.copy()))
                
            adj[course] = [] # if we made it to here then 
            # this course doesn't have circular dependencies

        return True
                


        