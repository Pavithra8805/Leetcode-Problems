class Solution(object):
    def maximumSum(self, arr):
        n = len(arr)

        res = arr[0]
        no_del = arr[0]
        one_del = float('-inf')

        for i in range(1, n):
            ele = arr[i]

            n1 = max(ele, no_del + ele)
            n2 = max(ele + one_del, no_del)

            no_del = n1
            one_del = n2
            res = max(res, no_del, one_del)
        return res