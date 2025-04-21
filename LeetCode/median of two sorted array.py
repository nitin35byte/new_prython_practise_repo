class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        i, j = 0, 0

        # Merge nums1 and nums2 into a single sorted list
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        # Append remaining elements from nums1
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        # Append remaining elements from nums2
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        # Calculate the median of the merged array
        m = len(merged)
        if m % 2 == 1:
            return float(merged[m // 2])  # Median for odd length array
        else:
            mid = m // 2
            median = (merged[mid - 1] + merged[mid]) / 2.0
            return float("{:.5f}".format(median))  # Format median to 5 decimal places


# Create an instance of the Solution class
solution = Solution()

# Define the input arrays nums1 and nums2
nums1 = [1, 3]
nums2 = [2]

# Call the findMedianSortedArrays method using the solution instance
median = solution.findMedianSortedArrays(nums1, nums2)
print("Median of the two sorted arrays:", median)




