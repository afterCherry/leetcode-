# 没有验证


# 能不能找得到：
# 找得到可以 return True,更准确的是 return index
# 找不到可以 return False,另外常用的是 return -1 来表示

def find(str1,str2):
    length1=len(str1)
    length2=len(str2)

    for i in range(length2):
        # 先找到第一个匹配的字符，才有往后匹配的可能
        if str2[i]==str1[0]:
            # index 记录匹配的首位置
            index=i
        for j in range(1,length1):
            if str1[j]==str2[i]:
                index+=1
            else:
                # break 出 for j 循环，再去 for i 看能不能找到下一个index
                break
        if j==length1:
            return index
        else:
            return -1


