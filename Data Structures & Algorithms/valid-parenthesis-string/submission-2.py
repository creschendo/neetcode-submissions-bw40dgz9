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
        if len(left) > len(star):
            return False
        while left:
            st = star.pop()
            le = left.pop()
            if le > st:
                return False
        return True