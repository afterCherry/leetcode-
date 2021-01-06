# 这个迭代要更简单，更容易理解
class Solution:
    def countAndSay(self, n: int) -> str:
        pre="1"
        for _ in range(1,n):
            i=0
            cur=""
            for index,item in enumerate(pre):
                if item!=pre[i]:
                    cur+=str(index-i)+pre[i]
                    i=index
            pre=cur+str(len(pre)-i)+pre[-1]
        return pre