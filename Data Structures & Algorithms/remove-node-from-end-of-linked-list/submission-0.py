# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head

        length = 0 

        while cur:
            length += 1
            cur = cur.next
        

        target = length - n - 1

        if target == -1:
            head = head.next
            return head

        count = 0 
        cur = head
        while cur:
            if count == target:
                cur.next = cur.next.next
                return head
                
            cur = cur.next
            count += 1
        