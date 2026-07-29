# Core Trick: You are shifting your partition from left to right in nums1.

# Aleft   | Aright
# ---------|---------
# ...      | ...

# Bleft   | Bright
# ---------|---------
# ...      | ...

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        total = m + n
        half = (total + 1) // 2

        left = 0
        right = m

        while left <= right:

            partitionA = (left + right) // 2
            partitionB = half - partitionA

            Aleft = float("-inf") if partitionA == 0 else nums1[partitionA - 1]
            Aright = float("inf") if partitionA == m else nums1[partitionA]

            Bleft = float("-inf") if partitionB == 0 else nums2[partitionB - 1]
            Bright = float("inf") if partitionB == n else nums2[partitionB]

            # -------------------------
            # Case 1 : Correct partition
            # -------------------------
            if Aleft <= Bright and Bleft <= Aright:

                if total % 2 == 1:
                    return max(Aleft, Bleft)

                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # -------------------------
            # Case 2 : Too many elements taken from A
            # Move LEFT
            # -------------------------
            elif Aleft > Bright:
                right = partitionA - 1

            # -------------------------
            # Case 3 : Too few elements taken from A
            # Move RIGHT
            # -------------------------
            else:
                left = partitionA + 1