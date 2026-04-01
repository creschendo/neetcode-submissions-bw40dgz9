class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right, water = 0, len(heights) - 1, 0
        while left < right:
            volume = (right - left) * min(heights[left], heights[right])
            if volume > water:
                water = volume
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return water