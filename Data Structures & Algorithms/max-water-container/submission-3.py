class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        water = 0
        while left < right:
            w = (right - left) * min(heights[left], heights[right])
            water = max(water, w)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return water