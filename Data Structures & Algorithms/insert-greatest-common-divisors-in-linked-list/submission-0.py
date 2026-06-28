import math 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        r = head.next

        while l and r:
            gcd = ListNode(math.gcd(l.val,r.val))
            l.next = gcd 
            gcd.next = r 

            l = r 
            r = r.next
        
        return head

        