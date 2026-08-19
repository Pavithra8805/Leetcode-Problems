class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        for i in range(1, n):
            for j in range(n):
                up = matrix[i - 1][j]

                left = float('inf')
                if j > 0:
                    left = matrix[i - 1][j - 1]

                right = float('inf')
                if j < n - 1:
                    right = matrix[i - 1][j + 1]

                matrix[i][j] += min(up, left, right)

        return min(matrix[-1])