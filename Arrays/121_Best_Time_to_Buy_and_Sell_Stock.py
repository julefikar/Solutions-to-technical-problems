class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        Loop through array, if next index is lower, make that lowest number.
        If current price minus the lowest price is greater than the profit, make that the profit. Return profit.
        TC: O(N)
        SC: O(1)
        '''
        profit = 0
        lowest = prices[0]
        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            elif prices[i] - lowest > profit:
                profit = prices[i] - lowest
        return profit