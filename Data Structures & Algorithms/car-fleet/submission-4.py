class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        

        pairs.sort(reverse = True)
        
        stack = []

        for pos, spd in pairs:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)
            