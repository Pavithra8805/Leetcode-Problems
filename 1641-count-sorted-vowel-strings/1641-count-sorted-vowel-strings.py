class Solution:
    def countVowelStrings(self, n: int) -> int:
        #---Tabulation

        dp = [1] * 5
        #[1,1,1,1,1]
        '''
            i = 2
            j = 0 [5,1,1,1,1]
            j = 1 [5,4,1,1,1]
            j = 2 [5,4,3,1,1]
            j = 3 [5,4,3,2,1]
            j = 4 [5,4,3,2,1]

            i = 3
            j = 0 [15,4,3,2,1]
            j = 1 [15,10,3,2,1]
            j = 2 [15,10,6,2,1]
            j = 3 [15,10,6,3,1]
            j = 4 [15,10,6,3,1] 
        '''
        for i in range( 2 ,  n + 1): #n 3
           
            for j in range(5):
                dp[j] = sum(dp[j:])

        return sum(dp)

        '''
        ---- Memoization
        # memo = {}

        # def solve(rem, prev):
        #     if rem == 0:
        #         return 1
        #     if (rem, prev) in memo:
        #         return memo[(rem, prev)]
            
        #     count = 0

        #     for i in range(prev, 5):
        #         count += solve(rem - 1, i)
            
        #     memo[(rem, prev)] = count
        #     return count

        # res = solve(n, 0)
        # return res

    ----- Brute force

        # v = "aeiou"

        # def backtrack(index, prev):
        #     if index == n:
        #         return 1
            
        #     count = 0

        #     for i in range(prev, 5):
        #         count += backtrack(index+1, i)
            
        #     return count
        
        # res = backtrack(0,0)
        # return res
'''