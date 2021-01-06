# 列表->字符串->int->字符串->列表
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 列表->字符串
        temp_str=""
        for digit in digits:
            temp_str+=str(digit)
        # 字符串->int
        res=int(temp_str)
        res+=1
        # int->字符串
        s=str(res)
        length=len(digits)
        s=s.zfill(length)
        # 字符串->列表
        li=[]
        for ch in s:
            temp=int(ch)
            li.append(temp)
        return li
