#Palindrome Number
#Maths
#return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
       if x<0:
            return False
        
        temp = x
        pal = 0

        while x!=0:
            rem = x%10
            pal = pal*10 + rem
            x = x//10
        
        if temp == pal:
            return True 
        else:
            return False
