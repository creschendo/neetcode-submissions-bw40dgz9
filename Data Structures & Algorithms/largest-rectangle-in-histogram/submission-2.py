class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0

        for i, h in enumerate(heights):

            left, right = i, i

            while left >= 0 and heights[left] >= h:
                left -= 1
            
            while right < len(heights) and heights[right] >= h:
                right += 1
            
            best = max(best, (right - left - 1) * h)
        return best