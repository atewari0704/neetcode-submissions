class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        direct_mapping = defaultdict(list)

        for p,c in prerequisites: direct_mapping[c].append(p)


        # we want to also have all the indirect prereqs available right away

        all_mapping = defaultdict(set)

        # get the mapping of my child and make it my own as well

        def dfs(c):
            if all_mapping.get(c):
                return all_mapping[c]
            
            for p in direct_mapping.get(c,[]):
                all_mapping[c].update( dfs(p) )
            
            all_mapping[c].add(c) # the course is a prereq of itself

            return all_mapping[c]

        
        for c in range(numCourses):
            dfs(c)


        res = []

        for p,c in queries:
            res.append(p in all_mapping[c])

        return res