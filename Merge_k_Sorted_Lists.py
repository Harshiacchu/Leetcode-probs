# Leetcode: https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        l = []
        for i in range(n):
            while lists[i]:
                t = lists[i].val
                l.append(t)
                lists[i] = lists[i].next
                # print(t)
        l = sorted(l)
        head = ListNode(-1)
        trav = head
        for i in l:
            trav.next = ListNode(int(i))
            trav = trav.next
        return head.next
