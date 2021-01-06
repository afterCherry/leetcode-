# 返回第一次的匹配位置
# 后面的 if else 一定要有，否则OJ平台提示内部出错

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle) if needle in haystack else -1