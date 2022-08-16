class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Very similar to first problem except we are checking for every positive profit instance.
        If the difference is positive, we will set the windowStart to windowEnd, so we don't
        accidentally add additional days. 
        If difference is negative, we are at a lowest point, so set point to that.
        TC: O(N) where N is number of len(prices)
        SC: O(1) no extra DS used
        '''
        windowStart = 0 
        total = 0
        for windowEnd in range(len(prices)):
            difference = prices[windowEnd] - prices[windowStart]
            if difference > 0:
                total += difference
                windowStart = windowEnd #Key!
            elif difference < 0:
                windowStart = windowEnd
        return total
            