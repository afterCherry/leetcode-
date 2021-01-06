# 缺点：和C串求前缀的时候，会重新从第一个字符开始记录，增加不必要的计算


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length=len(strs)
        j=0
        res=[]
        i=1
        while 1:
            while i<length:
                flag=1
                if strs[i][j] != strs[0][j]:
                    flag=0
                else:
                    i += 1
            if flag==1:
                res.append(strs[0][j])
                j+=1
            else:
                break
        return res




