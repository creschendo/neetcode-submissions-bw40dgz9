class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # set left and right pointers
        left, right = 0, len(numbers) - 1

        # guaranteed one solution, just set true loop
        while True:
            # candidate value
            val = numbers[left] + numbers[right]

            # the sum is too small, so the left value must increase
            if val < target:
                left += 1

            # the sum is too large, so the right value must decrease
            elif val > target:
                right -= 1

            # target found, 1 indexed so add one
            elif val == target:
                return [left + 1, right + 1]