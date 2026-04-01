class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            return merge(left, right)

        
        def merge(left, right):
            sol = []

            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sol.append(left[i])
                    i += 1
                else:
                    sol.append(right[j])
                    j += 1
            
            sol.extend(left[i:])
            sol.extend(right[j:])

            return sol

        return mergeSort(nums)