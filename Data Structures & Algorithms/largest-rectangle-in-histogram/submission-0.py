class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # increasing height stack, top is higher, bottom lower
        stack = [] # pair: (index, height)
        maxArea = 0

        # iterate through every height and index
        for i, h in enumerate(heights):
            # starting index of current rectangle
            start = i

            # extend the current rectangle backwards if possible
            # since previous rectangles are higher, they cant extend forwards anymore
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # recompute max area
                maxArea = max(maxArea, height * (i - index))

                # set left bound
                start = index
            # we've considered max possible left bound from current right bound, 
            # just add the new start index and height
            stack.append((start, h))
        
        # everything left in stack can reach the very end,
        # so consider the heights reaching from start to len(heights)
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea