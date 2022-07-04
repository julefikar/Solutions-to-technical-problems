class Solution(object):
    def totalFruit(self, fruits):
        
        '''
          ABCAC
            v
               v
          Do the sliding window approach. Make a hashmap which counts the instances of THAT character. As we
          iterate through the array, we add the index to hashmap. And WHILE the length of HM is > 2, we have to 
          decrement value of the left pointer (windowStart). When it is 1 instance of that character,
          remove it from hashmap and increment left (windowStart).
          Find the maxFruits by finding max of current maxFruits and the window length + 1.  
          Mistakes: Setting value of hashmap to one thing and the value needed to delete it to another.
          Not initializing correctly in the loops, I put left = fruits[windowStart] after the for loop instead of
          the while loop.
          Improvements: Do more test cases, interpret hashmap values more carefully. And initialize in current loop.
          TC: O(N) The outer for loop runs for all characters, and the inner while 
          loop processes each character only once; therefore, the time complexity of the algorithm will be O(N+N)=O(N)
          SC: O(1) At most 3 keys can be stored.
        '''
        fruit = {}
        (maxFruits, windowStart) = (0, 0)
        for windowEnd in range(len(fruits)):
            right = fruits[windowEnd]
            if right not in fruit:
                fruit[right] = 1
            fruit[right] += 1
            while len(fruit) > 2:
                left = fruits[windowStart]
                fruit[left] -= 1
                if fruit[left] == 1:
                    del fruit[left]
                windowStart += 1
            maxFruits = max(maxFruits, windowEnd - windowStart + 1)
        return maxFruits

