class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        mer=nums1+nums2
        mer.sort()
        l=len(mer)
        sum=0
        if l%2==1:
            return float(mer[l//2])
        else:
            mid1=mer[(l//2)-1]
            mid2=mer[l//2]
            mid=(float(mid1)+float(mid2))/2
            return mid
        
#TIME COMPLEXITY : O(l)
#SPACE COMPLEXITY : O(l*l)