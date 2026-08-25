class Solution(object):
    def combinationSum3(self, k, n):
        result = []

        def backtrack(start, temp, remaining):
            # Goal State
            if len(temp) == k:
                if remaining == 0:
                    result.append(temp[:])
                return

            # Exploration
            for num in range(start, 10):
                if num > remaining:
                    break

                temp.append(num)  
                backtrack(num + 1, temp, remaining - num)  
                temp.pop()  

        backtrack(1, [], n)
        return result