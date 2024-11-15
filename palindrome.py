class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x>=0):
            z=x
            a=0
            while z:
                y=z%10
                a=a*10+y
                z=z//10
            
            if(a==x):
                return True
            else:
                return False
        else:
            return False
