class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        str0=min(strs)
        str1=max(strs)
        length=len(str0)
        for i in range(length):
            if str0[i]!=str1[i]:
                return str0[:i]
        # 特例：最小串和最大串是一样的
        return str0