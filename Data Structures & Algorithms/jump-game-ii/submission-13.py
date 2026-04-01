class Solution:
    def jump(self, nums: List[int]) -> int:
        # BOTTOM UP 
        n = len(nums)
        dp = [1000000] * n
        dp[-1] = 0
        for i in range(n - 2, -1, -1):
            end = min(n, i + nums[i] + 1)
            for j in range(i + 1, end):
                dp[i] = min(dp[i], 1 + dp[j])
                print("i: " + str(i) + " j: " + str(j))
                print(dp)
        return dp[0]
        """
        i: 4 j: 5
        [1000000, 1000000, 1000000, 1000000, 1, 0]
        i: 3 j: 4
        [1000000, 1000000, 1000000, 2, 1, 0]
        i: 2 j: 3
        [1000000, 1000000, 3, 2, 1, 0]
        i: 1 j: 2
        [1000000, 4, 3, 2, 1, 0]
        i: 1 j: 3
        [1000000, 3, 3, 2, 1, 0]
        i: 1 j: 4
        [1000000, 2, 3, 2, 1, 0]
        i: 1 j: 5
        [1000000, 1, 3, 2, 1, 0]
        i: 0 j: 1
        [2, 1, 3, 2, 1, 0]
        i: 0 j: 2
        [2, 1, 3, 2, 1, 0]
        """

        # TOP DOWN
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(nums) - 1:
                return 0
            if nums[i] == 0:
                return 1000000
            
            res = 1000000
            end = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, end):
                res = min(res, 1 + dfs(j))
            memo[i] = res
            return res
        return dfs(0)
        """
        [2, 4, 1, 1, 1, 1]
        memo = {}
        - dfs(0) (1,2)
            res = 1000000
            - dfs(1) (2, 3, 4, 5)
                res = 1000000
                - dfs(2) (3)
                    res = 1000000
                    - dfs(3) (4)
                        res = 1000000
                        - dfs(4) (5)
                            res = 1000000
                                - dfs(5) ()
                                    return 0 (i == len(nums) - 1)
                            res = 1
                            memo = {4: 1}
                        res = 2
                        memo = {4: 1, 3: 2}
                    res = 3
                    memo = {4: 1, 3: 2, 2: 3}
                res = 4 (dfs(2))
                res = 3 (dfs(3))
                res = 2 (dfs(4))
                res = 1 (dfs(5))
                memo = {4: 1, 3: 2, 2: 3, 1: 1}
            res = 2
            - dfs(2)
                return 4 (memo hit)
            res = 2
        return 2








        """