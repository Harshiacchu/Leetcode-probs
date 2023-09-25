# Leetcode: https://leetcode.com/problems/rotate-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        # cur = head
        # l = 1
        # while cur.next:
        #     cur = cur.next
        #     l += 1
        # cur.next = head

        # k = l - (k%l)
        # while k > 0:
        #     cur = cur.next
        #     k -= 1
        
        # h = cur.next
        # cur.next = None
        # return h
        l = []
        while head:
            l.append(head.val)
            head = head.next 
        if k>len(l):
            k = int(k%len(l))
        l = (l[-k:] + l[:-k])
        h = ListNode(-1)
        t = h
        for i in l:
            t.next = ListNode(i)
            t = t.next
        return h.next
