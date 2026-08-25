class Solution:

    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)

        ans = 0

        for i in range(2, n):
            ans = max(ans, stones[i] - stones[i - 2])

        return max(ans, stones[1] - stones[0])