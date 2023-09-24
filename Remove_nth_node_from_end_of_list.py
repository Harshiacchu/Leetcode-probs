# Leetcode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        l = []
    
        while head:
            t = head.val
            l.append(t)
            head = head.next
                # print(t)
        l.pop(len(l)-n)
        head1 = ListNode(-1)
        trav = head1
        for i in l:
            trav.next = ListNode(int(i))
            trav = trav.next
        return head1.next
        
