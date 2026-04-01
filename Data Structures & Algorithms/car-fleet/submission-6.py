class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []

        for i in range(len(speed)):
            pairs.append((position[i], speed[i]))
        
        pairs.sort(reverse = True)

        stack = []
        print(pairs)
        for pos, speed in pairs:
            time = (target - pos) / speed
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)
        
        return len(stack)