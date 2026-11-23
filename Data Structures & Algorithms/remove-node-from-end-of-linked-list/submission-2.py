# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # go through list and get len and then go through again and remove
        # based on len - nth last node so you really only have to make n-1 
        #reference n+ 1 instead

        length = 0 

        cur = head

        while cur:
            length += 1
            cur = cur.next
        
        removal_i = length - n

        if removal_i == 0:
            head = head.next
            return head

        cur = head
        for i in range(length):
            if i == removal_i - 1:
                cur.next = cur.next.next
                return head
        
            cur = cur.next
