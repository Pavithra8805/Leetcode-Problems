class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], nums[i])

        ans = [0] * n
        suffix_min = float('inf')

        for i in range(n - 1, -1, -1):

            if prefix[i] > suffix_min:
                ans[i] = ans[i + 1]
            else:
                ans[i] = prefix[i]

            suffix_min = min(suffix_min, nums[i])

        return ans