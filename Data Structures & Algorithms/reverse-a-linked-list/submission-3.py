# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur,prev = head, None

        def recurse(prev,cur):
            if not cur: return prev

            next_up = cur.next
            cur.next = prev

            #get ready for next step/cycle
            prev = cur
            cur = next_up

            return recurse(prev,cur)

        self.head = recurse(prev,cur)

        return self.head


        # while cur:
        #     next_up = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = next_up
        
        #  prev

        # return self.head
        