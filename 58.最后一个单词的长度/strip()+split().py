# s=s.strip() 去除首尾空白字符串
# s.split(" ") 得到以空格分开的元素列表，元素是字符串

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 剪枝
        if not s:
            return 0
        s=s.strip()
        if len(s)==1:
            return 1
        else:
            s_res=s.split(" ")
            return len(s_res[-1])