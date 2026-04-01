class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (index, height)
        best = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                best = max(best, height * (i - idx))
                start = idx  # this bar can extend left to where the popped bar started
            stack.append((start, h))
        
        # anything remaining in the stack extends to the end
        for idx, height in stack:
            best = max(best, height * (len(heights) - idx))
        
        return best