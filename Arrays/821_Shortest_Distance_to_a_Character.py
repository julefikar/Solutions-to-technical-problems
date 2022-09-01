class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        def helper(arrC, i):
            minimum = float("inf")
            for x in arrC:
                minimum = min(minimum, abs(x-i))
            return minimum
        
        ans = []
        occurances = []
        for i in range(len(s)):
            if s[i] == c:
                occurances.append(i)
        print(occurances)
        
        for i in range(len(s)):
            minDistance = helper(occurances,i)
            ans.append(minDistance)
        return ans