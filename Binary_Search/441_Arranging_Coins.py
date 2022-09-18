class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Brute force O(N)
        # rows = 1
        # count = 1
        # while count <= n:
        #     rows += 1
        #     count += rows
        # return rows-1 if rows != 1 else rows
        '''
        Brute force was simple to think of and code up, the log n solution requires thought,
        idk if anyone can do it without knowing the Gauss's function
        TC: O(log(n))
        SC: O(1)
        '''
        low = 1
        high = n
        ans = 1
        while low <= high:
            mid = low + (high - low) // 2
            maxCoins = (mid + 1) * (mid / 2) #Gauss Algorithm to see how many coins up until mid row.
            if maxCoins > n:
                high = mid - 1
            else:
                low = mid + 1
                ans = mid
        return ans