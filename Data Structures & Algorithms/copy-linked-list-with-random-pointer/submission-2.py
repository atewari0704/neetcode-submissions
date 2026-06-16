"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_nodes = dict() #OG Node: Copy Node
        
        def copy(node):
            if not node: return

            cur_copy = Node(node.val)

            new_nodes[node] = cur_copy
        
            if node.next:
                cur_copy.next = copy(node.next)
   
            return cur_copy

        copy(head) # copying the next nodes

        cur = head
        while cur:
            # print("OG value:",cur.val)
            cur_copy = new_nodes[cur]

            if cur.random:
                cur_copy.random = new_nodes[cur.random]
                # print("NEW:", cur_copy.val, cur_copy.random.val)

            cur = cur.next

        
        return new_nodes.get(head,None)
            




        