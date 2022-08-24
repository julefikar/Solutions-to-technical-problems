#Leetcode 567, Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Extremely hard to grasp but a lot of information learned.
        It is basically valid anagram but checking for every window.
        TC: O(26N) = O(N) because every window requires a check, N is length of s2
        SC: O(1) 26 extra space used
        '''
        length = len(s1)
        #If s1 length is ever greater than s2, permumation can't exist in s2
        if length > len(s2):
            return False
        #Create two arrays of 26, to represent each CHARACTER
        hm1= [0] * 26
        hm2= [0] * 26
        for i in s1:
            #Update arr index depending on ASCII values
            hm1[ord(i) - ord('a')] += 1

        
        windowStart = 0
        for windowEnd in range(len(s2)):
            #Get first window which is size of s1
            if windowEnd < length:
                hm2[ord(s2[windowEnd])- ord('a')] += 1
            #Add current index and erase previous index
            else:
                hm2[ord(s2[windowEnd])- ord('a')] += 1
                hm2[ord(s2[windowEnd-length])- ord('a')]-= 1
            #Check if the arrays are equal.
            if hm1 == hm2:
                print(hm2)
                print(hm1)
                return True
        return False