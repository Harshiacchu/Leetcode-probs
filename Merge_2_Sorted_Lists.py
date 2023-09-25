# Leetcode: https://leetcode.com/problems/merge-two-sorted-lists/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # l = []
        # while list1:
        #     l.append(list1.val)
        #     list1 = list1.next
        # while list2:
        #     l.append(list2.val)
        #     list2 = list2.next
        # l.sort()
        # # print(l)
        # l1 = ListNode(-1)
        # t = l1
        # for i in l:
        #     t.next = ListNode(i)
        #     t = t.next
        # return l1.next

        h = ListNode()
        curr = h
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return h.next
