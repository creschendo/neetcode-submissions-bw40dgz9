class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A
        m, n = len(A), len(B)
        half = (m + n + 1) // 2
        left, right = 0, len(A)
        while left <= right:
            i = (left + right) // 2
            j = half - i

            A_left  = A[i-1] if i > 0 else float("-inf")
            A_right = A[i]   if i < m else float("inf")
            B_left  = B[j-1] if j > 0 else float("-inf")
            B_right = B[j]   if j < n else float("inf")

            # If the upper bound of the left partition of A is greater
            # than the lower bound of the right partition of B, there are 
            # too many A elements, thus go left
            if A_left > B_right:
                right = i - 1
            # If the upper bound of the left partition of B is greater
            # than the lower bound of the right partition of A, there are 
            # too few large elements in A, thus go right
            elif B_left > A_right:
                left = i + 1
            # The partition is valid, so just break and return i
            else:
                if (m + n) % 2 == 1:
                    return max(A_left, B_left)
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
       