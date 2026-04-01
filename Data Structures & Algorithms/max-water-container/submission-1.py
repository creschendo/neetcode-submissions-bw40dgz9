class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # set left and right pointers and max water tracker
        left, right, water = 0, len(heights) - 1, 0

        while left < right:
            # current volume, the difference in indexes times min height
            volume = (right - left) * min(heights[left], heights[right])

            # move the smaller wall pointer inward
            # default to moving right if same height
            if volume > water:
                water = volume
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return water