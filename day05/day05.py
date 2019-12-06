# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 输出一个元素
print(L[0])
# 输出前N和元素
r = []
for i in range(3):
    r.append(L[i])
print(r)

# 或者 均表示下标
print(L[0:3])
# 0可省略
print(L[:3])
print(L[1:3])
# -号下表的使用
L = list(range(100))
print(L[:10])
print(L[-10:])
# 间隔取数每两个数取出一个
print(L[:10:2])
# 所有数，每5个取一个：
print(L[::5])


def trim(s):
    if len(s) == 0:
        return s
    elif s[0] != ' ' and s[-1] != ' ':
        return s
    elif s[0] == ' ':
        return trim(s[1:])
    elif s[-1] == ' ':
        return trim(s[:-1])
    return s


print(trim("     ssfdf "))
