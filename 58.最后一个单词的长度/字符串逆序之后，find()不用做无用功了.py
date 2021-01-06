class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        # 剪枝
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        s=s[::-1]
        index=s.find(" ")
        if index==-1:
            return len(s)
        return index
