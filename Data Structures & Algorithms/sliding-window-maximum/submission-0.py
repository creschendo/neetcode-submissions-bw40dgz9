class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # output
        sol = []

        # queue
        #   - stores indices rather than values for efficient window tracking
        queue = deque()

        # left and right window indices
        left, right = 0, 0

        while right < len(nums):
            # pop smaller values from queue
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            # remove left value from window
            if left > queue[0]:
                queue.popleft()

            # append current window max
            if (right + 1) >= k:
                sol.append(nums[queue[0]])
                left += 1
            right += 1

        return sol