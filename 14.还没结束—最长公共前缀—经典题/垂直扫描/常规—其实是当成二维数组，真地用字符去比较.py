# 找最长公共前缀的优点—匹配成功的子串是在所有字符串首下标是0
# 控制strs[0],遍历strs剩余的，返回结果
# 1.对strs[0]都遍历完了，那就是strs[0]了
# 2.对遍历的字符串本身也遍历完了，那就是这个字符串了
# 以上都是直接用了某一个字符串—一个参考字符串，一个遍历字符串
# 3.公共：当前匹配不了了，则返回之前的匹配成功的

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        length=len(strs)
        length0=len(strs[0])
        for i in range(length0):
            ch=strs[0][i]
            for j in range(1,length):
            # 外边在i+=1的
                if i==len(strs[j]) or ch!=strs[j][i]:
                    return strs[0][:i]
        return strs[0]
