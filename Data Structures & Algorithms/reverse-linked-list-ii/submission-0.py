# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head

        cur,i = head,1 # what we need to start off with

        def reverse_it(cur,prev,i):
            left_node = cur

            while i <= right:
                if i == right: 
                    right_node = cur

                next_up = cur.next
                cur.next = prev
                prev = cur
                cur = next_up

                i += 1
            
            left_node.next = cur # only happens when we are at right + 1

            return right_node

        while i <= left:
            if i+1 == left:
                cur.next = reverse_it(cur.next,cur,i+1)
                break

            elif i == left:
                head = reverse_it(cur,None,i) # the prev is none and left is the starting node
                break

            i += 1
            cur = cur.next
        
        return head










