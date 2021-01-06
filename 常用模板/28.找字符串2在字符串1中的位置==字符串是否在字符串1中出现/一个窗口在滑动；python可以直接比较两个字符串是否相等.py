class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        len1=len(haystack) # 字符串长度用len()
        len2=len(needle)
        # i的取值范围是举例子归纳出来的
        for i in range(len1-len2+1):
                # 列表下标区间是前闭后开
                if haystack[i:i+len2]==needle:
                    return i
        return -1