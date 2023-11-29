# Leetcode: https://leetcode.com/problems/add-two-numbers-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Convert a no to int 
        def ti(l1):
            n = 0
            while l1:
                n = n * 10 + l1.val
                l1 = l1.next
            return n
        
        def tl(n):
            ll = None
            while n:
                # sum = 7807
                # 7 will be added then 0,8,7. [7->8->0->7]
                n,val = divmod(n,10)
                ll = ListNode(val,ll)
            return ll or ListNode()
        
        return tl(ti(l1)+ti(l2))
