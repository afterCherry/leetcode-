class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        pre=self.countAndSay(n-1)

        i=0
        res=""
        for index,item in enumerate(pre):
            if item!=pre[i]:
                res+=str(index-i)+pre[i]
                i=index
        # 最后一个元素
        res+=str(len(pre)-i)+pre[-1]
        return res

