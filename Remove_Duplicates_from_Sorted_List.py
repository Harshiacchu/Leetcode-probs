# Leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = []
    
        while head:
            t = head.val
            l.append(t)
            head = head.next
                # print(t)
        l = sorted(set(l))
        head1 = ListNode(-1)
        trav = head1
        for i in l:
            trav.next = ListNode(int(i))
            trav = trav.next
        return head1.next
        
