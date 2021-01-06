# str.find(str, beg=0, end=len(string))
# find()方法检测字符串中是否包含子字符串 str
# 如果指定beg（开始）和end（结束）范围，则检查是否包含在指定范围内
# 返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1


str1 = "Runoob example....wow!!!"
str2 = "exam"

print(str1.find(str2))
print(str1.find(str2, 5))
print(str1.find(str2, 10))