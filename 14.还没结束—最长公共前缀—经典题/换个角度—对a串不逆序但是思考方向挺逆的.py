# 妙啊！————求的是最长公共前缀，反而是对字符串逆向着去思考的

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        s=strs[0]
        for i in range(len(strs)):
            # 确实是该用while来实现不断地不要最后一个字符
            while strs[i].find(s)!=0:
                s=s[:-1]
        return s