import re
a = r"umji"
# 子串在前
# search() 扫描整个字符串并返回第一个成功的匹配
match = re.search(a,'umji isbest umji inworld')
if match:
    # group() 以str形式返回对象中match的元素
    print(match.group())
    print(type(match.group()))
    # start() 返回匹配的开始位置
    print(match.start())
    # end() 返回匹配的结束位置
    print(match.end())
    # span() 以tuple形式返回范围
    print(match.span())


