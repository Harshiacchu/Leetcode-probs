#  Leetcode: https://shorturl.at/kzMVW
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1 = sorted(nums1+nums2)
        # print(float(5)/float(2))
        return nums1[len(nums1)//2] if len(nums1)%2!=0 else (float(nums1[len(nums1)//2])+float(nums1[len(nums1)//2-1]))/float(2)
