# Leetcode: https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) :
        # s1 = ""
        # s2 = ""
        # while l1 is not None:
        #     s1 += str(l1.val)
        #     l1 = l1.next
        # while l2 is not None:
        #     s2 += str(l2.val)
        #     l2 = l2.next
        def num(head):
            n = 0
            p = 0
            trav = head
            while trav:
                n += trav.val * (10**p)
                p += 1
                trav = trav.next
            return n

        def cal_sum(h1,h2):
            s3 = str(num(h1)+num(h2))
            head = ListNode(-1)
            trav = head
            for i in str(s3)[::-1]:
                trav.next = ListNode(int(i))
                trav = trav.next
            return head.next
        
        return cal_sum(l1,l2)
