class Solution:
    def countVowelStrings(self, n: int) -> int:
        memo = {}

        def solve(rem, prev):
            if rem == 0:
                return 1

            if (rem, prev) in memo:
                return memo[(rem, prev)]

            count = 0

            for i in range(prev, 5):
                count += solve(rem - 1, i)

            memo[(rem, prev)] = count
            return count

        return solve(n, 0)