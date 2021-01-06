import bisect

# 新插入元素在原列表中没有
li = [1, 3, 5, 7, 9]
print(bisect.bisect_left(li, 6))
print(bisect.bisect_right(li, 6))
print(bisect.bisect(li, 6))
print("-"*30)

# 新插入元素在原列表中有
li = [1, 3, 4, 4, 4, 7, 8]
print(bisect.bisect_left(li, 4))
print(bisect.bisect_right(li, 4))
print(bisect.bisect(li, 4))
print("-"*30)

# 新插入元素在原列表中没有
bisect.insort_left(li, 6)
print(li)
bisect.insort_right(li, 4)
print(li)
bisect.insort(li, 8)
print(li)
print("-"*30)

# 新插入元素在原列表中没有
bisect.insort_left(li, 4)
print(li)
bisect.insort_right(li, 4)
print(li)
bisect.insort(li, 4)
print(li)

