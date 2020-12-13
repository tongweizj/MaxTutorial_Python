# 字典创建

a = {
    1: 'a',
    2: 'b',
    '3':'c'
}
# key 必须是不可改变的数据类型， 列表不能做key
print(a)

b = dict()
b = dict(a='a', b='b')
print(b.get('a'))