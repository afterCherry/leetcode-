class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D":500,"M": 1000,
               "IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        res=0
        length=len(s)
        for index,value in enumerate(s):
            if index<length-1 and dic[s[index+1]]>dic[s[index]]:
                res += - dic[s[index]]
            else:
                res +=  dic[s[index]]
        return res




