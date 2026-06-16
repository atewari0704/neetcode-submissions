# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # handle cases where l1 or l2 might not exist


        def make_list(i):
            if i == -1: return  
            cur = ListNode(sum_up[i])
            cur.next = make_list(i-1)
            return cur 

        cur = l1
        l1_str = ""
        while cur:
            l1_str += str(cur.val)
            cur = cur.next
        
        l1_str = l1_str[::-1]

        cur = l2
        l2_str = ""
        while cur:
            l2_str += str(cur.val)
            cur = cur.next
        
        l2_str = l2_str[::-1]

        sum_up = int(l1_str) + int(l2_str)
        sum_up = str(sum_up)

        return make_list(len(sum_up)-1)

        
        

        