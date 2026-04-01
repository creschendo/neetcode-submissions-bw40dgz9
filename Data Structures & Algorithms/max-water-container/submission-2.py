class Solution:
    def maxArea(self, heights: List[int]) -> int:
        sol = float("-inf")
        left, right = 0, len(heights) - 1
        while left < right:
            vol = (right - left) * min(heights[left], heights[right])
            sol = max(vol, sol)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return sol