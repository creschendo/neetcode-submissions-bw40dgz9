class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # Time complexity: O(n)
        # Space complexity: O(n)

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

            # append max only if window size has been reached
            if (right + 1) >= k:
                sol.append(nums[queue[0]])
                left += 1
            right += 1

        return sol

        """
        Explanation: 
        Window position            Max
        ---------------           -----
        [1  2  1] 0  4  2  6        2
        1 [2  1  0] 4  2  6         2
        1  2 [1  0  4] 2  6         4
        1  2  1 [0  4  2] 6         4
        1  2  1  0 [4  2  6]        6

        Step 1:
        queue = [1]
        - nothing added to solution, right += 1

        Step 2:
        queue = [2]
        - 1 gets popped since it's smaller than 2, 2 gets pushed
        - nothing added, right += 1

        Step 3:
        queue = [2, 1]
        sol = [2]
        - nothing to pop, push 1 since it's smaller
        - add 2, the leftmost element to solution
        - left += 1, right += 1

        Step 4:
        queue = [2, 1, 0]
        sol = [2, 2]
        - add 2 to sol
        - left += 1, right += 1

        Step 5:
        queue = [4]
        sol = [2, 2, 4]
        - pop 2, 1, 0 since all smaller than 4
        - add 4 to both queue and solution
        - left += 1, right += 1

        Step 6:
        queue = [4, 2]
        sol = [2, 2, 4, 4]
        - nothing popped, just add 2 
        - add 4 to sol
        - left and right increment

        Step 7:
        queue = [6]
        sol = [2, 2, 4, 4, 6]
        - 4 and 2 get popped, since smaller than 6
        - 6 gets added to sol
        """