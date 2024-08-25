class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array to perform binary search on it
        # This helps to minimize the binary search range and handle edge cases effectively
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_length = m + n
        is_odd = total_length % 2 == 1
        
        # Perform binary search on the smaller array
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = (total_length + 1) // 2 - i
            
            maxLeftX = nums1[i - 1] if i > 0 else float('-inf')
            minRightX = nums1[i] if i < m else float('inf')
            
            maxLeftY = nums2[j - 1] if j > 0 else float('-inf')
            minRightY = nums2[j] if j < n else float('inf')
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if is_odd:
                    return max(maxLeftX, maxLeftY)
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            
            elif maxLeftX > minRightY:
                right = i - 1
            else:
                left = i + 1

        raise ValueError("Input arrays are not sorted or have invalid lengths.")

