# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # def dfs(node, target, ancestors):
        #     if not node: return

        #     if node.val == target.val:
        #         ancestors.append(node)
        #         return True
            
        #     if dfs(node.left, target, ancestors):
        #         ancestors.append(node)
        #         return True
            
        #     elif dfs(node.right, target, ancestors):
        #         ancestors.append(node)
        #         return True
        

        # p_ancestors = []
        # q_ancestors = []
        
        # dfs(root, p, p_ancestors)
        # dfs(root, q, q_ancestors)


        # q_ancestors = set(q_ancestors)

        # for ancestor in p_ancestors:
        #     if ancestor in q_ancestors:
        #         return ancestor

        # via bfs
        # each bfs node will have it's cur val and all the parents it came from

        
        p_ancestors,q_ancestors = None,None
        queue = deque([ (root,[]) ])

        while p_ancestors == None or q_ancestors == None:
            cur, ancestors = queue.popleft()
            ancestors.append(cur)

            if cur.val == p.val:
                p_ancestors = ancestors[::]
            
            if cur.val == q.val:
                q_ancestors = ancestors[::]

            if cur.left:
                queue.append( (cur.left, ancestors[::]) )
            
            if cur.right:
                queue.append( (cur.right, ancestors[::]) )

        q_ancestors = set(q_ancestors)

        for ancestor in p_ancestors[::-1]:
            if ancestor in q_ancestors:
                return ancestor

    
        


                

            

        


               


            

        

