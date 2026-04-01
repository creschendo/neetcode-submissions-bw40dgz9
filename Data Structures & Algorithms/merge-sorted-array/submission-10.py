class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        one, two, ptr = m - 1, n - 1, m + n - 1

        while one >= 0 and two >= 0:
            if nums1[one] > nums2[two]:
                nums1[ptr] = nums1[one]
                ptr -= 1
                one -= 1
            else:
                nums1[ptr] = nums2[two]
                ptr -= 1
                two -= 1
        

        while two >= 0:
            nums1[ptr] = nums2[two]
            ptr -= 1
            two -= 1

