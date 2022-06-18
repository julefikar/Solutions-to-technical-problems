class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        '''
        We find out that if a number isn't happy, it will keep repeating the sum of the squares of its digits. So we can
        make a hashset, where we append the values. If value ever is 1, return true.
        TC: O(log n)
        SC: O(log n)
        '''
        def sum_of_digits(n): 
            total_sum = 0
            while n > 0:
                digit = n % 10
                total_sum += digit ** 2
                n = n // 10
            return total_sum
        
        vals_seen = set() 
        while n!=1 and n not in vals_seen:
            vals_seen.add(n) #Appends to HashSet
            n = sum_of_digits(n) # Calls function to add the sum of digits
        return n == 1 #Happy number if n is 1
                
    
        