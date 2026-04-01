class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def divide(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = divide(arr[:mid])
            right = divide(arr[mid:])

            return merge(left, right)
        
        def merge(left, right):
            l, r = 0, 0
            sol = []
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    sol.append(left[l])
                    l += 1
                else:
                    sol.append(right[r])
                    r += 1
            sol.extend(left[l:])
            sol.extend(right[r:])
            return sol
        
        return divide(nums)
