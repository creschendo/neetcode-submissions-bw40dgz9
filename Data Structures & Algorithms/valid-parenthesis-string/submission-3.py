class Solution:
    def checkValidString(self, s: str) -> bool:
        left = [] 
        star = []
        for i in range(len(s)):
            if s[i] == "(":
                left.append(i)
            elif s[i] == "*":
                star.append(i)
            elif s[i] == ")":
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
                    
        while left and star:
            if left.pop() > star.pop():
                return False
        return not left