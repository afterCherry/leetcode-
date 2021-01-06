class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length=len(s)
        i=length-1
        cnt = 0
        while i>=0:
            while i>=0 and s[i]==" ":
                i-=1
            while i>=0 and s[i]!=" ":
                cnt+=1
                i-=1
            break
        return cnt
