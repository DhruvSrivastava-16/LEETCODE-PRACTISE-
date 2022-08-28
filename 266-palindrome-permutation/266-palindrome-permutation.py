class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import Counter
        
		# Count the total number of occurences for each character in the string.
        counted = Counter(s)
        counts = 0
		
        # Iterate through the string to find odd occurences. A palindrome can have only one odd number.
        for i in counted:
            if counted[i] % 2 != 0 :
                counts +=1
				
        # Return false if there are multiple odd values in the string.
        if counts > 1:
            return False
        
        return True
            