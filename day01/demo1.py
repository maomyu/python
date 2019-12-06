print('hello')
print('I\'m \"OK\"')
print('I\'m learning\nPython.')
# 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容，
print('''line
line2

line3''')
print(not 1 > 2)
age = 1
if age >= 18:
    print('adult')
else:
    print('teenager')

# 全部大写的变量名表示常量
PI = 3.14159265359
# /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：
print(9/3)