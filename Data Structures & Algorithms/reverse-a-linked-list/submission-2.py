# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur,prev = head, None

        while cur:
            next_up = cur.next
            cur.next = prev
            prev = cur
            cur = next_up
        
        self.head = prev
        
        return self.head
        