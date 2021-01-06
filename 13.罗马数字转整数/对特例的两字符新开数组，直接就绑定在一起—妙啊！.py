class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D":500,"M": 1000,
               "IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        # 字符串是否在，用in 列表
        list=["IV","IX","XL","XC","CD","CM"]
        # s 多加一个没意义的项，则实际长度=原来长度+1，这样当最后的字符单独算时就用上了
        s+=" "
        res ,index= 0,0
        length = len(s)
        # 因为多加的空格，index下标就能用到整个原来字符串了
        while index<length-1:
            if s[index]+s[index+1] in list:
                res+=dic[s[index]+s[index+1]]
                index+=2
            else:
                res += dic[s[index]]
                index += 1
        return res




