# 列表->字符串->int->字符串->列表
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length=len(digits)
        # 列表->字符串
        temp_str=""
        for num in digits:
            temp_str+=str(num)
        # 字符串->int
        temp_res=int(temp_str)
        temp_res+=1
        # int->字符串
        s=str(temp_res)
        s=s.zfill(length)
        # 字符串->列表
        list=[]
        for ch in s:
            digit=int(ch)
            list.append(digit)
        return list

