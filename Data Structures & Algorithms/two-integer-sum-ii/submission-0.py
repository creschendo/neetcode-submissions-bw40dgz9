class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while True:
            val = numbers[left] + numbers[right]
            if val < target:
                left += 1
            elif val > target:
                right -= 1
            elif val == target:
                return [left + 1, right + 1]