class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        Almost same question as permutations in a string,
        finished problem within 10 minutes.
        TC: O(N) really O(26N) where N is len(s)
        SC: O(n) 26 extra space used to stack chars, N used
        the number of answers. 
        '''
        lengthP = len(p)
        lengthS = len(s)
        if lengthS < lengthP:
            return []
        charsP = [0] * 26
        charsS = [0] * 26
        ans = []
        for i in p:
            charsP[ord(i) - ord('a')] += 1
        #print(charsP)
        
        for i in range(lengthS):
            if i < lengthP:
                charsS[ord(s[i]) - ord('a')] += 1
            else:
                charsS[ord(s[i]) - ord('a')] += 1
                charsS[ord(s[i-lengthP]) - ord('a')] -= 1
            
            if charsP == charsS:
                ans.append(i-(lengthP-1))
        
        return ans
        