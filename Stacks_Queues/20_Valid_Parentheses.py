class Solution(object):
    '''
    Create a hashmap. Set keys and values equaling to opening and closing. Check if opening has a closing, if it doesn't return false.
    TC: O(N)
    SC: O(N)
    '''
    def isValid(self, s):
        if len(s) % 2 == 1 or len(s) == 0: #Every opening must have a closing, so if it's odd, this is not the case.
            return False
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        stack = []
        for i in s:
            if i in bracket_map:
                stack.append(i)
            elif len(stack) == 0 or bracket_map[stack.pop()] != i: #If the poped element is not the value of index, return false.
                return False
        return len(stack) == 0 