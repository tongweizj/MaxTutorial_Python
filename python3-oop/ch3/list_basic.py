a= [1, 2, 3]
b = [1, 'abc', 2.0, ['a', 'b', 'c']]

print(a)
print(b)

# 通过index来访问列表中数值
a[0]
print(a[0], a[1])

# 通过切片来显示

print(b[1:3])

s= 'abcdef'
print(s[1:3])   # 不显示 s[3]


print(len(s))

print(max(a))

a.append(4)
print(a)

list1 = [1, 2, 3, 4]
list2 = list1*2 + [4, 5, 6]
print(list2)