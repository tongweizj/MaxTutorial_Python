name: str = 'Python'
age = '27'

#

new_str = "我是 {}, 今年 {} 岁了".format(name, age)
new_str2 = "我是 {name}, 今年 {age} 岁了".format(
    name = 'Python', age = '27')
print(new_str2)


new_str3 = f"我是 {name}, 今年 {age} 岁了"
print(new_str3)