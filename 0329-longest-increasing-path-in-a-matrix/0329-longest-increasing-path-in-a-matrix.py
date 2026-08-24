class Solution(object):
    def longestIncreasingPath(self, matrix):
        m, n = len(matrix), len(matrix[0])
        res = 0

        dp = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]

            dp[i][j] = 1

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for di, dj in directions:
                new_i, new_j = i + di, j + dj

                if (0 <= new_i < m and
                    0 <= new_j < n and
                    matrix[new_i][new_j] > matrix[i][j]):

                    dp[i][j] = max(
                        dp[i][j],
                        1 + dfs(new_i, new_j)
                    )

            return dp[i][j]

        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))

        return res