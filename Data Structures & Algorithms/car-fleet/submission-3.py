class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []

        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        
        pairs.sort(reverse = True)

        stack = []

        for pos, speed in pairs:
            time = (target - pos) / speed
            if not stack or stack[-1] < time:
                stack.append(time)
            
        
        return len(stack)