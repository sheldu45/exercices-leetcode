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
        left, right = 0, m
        
        # Perform binary search on the smaller array
        while left <= right:
            # Partition indices for nums1 and nums2
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i
            
            # Handle edge cases for partition boundaries
            # maxLeftX is the largest element on the left side of nums1's partition
            # minRightX is the smallest element on the right side of nums1's partition
            maxLeftX = nums1[i - 1] if i > 0 else float('-inf')
            minRightX = nums1[i] if i < m else float('inf')
            
            # maxLeftY is the largest element on the left side of nums2's partition
            # minRightY is the smallest element on the right side of nums2's partition
            maxLeftY = nums2[j - 1] if j > 0 else float('-inf')
            minRightY = nums2[j] if j < n else float('inf')
            
            # Check if correct partition is found
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If the total number of elements is odd, return the max of left parts
                if (m + n) % 2 == 1:
                    return max(maxLeftX, maxLeftY)
                # If the total number of elements is even, return the average of middle two elements
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            
            # If we are too far on the right side for nums1, move left
            elif maxLeftX > minRightY:
                right = i - 1
            # If we are too far on the left side for nums1, move right
            else:
                left = i + 1

        # Raise error if no valid partition is found (should not happen with valid input)
        raise ValueError("Input arrays are not sorted or have invalid lengths.")
