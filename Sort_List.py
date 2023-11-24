#Leetcode: https://leetcode.com/problems/sort-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Insertion Sort - TLE
        # if head:
        #     t = head
        #     while t:
        #         i = t.next
        #         while i:
        #             if t.val > i.val:
        #                 t.val, i.val = i.val, t.val
        #             i = i.next
        #         t = t.next
        #     return head
        # else:
        #     return head

        #Merge Sort

        # If linked list is null
        if not head or not head.next:
            return head
        
        #Using slow and fast pointers to easily find the mid point
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next

        #initialising it to zero - to identify left and right subsets
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        #Merge sorted linked list

        #Creating a dummy node
        d = ListNode(0)
        c = d
        while left and right:
            if left.val < right.val:
                c.next = left 
                left = left.next
            else:
                c.next = right
                right = right.next
            c = c.next
        c.next = left or right
        return d.next
