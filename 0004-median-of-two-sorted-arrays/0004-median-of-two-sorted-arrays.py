class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # TimeComplexity ---- O((n+m)*log(n+m))
        # merged = nums1+nums2
        # merged.sort()
        # k=len(merged)
        # return merged[len(merged)//2] if k%2 else float(merged[k//2-1]+merged[k//2])/2
        # -----------------------------
        # TimeComplexity ---- O(n+m)
        i, j, m1, m2 = 0, 0, 0, 0
        n=len(nums1)+len(nums2)
        for _ in range(n//2+1):
            m2 = m1
            if (i != len(nums1) and j != len(nums2)):
                if (nums1[i] > nums2[j]):
                    m1 = nums2[j]
                    j+=1
                else:
                    m1 = nums1[i]
                    i+=1
            elif (i < len(nums1)):
                m1 = nums1[i]
                i+=1
            else:
                m1 = nums2[j]
                j+=1
        if n%2:
            return m1
        return float(m1+m2)/2
    
        # TimeComplexity ---- O(log(n+m)) ??

        