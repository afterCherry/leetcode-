class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        import re
        res=re.search(needle,haystack)
        # 是否存在是与None比较
        if res!=None:
            return res.span()[0]
        else:
            return -1
