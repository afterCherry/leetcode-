class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # len1=len(haystack)
        # len2=len(needle)
        len1,len2=len(haystack),len(needle) #python可以这样

        # 剪枝—空字符串
        if len2==0:
            return 0

        # 先串1，再串2—逻辑也清楚
        begin1=0
        while begin1<=len1-len2:
            begin2=0
            while begin2<len2:
                if haystack[begin1] == needle[begin2]:
                    begin1 += 1
                    begin2 += 1
                # 不相等就开始新的一轮比较或者看是否可以结束了
                else:
                    break
            if begin2 == len2:
                return begin1 - len2
            begin1 = begin1 - begin2 + 1 # 执行结束去begin2=0—循环的妙处
        return -1





