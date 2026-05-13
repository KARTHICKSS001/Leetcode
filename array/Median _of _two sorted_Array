class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = sorted(nums1 + nums2)
        n = len(merge)
        mid = n // 2

        if n % 2 == 0:
            return (merge[mid - 1] + merge[mid]) / 2
        else:
            return merge[mid]
