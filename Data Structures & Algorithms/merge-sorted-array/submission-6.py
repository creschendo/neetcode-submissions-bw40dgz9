class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left, right, idx = m - 1, n - 1, m + n - 1

        while left > -1 and right > -1:
            if nums1[left] > nums2[right]:
                nums1[idx] = nums1[left]
                left -= 1
            else:
                nums1[idx] = nums2[right]
                right -= 1
            idx -= 1
        if right > -1:
            nums1[:right + 1] = nums2[:right + 1]
        
        
        

