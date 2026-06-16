# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def build(n1,n2,add_one):
            if not n1 and not n2: 
                if add_one: return ListNode(1)
                return None

            sum_val = 0 if not add_one else 1


            if n1: 
                sum_val += n1.val
                n1 = n1.next
            
            if n2:
                sum_val += n2.val
                n2 = n2.next
            
            if sum_val >= 10 :
                add_one = True
                sum_val -= 10
            
            else:
                add_one = False
            
            cur = ListNode(sum_val)

            cur.next = build(n1,n2,add_one)

            return cur 
            

        return build(l1,l2,False)

        # def make_list(i):
        #     if i == -1: return  
        #     cur = ListNode(sum_up[i])
        #     cur.next = make_list(i-1)
        #     return cur 

        # cur = l1
        # l1_str = ""
        # while cur:
        #     l1_str += str(cur.val)
        #     cur = cur.next
        
        # l1_str = l1_str[::-1]

        # cur = l2
        # l2_str = ""
        # while cur:
        #     l2_str += str(cur.val)
        #     cur = cur.next
        
        # l2_str = l2_str[::-1]

        # sum_up = int(l1_str) + int(l2_str)
        # sum_up = str(sum_up)

        # return make_list(len(sum_up)-1)

        
        

        