# 匹配到最小的括号对，就把这对括号删除
# 左括号进栈；右括号不进栈，判断和栈顶是否匹配
# 结束—栈为空

class Solution:
    def isValid(self, s: str) -> bool:
        # 一共就左右两种括号的可能性，key是右括号，非key的value是左括号，后面也好判断
        dic = {")": "(", "]": "[", "}": "{"}
        stack=[]
        for item in s:
            # 栈不空就用到栈顶元素
            if stack:
                # 只能是右括号
                if item in dic :
                    if stack[-1]==dic[item]:
                        stack.pop()
                    else:
                        return False
                # 只能是左括号
                else:
                    stack.append(item)
            # 栈空就先进去一个元素
            else:
                stack.append(item)
            # 以上两个else可以合并，所以对对应的两个if用and合并
        return stack==[]