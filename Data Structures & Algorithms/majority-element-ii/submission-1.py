class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num1 = num2 = -1
        cnt1 = cnt2 = 0

        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                cnt1 = 1
                num1 = num
            elif cnt2 == 0:
                cnt2 = 1
                num2 = num
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 = 0, 0

        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
        
        sol = []
        if cnt1 > n // 3:
            sol.append(num1)
        if cnt2 > n // 3:
            sol.append(num2)

        return sol




        """
        O(n) time, O(n) space
        counts = {}
        sol = []
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for n, c in counts.items():
            if c > (len(nums) // 3):
                sol.append(n)

        return sol
        """