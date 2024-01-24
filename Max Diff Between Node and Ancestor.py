# Leetcode: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/?envType=daily-question&envId=2024-01-11

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxdiff = 0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        self.maxval(root, root.val, root.val)
        return self.maxdiff
    def maxval(self, currnode, minvalue, maxvalue):

        if currnode:
            minvalue = min(minvalue, currnode.val)
            maxvalue = max(maxvalue, currnode.val)
            self.maxdiff = max(self.maxdiff, maxvalue-minvalue)
        
            self.maxval(currnode.left, minvalue, maxvalue)
            self.maxval(currnode.right, minvalue, maxvalue)
    
    
