class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        tens, fives = 0, 0

        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
                if not fives:
                    return False
                fives -= 1
            else:
                change = 15
                if tens:
                    tens -= 1
                    change -= 10
                while change > 0:
                    if not fives:
                        return False
                    fives -= 1
                    change -= 5
        return True

                
