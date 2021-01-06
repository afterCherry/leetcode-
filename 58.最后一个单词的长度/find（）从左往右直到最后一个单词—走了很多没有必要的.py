class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s=s.strip(" ")
        index=s.find(" ")
        while 1:
            if s.find(" ",index+1)!=-1:
                index=s.find(" ",index+1)
            else:
                return len(s)-index-1
