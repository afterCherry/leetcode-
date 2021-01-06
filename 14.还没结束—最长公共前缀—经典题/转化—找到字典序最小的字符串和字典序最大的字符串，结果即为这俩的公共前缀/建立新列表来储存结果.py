# 用了列表来存储 字符串->列表->字符串 确实麻烦了

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        str0=min(strs)
        str1=max(strs)
        length=len(str0)
        res=[]
        for i in range(length):
            if str0[i]==str1[i]:
                res.append(str0[i])
            else:
                break
        return "".join(res)
