class Solution:
    def isPalindrome(self, x: int) -> bool:
        l=list(str(x))
        length=len(l)
        while length>0:
            if l.pop(0)!=l.pop():
                return False
        return True