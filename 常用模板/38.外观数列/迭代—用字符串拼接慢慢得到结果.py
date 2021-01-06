# 数字也是字符串

class Solution:
    def countAndSay(self, n: int) -> str:
        # 第一项直接给出来，后面才能做到对前面的描述
        pre = ""
        cur = "1"
        for i in range(1,n):
            # 一样的操作进行循环—可以用多位的方便找规律 e.g.111221
            pre=cur
            cur=""   #cur当前项结果—就是对前一项pre进行拼接 次数+数字
            start=end=0
            while end<len(pre):
                while end<len(pre) and pre[start]==pre[end]  :
                    end+=1
                cur+=str(end-start)+pre[start]
                start=end
        return cur