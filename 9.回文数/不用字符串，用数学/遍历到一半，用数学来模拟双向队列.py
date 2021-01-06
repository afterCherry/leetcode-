import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x==0:
            return True
        else:
            length=int(math.log(x,10))+1
            l=length-1
            for i in range(length//2):
                if x//(10**l)!=x%10:
                    return False
                x=(x%(10**l))//10
                l-=2
            return True

