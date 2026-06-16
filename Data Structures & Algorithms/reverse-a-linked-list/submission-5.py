# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        q,cur = deque([None]), head

        while cur:
            q.appendleft(cur)
            cur = cur.next
        
        for i in range(len(q)-1):
            q[i].next = q[i+1]
        
        return q[0]


