class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left, right = 0, 0
        seen = set()
        for i in range(min(k, len(nums))):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            right += 1
        
        while right < len(nums):
            if nums[right] in seen:
                return True
            seen.add(nums[right])
            seen.remove(nums[left])
            left += 1
            right += 1
        

        return False
