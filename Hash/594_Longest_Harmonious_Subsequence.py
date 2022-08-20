class Solution:
    def findLHS(self, nums: List[int]) -> int:
        #Subsequence - number of "exceptions" don't matter
        #When we want most of something, if frequency is relevant, use a HM
        #TC: O(N) #Just iterating through HM N times where N is number of unique nums
        #SC: O(N) #Use of HM
        digits = Counter(nums)
        ans = 0
        for digit in digits:
            complement = digit - 1
            if complement in digits:
                ans = max(ans, digits[digit] + digits[complement])
        return ans
        