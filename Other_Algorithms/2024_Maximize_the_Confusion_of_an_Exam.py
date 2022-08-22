class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        '''
        Sliding Window
        TC: O(N) where N denotes the number of length of answerKeys
        SC: O(1) HM used but constant amount of keys
        '''
        windowStart = 0
        res = 0
        TF = {'T':0,'F':0}
        for windowEnd in range(len(answerKey)):
            TF[answerKey[windowEnd]] += 1
            
            while (windowEnd - windowStart + 1) - max(TF.values()) > k:
                TF[answerKey[windowStart]] -= 1
                windowStart += 1
            
            res = max(res, windowEnd - windowStart + 1)
        return res