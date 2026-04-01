class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        one, two = m - 1, n - 1
        index = m + n - 1

        while one >= 0 and two >= 0:
            if nums1[one] > nums2[two]:
                nums1[index] = nums1[one]
                one -= 1
            else:
                nums1[index] = nums2[two]
                two -= 1
            index -= 1
        if two >= 0:
            nums1[:index + 1] = nums2[:two + 1]

        
